
RIS_USERS_PATH = 

with open(RIS_USERS_PATH, 'r') as risusersfile:
    risusers = risusersfile.readlines()
    users = [user.split(',') for user in risusers]
    for user in users:
            user = [element.strip() for element in user]
