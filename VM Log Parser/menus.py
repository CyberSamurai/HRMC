# Code for all of the menus

import parselogs

# Globals and functions

main_menu_choice = ''

def MENU_MAIN():
    global main_menu_choice
    print """--Greg's Magic Log Reader--\n
      Main Menu
     ___________________
    |                   |
    |1. Query by user   |
    |2. Query by IP     |
    |3. Query by event  |
    |4. Refresh logs    |
    |0. Exit            |
    |___________________|
    """
    main_menu_choice = raw_input("Choose an option: ")


def MENU_USER():
    print """
      Query by user
     ____________________________________
    |                                    |
    |1. How many times did user login?   |
    |2. What IP did they login from?     |
    |3. How many failed login attempts?  |
    |4. Summary Report                   |
    |5. Go back to main menu             |
    |0. Exit                             |
    |____________________________________|

    """
    return raw_input("Choose an option: ")


def MENU_IP():
    print """
      Query by IP Address
     ____________________________________
    |                                    |
    |1. How many times did IP login?     |
    |2. What users logged in on this IP? |
    |3. How many failed login attempts?  |
    |4. Summary Report                   |
    |5. Go back to main menu             |
    |0. Exit                             |
    |____________________________________|

    """
    return raw_input("Choose an option: ")


def MENU_EVENT():
    print """
      Query by event
     ____________________________________
    |                                    |
    |1. Show successful logins           |
    |2. Show failed logins               |
    |3. Go back to main menu             |
    |0. Exit                             |
    |____________________________________|

    """
    return raw_input("Choose an option: ")


def MENU_REFRESH():
    print """
    REFRESHING LOG DATA... Please Wait...

    """
    parselogs.main()

##print MENU_MAIN
##print MENU_USER
##print MENU_IP
##print MENU_EVENT
##print MENU_REFRESH


MENU_MAIN()
if type(main_menu_choice) != 'int':
    
if int(main_menu_choice) not in [1,2,3,4,0]:
    print "\nInvalid choice!  Please select a valid menu option.\n"
    raw_input("Press Enter to continue")
    MENU_MAIN()


