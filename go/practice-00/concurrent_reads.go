// This program creates a set of threads that will wait for input from
// a channel, and process the input.

package main

import (
	"fmt"
)

// Send integers in the sequence 0, 1, ..., loop_limit to int channel ch.
// When generation is complete, send '0' to the signal channel.
// ---------------------------------------------------------------------------
func generate_integers(loop_limit int, ch chan<- int, signal_chan chan<- int) {

	//fmt.Println("Entering generate_integers...")

	for loop_counter := 0; loop_counter < loop_limit; loop_counter++ {
		ch <- loop_counter // Send the current loop value to the int channel.
	}

	//fmt.Println("Exiting generate_integers...")
	signal_chan <- 0
	return
}

// Read integers from the int channel, and print them to the terminal,
// along with the ID of the current function that is running. Send the
// value read from the input channel to the output channel.
// Before each read operation, check for a signal from the signal channel.
// ---------------------------------------------------------------------------
func read_integers(proc_id int, input_chan <-chan int,
	outout_chan chan<- int, signal_chan <-chan int) int {

	//fmt.Println("Entering read_integers...")

	var my_val int

	for {
		my_val = <-input_chan
		//fmt.Println("My ID: ", proc_id, "Handled Value: ", my_val)
		outout_chan <- my_val

		if len(signal_chan) > 1 {
			my_signal := <-signal_chan
			return my_signal
		}
	}
}

// Check the input signal channel for values, return true/false.
func check_generation_finished(input_signal_channel chan int) bool {
	if len(input_signal_channel) > 0 {
		return true
	} else {
		return false
	}
}

// Return true if the boolean parameter is true, and the input channel is empty.
func main_is_finished(generation_finished bool, input_chan chan int) bool {
	if generation_finished && len(input_chan) == 0 {
		return true
	} else {
		return false
	}
}

// This function will send a kill message to each thread in the thread pool.
func terminate_threads(thread_signal_channel_pool []chan int) {
	for current_channel := range thread_signal_channel_pool {
		thread_signal_channel_pool[current_channel] <- 0
	}
}

func main() {

	// Program parameters:
	number_of_threads := 5   // Number of handling threads to create
	number_of_values := 1000 // Number of values to generate for input

	thread_output_channel_buffer_size := 3 // Size of thread output channel buff.
	input_channel_buffer_size := 10        // Size of input channel buffer.

	// Create input channel
	var input_channel = make(chan int, input_channel_buffer_size)
	var input_signal_channel = make(chan int, 1)
	// Create thread channel pools
	var thread_signal_channel_pool = make([]chan int, number_of_threads)
	var thread_output_channel_pool = make([]chan int, number_of_threads)

	for i := range thread_signal_channel_pool {
		thread_signal_channel_pool[i] = make(chan int, 1)
	}

	for i := range thread_output_channel_pool {
		thread_output_channel_pool[i] = make(chan int, thread_output_channel_buffer_size)
	}

	// Control flow checks
	var generation_finished bool = false

	// Spawn input generation thread:
	go generate_integers(number_of_values, input_channel, input_signal_channel)

	// Spawn thread processes
	for i := 0; i < number_of_threads; i++ {
		go read_integers(i, input_channel, thread_output_channel_pool[i],
			thread_signal_channel_pool[i])
	}

	// Main program loop:
	// --------------------------------------------------------------------------
	for {
		// First, check whether the generation is finished, and whether to exit.
		generation_finished = check_generation_finished(input_signal_channel)
		if main_is_finished(generation_finished, input_channel) {
			terminate_threads(thread_signal_channel_pool)
			return
		}

		// Next, read input from each channel:
		for current_channel := range thread_output_channel_pool {
			thread_output_val := <-thread_output_channel_pool[current_channel]
			fmt.Println("Thread #", current_channel, "\thandled value: ", thread_output_val)
		}
	}
}
