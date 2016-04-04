#!/bin/bash
checkon=$(ps aux | grep python | wc -l)
echo $checkon
if [ $checkon -eq 2 ]
	then
		echo "ik denk dat ie draait"
	else 
		echo "wtf"
fi


