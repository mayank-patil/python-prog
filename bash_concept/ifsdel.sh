#!/bin/bash
#delimiting [Space],|and other symbols and charcater 
#IFS should be capital
echo "enter file name to parse:"
read file

echo "enter the delimeter:"
read dlim

IFS="$dlim"
while read -r CPU MEM DI;do
	echo "cpu: $CPU"
	echo "memory: $MEM"
	echo "DISK: $DI"
done <"$file"
