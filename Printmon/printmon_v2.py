#!C:\Python27\python

#Directory Batch Print Tool
#Written by Greg Morford
#Date: 7/30/2013
#Intended Purpose:  Monitor specified directory on Windows server. print
#                   incoming text files then delete them.


#Documentation for the pywin32 win32print module used
#http://docs.activestate.com/activepython/2.7/pywin32/win32print.html

import win32print
import win32api
from os.path import isfile, join
import glob



#Main program loop that iterates through file list, prints each iteration,
#then deletes it.  Not need to bother with temp file queue because list
#iteration should know of all the current files.
def main():
    watchQueue = "c:\\temp\\"  #[] Look at adding argv to pass this directory as command argument
    printer_name = win32print.GetDefaultPrinter()
    fileQueue = [f for f in glob.glob("%s\\*.*" % watchQueue) if isfile(join(watchQueue, f))]
    for i in fileQueue:
        if #file type is raw text:
            printRawFile(i, printer_name)
        else:
            printFile(i, printer_name)
        if #insert some kind of logic to check print status:
            alert(morfordg@hutchregional.com)
        elif #successful print:
            deleteFile(i)


#-=-=Define the raw text or pcl print function=-=-
#[] Need code for exceptions/failed prints to fire off alerts
def printRawFile(document, printer_name):
    hPrinter = win32print.OpenPrinter(printer_name)
    try:
        win32print.StartDocPrinter(hPrinter, 1, ("Untitled", None, "RAW"))
        try:
            win32print.StartPagePrinter(hPrinter)        
            win32print.WritePrinter(hPrinter, raw_data) #see docs for args
            win32print.EndPagePrinter(hPrinter)
        finally:
            win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)


#-=-=Define the general purpose shellexecute print function=-=-
def printFile(document, printer_name):
    win32api.ShellExecute(
        0,
        "print",
        str(document),
        '/d:"%s"' % printer_name,
        ".",
        0
    )


#-=-=Define the alert on errors=-=-
def alert(email):
    


#-=-=Define the delete function=-=-
def deleteFile():
