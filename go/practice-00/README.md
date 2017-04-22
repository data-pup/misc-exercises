# GO\_CHANNEL\_EXERCISES
An exercise using Go, demonstrating a race condition and fixing the error.

One of the Go language's most helpful features is the goroutine. However, if not handled properly this can lead to race conditions that will cause an error during the program's execution. This repository includes code that I wrote learning how to use this concurrency, and how to prevent a deadlock when the channels are empty.

The goal of the program was to create a goroutine that will generate a sequence of integers, and send them to an input channel. Then, a set of different goroutines will read from this channel and send the values to individual output channels. This helped me understand more about concurrency and scheduling within Go.

The 'concurrent\_reads\_with\_race\_condition.go' program will sometimes end with a deadlock, and exit with an error code.

The 'concurrent\_reads.go' program shows how I tried to implement a solution to this problem. I also improved the function to allow for a variable number of threads within a thread pool. Each goroutine sends its output to a specific channel within an array, and will stop when it receives an input through a separate signal channel.
