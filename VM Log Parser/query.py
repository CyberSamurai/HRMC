# code for all the queries and reports

import parselogs


def query_user(query_choice):
    """menu_choice(int) -> Writes query output to file (NoneType)
    Performs query based on query_choice(int) and writes results to output
    file and launches file for viewing.
    """
    if type(query_choice) != 'int':
        return "Invalid choice, query_choice must be an integer"
    if query_choice == 1:
        pass #insert code for query 1 - What IP did they login from
    if query_choice == 2:
        pass #insert code for query 2 - Successful login attempts
    if query_choice == 3:
        pass #insert code for query 3 - Failed login attempts
    if query_choice == 4:
        pass #insert code for query 4 - Summary report
