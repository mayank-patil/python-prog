#!/bin/bash
#testing the existence of a file name
filename=$1
echo "testing for file"

if [  -a $filename ]
then
echo "file $filename don't exist"
fi

