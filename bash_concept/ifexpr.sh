#!/bin/bash
filename=$1

echo "testing for file $filename"

if [ -f $filename ] && [ -r $filename ]
then
	echo "file $filename exist and is readable"
fi
