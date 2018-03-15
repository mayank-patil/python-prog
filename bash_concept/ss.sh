#!/bin/bash
echo "enter a no. between 1 to 3"
read a
if [ $a == 1 ]
then
echo "the no. is $a"
elif [ $a == 2 ]
then 
echo "the no. is $a"
elif [ $a == 3 ]
then 
echo "the no. is $a"
else
echo "you failed to follow instructions."
fi

