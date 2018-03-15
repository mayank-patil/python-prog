#!/bin/bash
echo "enter a filename"
read f
while read -r supes;do
echo "supes name: $supes"
done < "$f"

