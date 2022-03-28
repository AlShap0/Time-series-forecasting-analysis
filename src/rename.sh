#!/bin/bash

for file in "$@"
do
	#echo 'en_climate_daily_QC_702S006_2003_P1D.csv'| awk -F '[_]' '{print $6}'
	name=$(echo $file| awk -F '[_]' '{print $6}')
	name=$name'_data.csv'
	mv $file ../data/$name 
done
