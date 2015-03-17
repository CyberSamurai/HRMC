#!/bin/bash

#This takes a LONG time as it loops through every archive for each
#file in the list
while read LINE; do
    find . -iname "*$LINE*" -exec cp {} /cygdrive/z/Restored_Files/ \;
done < ../files_test.txt


#Determine file type and append the extension to the filename
for i in *;
    do
        filetype=$(file "$i" | awk '{print $2}')
        case $filetype in
            TIFF) ext="tif"
                ;;
            PDF) ext="pdf"
                ;;
            ASCII) ext="txt"
                ;;
            Rich) ext="rtf"
                ;;
            gzip) ext="gz"
                ;;
        esac
        mv "$i" "$i.$ext"
done