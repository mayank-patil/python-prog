#!/bin/bash
#reading and writing a file
echo "enter file name :"
read file

exec 5<>$file #to open a file for read and an write

while read -r supes;do
	echo "superhero name: $supes"
done <&5 #read from file

echo "file was read  on : `date`" >&5 #write in file

exec 5>&- #close descripter in file
