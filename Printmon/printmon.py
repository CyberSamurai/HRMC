#!C:\Python27\python

"""
Batch Print Tool
Written by Greg Morford
Date: 7/30/2013
License: See LICENSE.txt
Intended Purpose:  Monitor specified directory on Windows server. print
 incoming text files then delete them.

"""

import win32print
from os.path import isfile
import glob
import os
import time
import win32com.shell.shell as shell
import win32event


#Set this to be whichever directory is to be monitored
source_path = "c:\\temp\\source\\"  #[]Add argv to pass this directory as command arg


def main():
    """Main program that iterates through file list, prints each iteration,
    then deletes it."""
    printer_name = win32print.GetDefaultPrinter()
    while True:
        file_queue = [f for f in glob.glob("%s\\*.txt" % source_path) if isfile(f)]
        if len(file_queue) > 0:
            for i in file_queue:
                print_file(i, printer_name)
                delete_file(i)
                print "Filename: %s has printed" % i
        else:
            print "No files to print. Will retry in 15 seconds"
        time.sleep(15)


def print_file(pfile, printer):
    """prints 'pfile' to 'printer' and waits for the handle to signal.
    ShellExecuteEx fMask parameter note:
    SEE_MASK_NOASYNC(0x00000100)=256 + SEE_MASK_NOCLOSEPROCESS(0x00000040)=64
    """
    handle = shell.ShellExecuteEx(
    fMask = 256 + 64,
    lpVerb = 'print',
    lpFile= pfile,
    lpParameters = printer
    )
    hprocess = win32event.WaitForSingleObject(handle['hProcess'], -1)
    return hprocess


def delete_file(f):
    os.remove(f)

    
##Placeholder for future alert functionality
def alert(email):
    pass
    
main()
