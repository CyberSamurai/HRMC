#!/bin/bash

# Author:  Greg Morford
# Date:  03/10/2015
# Description: To create TAG file for processing non-ascii files in EDM
# Revision History: 
#
# TODO: 
# 1. Add parameter support for source & destination.


# Note, the IBEX_Chart batch file is copying these images from ibex server to our source directory.

# User variables
imagesource="/cygdrive/c/tmp/imagesource/"
tempdir="/cygdrive/c/tmp/imagetest/"
OLCReports="/cygdrive/c/tmp/OLCReports/"
Upload="/cygdrive/c/tmp/OLC_UPLOAD_S0AR/"
imagelist="/cygdrive/c/tmp/tagtest/image.list"
tagfile="/cygdrive/c/tmp/tagtest/ibex_images.tag"
fname="${tagfile##*/}"


# Checking for existence of files to start processing.
files=$(shopt -s nullglob dotglob; echo ${imagesource}SITE1*.JPG)
if (( ${#files} )); then
  # Using a temp working directory so new files aren't introduced during iteration.
  mv ${imagesource}SITE1*.JPG $tempdir
else echo "No files found."; exit 0
fi


# Check for existence of previous image.list; do not want to overwrite it on next awk run.
if [[ -f $imagelist ]]; then
  echo "Previous run did not complete; please clean up files: $imagelist"; exit 1
fi

# Build our image file list to parse with awk.
for entry in ${tempdir}* ; do
  if [[ -e $entry ]]; then
    echo ${entry##*/} >> $imagelist
    # Put images where they can be retrieved by the OLC per EDM manual.
    mv "$entry" $OLCReports
  else echo "File $entry not found.  Trying next file..."; continue
  fi
done


# Build our TAG file with awk.
## First need number of lines to test for end of file to leave off last form feed character.
## RegEx to put parts of filename into array for EDM indexes. 
## Print each line as specified in EDM manual TAG file guidelines.
## Test for last line to make sure we don't add form feed on end.
## Sourcing $imagelist file and output into tag file.
awk -v nlines=$(wc -l < $imagelist ) 'match($0,/^SITE1_([0-9]+)_([0-9]+)_([A-Za-z0-9_-]{1,})\.JPG$/,ary) {
    print "ENCNO:  "ary[2]"\t\t""DOCDATE:  "ary[1]"\t""LABELSTR:  "ary[3]"\n""FILE:\\\\DITEST\\TEST\\OLCReports\\"$1"\n"
  }
  NR != nlines {
    print "\f"
  }
  ' $imagelist > $tagfile # [] Need to put some error checking/logging here.


# Put .tag file into EDM UPLOAD with unique date-time stamp name.
if [[ -w $Upload ]]; then
  mv $tagfile ${Upload}${fname%.*}_$(date '+%Y%m%d%H%M%S').${fname##*.}
else echo "Upload directory write permission denied."; exit 1
fi

# Cleanup after ourselves so next iteration can run.
if [[ -e $imagelist ]]; then
  rm $imagelist
  exit 0
fi
