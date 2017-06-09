#!/bin/bash

if [ $# -ne 1 ]; then
    echo $0: usage: final_publisher path_name
    exit 1
fi

path=$1

counter=1
echo "Starting Publisher using Mosquitto"
echo "----------------------------------"
while true; do
	cmd_str="mosquitto_pub -r -t '$path' -m 'Hello_$counter'"
	echo "Running command : "$cmd_str
	eval $cmd_str
	sleep_cmd="sleep 3"
	eval $sleep_cmd
	counter=$((counter+1))
done
