#!/bin/bash
### ----------------------------------------------------------------------- ###
###                    Hello! I am the Fibonacci Quine.
### ----------------------------------------------------------------------- ###
### I have been called 0 time(s).
### The current Fibonacci value is: 0
### ----------------------------------------------------------------------- ###
### A 'quine' is a program that prints its own source code as its output.
### I am a little bit different however! As you can see up above, I will keep
### track of how many times this program has been invoked. As an added bonus,
### I will also show the value at the corresponding position in the Fibonacci
### sequence!
###
### To try this out, place this code in a file named 'fibonacci-quine.sh'
### If you run this script using './fibonacci-quine.sh' you should see this
### message, with a minor exception. The message above will have changed!
### How does this work? Magi-lol, Jk! Here's how! I am a quine after all. :o)
### ----------------------------------------------------------------------- ###

# Declare the name of this file, and a register for saving previous Fibonacci
# values. (Note: the header effectively functions as a second register.)
FILENAME="fibonacci-quine.sh"
FIB_REGISTER=1

# Use sed to find the current contents of any lines in this file to be modified.
COUNTER_LINE=$(sed -n '5p' "$FILENAME")
FIB_HEADER_LINE=$(sed -n '6p' "$FILENAME")
FIB_REGISTER_LINE=$(sed -n '23p' "$FILENAME")

# Create blank versions of the Fibonacci header and register lines, by
# stripping the numbers from the lines.
BLANK_FIB_HEADER_LINE=$(echo "$FIB_HEADER_LINE" | sed -e 's/[0-9]//g')
BLANK_FIB_REGISTER_LINE=$(echo "$FIB_REGISTER_LINE" | sed -e 's/[0-9]//g')

# Find the previous counter value, increment the counter, and create a new line.
COUNTER_VALUE=$(echo "$COUNTER_LINE" | sed -e 's/[^0-9]//g')
NEW_COUNTER_LINE="### I have been called $(($COUNTER_VALUE+1)) time(s)."

# Identify the Fibonacci value in the header, find the next Fibonacci value.
FIB_HEADER_VALUE=$(echo "$FIB_HEADER_LINE" | sed -e 's/[^0-9]//g')
NEW_FIB_HEADER_VALUE=$(($FIB_HEADER_VALUE + $FIB_REGISTER))

# Create a new header line, using the next value in the sequence.
NEW_FIB_HEADER_LINE="$BLANK_FIB_HEADER_LINE$NEW_FIB_HEADER_VALUE"

# Store the previous header value in the register, create a new source line.
NEW_FIB_REGISTER_LINE="$BLANK_FIB_REGISTER_LINE$FIB_HEADER_VALUE"

# Create a temporary directory.
TEMPDIR=$(mktemp -dt "$(basename "$0").XXXXXXXXXX")

# Create a file within the temporary directory.
TEMPFILE=".temp-$FILENAME"
TEMPFILE_ABSOLUTE_PATH="$TEMPDIR/$TEMPFILE"
touch "$TEMPFILE_ABSOLUTE_PATH"

# Using awk, replace lines in the tempfile with our new values.
awk -v newcounterline="$NEW_COUNTER_LINE" \
-v newfibline="$NEW_FIB_HEADER_LINE" \
-v newregline="$NEW_FIB_REGISTER_LINE" \
  '(NR == 5) { print newcounterline }; \
  (NR == 6) { print newfibline }; \
  (NR == 23) { print newregline }; \
  (NR != 5 && NR != 6 && NR != 23) { print };' \
    "$FILENAME" > "$TEMPFILE_ABSOLUTE_PATH"

# /bin/cat "$TEMPDIR/$TEMPFILE"    # DEBUG: Print the temp file, when testing.

# Move the edited file into place, set the executable permission on the file.
mv "$TEMPFILE_ABSOLUTE_PATH" "$FILENAME"
chmod u+x "$FILENAME"

# Remove the temporary directory that we created previously.
rm -rf "$TEMPDIR"

# Print the contents of this file, and pipe the results to less.
/bin/cat "$FILENAME" | less
