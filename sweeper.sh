#!/usr/bin/env bash

folder_name=$1
echo Moving all the results into $folder_name ... 

# combine multiple surface files
for ii in `ls surface_eps*.dat`
do 
    jj=`echo $ii | cut -f 1-3 -d _ `
    cat $jj\_*.dat > $jj.dat
done
rm surface_eps_*_*.dat 2> /dev/null

mkdir $folder_name
mv *.dat $folder_name
mv *.err $folder_name
mv *.log $folder_name
cp music_input_2 $folder_name/music_input
mv $folder_name/known_nuclei.dat ./
rm -fr $folder_name/tmp*.dat
