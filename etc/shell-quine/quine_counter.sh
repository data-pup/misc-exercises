#!/bin/bash

COUNTER=0
FILENAME="quine_counter.sh" # This line *MUST* contain the name of this file.
echo "$FILENAME has been invoked $COUNTER times"

PREVIOUSCOUNTERLINE=$(/bin/cat $FILENAME | grep "^COUNTER=" | head -n 1 )
### echo "Previous counter line found: $PREVIOUSCOUNTERLINE"

NEWCOUNTERLINE="COUNTER=$((COUNTER+1))"
### echo "New counter line: $NEWCOUNTERLINE"

SEDCOMMAND="1,/^COUNTER=/s/${PREVIOUSCOUNTERLINE}/${NEWCOUNTERLINE}/"
### echo "Sed command: $SEDCOMMAND"

TEMPFILE=$(mktemp /tmp/_quine_counter.XXXXX) || exit 1
### echo "Obtained temporary file $TEMPFILE"

### echo "Replacing counter line..."
sed -e "${SEDCOMMAND}" $FILENAME > $TEMPFILE

### echo "Contents of new file:" # DEBUG
# cat $TEMPFILE # DEBUG
### echo && echo # DEBUG

### echo "Replacing previous file..."
/bin/cat $TEMPFILE > $FILENAME

### echo "Removing tempfile..."
rm $TEMPFILE
