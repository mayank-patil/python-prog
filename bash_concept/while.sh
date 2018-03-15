#!/bin/bash
#while loop 
echo "enter display count of a string"
read a
echo "enter the string"
read s
count=1

while [ $count -le $a ]
do
	echo "$s - $count"
	count="`expr $count + 1`"
done
