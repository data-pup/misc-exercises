// This is a basic example of working with multiple channels. 
// In one function, generate a string of values,
// in another function, print out the value, and which function
// read the function.

// What I learned writing this program: I learned how to work with
// concurrent processes that can handle different output channels, and
// how to read from each channel from inside of the main function.

// Problems I encountered: The program will hit a deadlock and fail
// when the generation function is done creating integers. This is a
// problem that I need to figure out how to solve.

// This program demonstrates a race condition in Go. Potentially, this
// program will end with a deadlock, with exit status 2.

package main

import (
	"fmt"
)

// Send integers in the sequence 0, 1, ..., loop_limit to int channel ch.
func generate_integers(loop_limit int, ch chan<- int) {
	fmt.Println("Entering generate_integers...")
	for loop_counter := 0; loop_counter < loop_limit; loop_counter++ {
		fmt.Println("Generated the int value ", loop_counter, " and sent to input_channel.")
		ch <- loop_counter // Send the current loop value to the int channel.
	}
	fmt.Println("Exiting generate_integers...")
}

// Read integers from the int channel, and print them to the terminal,
// along with the ID of the current function that is running. Send the
// value read from the input channel to the output channel.
func read_integers(proc_id int, input_chan <-chan int, outout_chan chan<- int) {
	fmt.Println("Entering read_integers...")
	for {
		my_val := <-input_chan
		fmt.Println("My ID: ", proc_id, "Handled Value: ", my_val)
		outout_chan <- my_val
	}
}

func main() {

	number_of_loops := 100
	output_channel_buffer_size := 10

	fmt.Println("Creating channels...")
	input_channel := make(chan int)
	output_channel_1 := make(chan int, output_channel_buffer_size)
	output_channel_2 := make(chan int, output_channel_buffer_size)
	fmt.Println("Created channels...")

	fmt.Println("Generating integers...")
	go generate_integers(number_of_loops, input_channel)

	fmt.Println("Begin reading threads...")
	go read_integers(1, input_channel, output_channel_1)
	go read_integers(2, input_channel, output_channel_2)

	for i := 0; i < number_of_loops/2-2; i++ {
		chan1_val := <-output_channel_1
		chan2_val := <-output_channel_2
		fmt.Println("Main function read the values ", chan1_val, " and ", chan2_val, " from the concurrent output channels.")
	}
}
