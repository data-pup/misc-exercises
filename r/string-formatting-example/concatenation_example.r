# This is an example of string formatting in R within a for loop.
# This is helpful for cases when you might be generating multiple output files,
# for example.
#
# NOTE: This example uses the cat function. Cat is for concatenating and then
# printing the string that we have formatted. If you would like to put this
# into a variable, you can use the paste function.
#
# This function will find the suffix of an integer for the loop's output.
# For example, "4th" or "1st"

find_number_suffix <- function(my_number) {
    # Find the least significant decimal digit of the parameter
    my_last_digit <- as.numeric(my_number) %%  10

    # This group of statements will check for "teen" numbers, which have
    # different suffixes when written out.
    if( (as.numeric(my_number)>10) && (as.numeric(my_number)<20) ) {
        return ("th")
    }

    # Return a different string for different cases, otherwise return "th"
    if(my_last_digit == 1){ return ("st")}
    if(my_last_digit == 2){ return ("nd")}
    if(my_last_digit == 3){ return ("rd")}
    else { return ("th")}
}

# Here is the loop where we will format output. Be sure to set the sep option.
for( i in 1:25 ) {
    my_numeric_suffix <- find_number_suffix(i)
    cat("We are currently executing the ",trimws(format(i),which="both"), trimws(format(my_numeric_suffix),which="both"), " loop iteration\n", sep="")
}
