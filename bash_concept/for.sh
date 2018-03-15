#!/bin/bash
echo "list all the content"

she=`ls *.sh`
#echo "listing in $she"
for i in "$she"; do
dis="`cat $i`"
echo "$i and content $dis"
done

