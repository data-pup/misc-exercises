/* This is the Fizz-Buzz exercise implemented in the Go language.
 * It will print the sequence of numbers from 1 to 100.
 * If a number is divisible by 3, then 'Fizz' will be printed instead.
 * If a number is divisible by 5, then 'Buzz' will be printed instead.
 * If a number is divisble by both, then 'FizzBuzz' will be printed.
 * ---------------------------------------------------------------------------
 *
 * Program Overview:
 * ---------------------------------------------------------------------------
 * Main function will create the following routines:
 *   - generate_integers
 *   - generate_output_term
 *
 * The main function will make two goroutine calls,
 * after establishing channels for passing values between functions.
 *
 * The generate_integers function will send integer values to a channel,
 * until it reaches a loop limit, which will send a final int value of -1.
 *
 * The generate_output_term function will read integers from a channel,
 * (the channel being filled by generate_integers) and generate a string
 * according to the rules of the FizzBuzz game. Values divisible by
 * 3 will return 'Fizz', values divisible by 5 will return 'Buzz', and
 * values that are divisble by both will return 'FizzBuzz'. Other values
 * will return the input integer given to the function represented as
 * a string.
 * ---------------------------------------------------------------------------
 *
 * NOTE: Be sure that the -1 sentinal value will stop the other programs.
 * This signal should be transmitted to each routine that is running.
*/

package main

import (
    "fmt"
    "strconv"
)


// ---------------------------------------------------------------------------
//                           Parallelization                                //
// ---------------------------------------------------------------------------

// ---------------------------------------------------------------------------
// Send integers in the sequence {0, 1, ...,loop_limit} to int channel ch.
// When generation is complete, send '-1' to the integer channel, and return.
// ---------------------------------------------------------------------------
func generate_integers(loop_limit int, sequence_channel chan<- int) {

  fmt.Println("Entering generate_integers...")

  for loop_counter := 1; loop_counter < loop_limit; loop_counter++ {
    sequence_channel <- loop_counter
  }

  fmt.Println("Terminating generate_integers...")

  // Send -1 to the output channel to signal that the sequence is complete.
  sequence_channel <- -1

  fmt.Println("Exiting generate_integers...")

  return
}


// ---------------------------------------------------------------------------
// This function will read integers from the sequence channel,
// and print the correct string for the output. NOTE: Don't print -1.
// ---------------------------------------------------------------------------
func generate_output_term( sequence_channel <-chan int,
  fizzbuzz_channel chan<- string) {

  // Read an integer value from the channel, and create a string.
  for {
    sequence_value := <-sequence_channel

    // If the value read from the sequence channel is -1, pass the value
    // through the channel and exit the function.
    if sequence_value == -1 {
      fizzbuzz_channel <- "-1"
      return
    }

    sequence_string := ""

    // Create a FizzBuzz return value.
    if (sequence_value % 3) == 0 {
      sequence_string = sequence_string + "Fizz"
    }
    if (sequence_value % 5) == 0 {
      sequence_string = sequence_string + "Buzz"
    }
    if sequence_string == "" {
      sequence_string = strconv.Itoa(sequence_value)
    }

    // Write the string to the fizzbuzz channel, and continue.
    fizzbuzz_channel <- sequence_string
  }
  return
}

// ---------------------------------------------------------------------------
//                               Main Function                              //
// ---------------------------------------------------------------------------

func main() {

  // Program Variables
  // ------------------------------------------------------------------------
  fmt.Println("Establishing program parameters...")
  loop_limit := 100
  buffer_size := 5


  // Routine Channels
  // ------------------------------------------------------------------------
  fmt.Println("Creating channels...")
  var raw_integer_channel = make(chan int, buffer_size)
  var fizzbuzz_channel = make(chan string, buffer_size)

  // Routine Calls
  // ------------------------------------------------------------------------
  fmt.Println("Creating rountines...")
  go generate_integers(loop_limit, raw_integer_channel)
  go generate_output_term(raw_integer_channel, fizzbuzz_channel)

  // Read/Print Loop
  // ------------------------------------------------------------------------
  my_val := ""
  my_val = <-fizzbuzz_channel

  for {
    fmt.Println(my_val)
    my_val = <-fizzbuzz_channel

    if my_val == "-1" {
      fmt.Println("Exiting loop...")
      break
    }
  }

  // End Program
  // ------------------------------------------------------------------------
  fmt.Println("Exiting...")
  return
}
