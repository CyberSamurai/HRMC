# Script to check for non-existent or disabled users in AD and add denotion

import active_directory

# open csv file as a list
FILEPATH = 'C:\\TEMP\\Users_input_WIP.csv'
with open(FILEPATH, 'r') as userfile:
    masterlist = [line.split(',') for line in userfile]

#clean up extra white space
for user in masterlist:
    for i in range(len(user)):
            user[i] = user[i].strip()

# pull userid to query AD and cleanup; add AD descriptions
for user in list(masterlist):
    u = active_directory.find_user(user[1])
    if u is None:
        masterlist.remove(user)
    else:
        try:
            desc = u.description.encode('ascii','ignore')
            user.append(desc)
        except AttributeError:
            user.append("")
    try:
        if 'ADS_UF_ACCOUNTDISABLE' in u.userAccountControl:
            masterlist.remove(user)
    except AttributeError:
         pass

    
# Write new data to CSV file
outfilename = 'C:\\TEMP\\Users_output_WIP.csv'
with open(outfilename, 'w') as outputfile:
    for user in masterlist:
        outputfile.write(user[0]+','+user[1]+','+user[2]+','+user[3]+'\n')
