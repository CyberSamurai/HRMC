# Name: ECC_Print
# Date: 8/20/2013
# Author: Greg Morford
# Description:  Set default printer to PDF print queue to send reports to EDM
# from ECC Perfusion application in Surgery. ECC autoprints to default printer.

import win32print
import subprocess

NEW_PRINTER = '\\\\server\\printer'

# Saving default printer for later to set back.
default_printer = win32print.GetDefaultPrinter()


def printer_check(printer):
    """ Check for existance of printer argument. """
    printers = win32print.EnumPrinters(
        win32print.PRINTER_ENUM_CONNECTIONS,
        None,
        4)
    for key in printers:
        if printer in key['pPrinterName']:
            return True


def set_default():
    """ Set new default printer or installs
    printer if doesn't exist then sets as default. """
    if printer_check(NEW_PRINTER):
        win32print.SetDefaultPrinter(NEW_PRINTER)
    else:
        win32print.AddPrinterConnection(NEW_PRINTER)
        win32print.SetDefaultPrinter(NEW_PRINTER)


def main():
    set_default()
    #subprocess.call(['c:\\dms32\ecc_serv_a.exe']) #Launch the app
    subprocess.call(['notepad']) # test application; remove when done
    win32print.SetDefaultPrinter(default_printer) #Set default printer back

main()



