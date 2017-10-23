#!/bin/bash
TEMPLATE=$1
SCRIPT=$2

ACTUAL=$(cat $TEMPLATE)

RESULT=$(echo -e ${@:3} | ./$SCRIPT)

var=$(echo -e "$ACTUAL" | md5sum)
var2=$(echo -e "$RESULT" | md5sum)
if [[ $var == $var2 ]] ; then
    echo "test result >>> matching strings!"
else
    echo "TEST RESULT >>> ERR no match :("
    echo -e "<<<< Expected: " $ACTUAL
    echo -e "<<<<      Got: " $RESULT
fi
