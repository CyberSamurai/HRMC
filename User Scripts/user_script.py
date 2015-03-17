# load in user files
admins_file = open('C:\\TEMP\\users_admins_conv.txt','r')
providers_file = open('C:\\TEMP\\users_providers_conv.txt','r')
radiologists_file = open('C:\\TEMP\\users_radiologists_conv.txt','r')
techs_file = open('C:\\TEMP\\users_technicians_conv.txt','r')

admins = admins_file.readlines()
providers = providers_file.readlines()
radiologists = radiologists_file.readlines()
techs = techs_file.readlines()


user_lists = [admins, providers, radiologists, techs]

# remove irrelevant data and strip whitespace
for usergroup in user_lists:

    for line in list(usergroup):
        if not line.startswith('HPTLWIN'):
            usergroup.remove(line)
    for i in range(len(usergroup)):
        usergroup[i] = usergroup[i].strip()


# Write cleaned up data to one single CSV file
users_file = open('.\\users_full.csv', 'w')
users_file.write("User Level, UserID, F-name, L-name\n")
for user in user_lists[0]:
    users_file.write("Admin, "+ user + ", "+","+"\n")
for user in user_lists[1]:
    users_file.write("Provider, "+ user + ", "+","+"\n")
for user in user_lists[2]:
    users_file.write("Radiologist, "+ user + ", "+","+"\n")
for user in user_lists[3]:
    users_file.write("Tech, "+ user + ", "+","+"\n")

users_file.close()
