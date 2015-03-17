import active_directory


#Create a list from the "users_full.csv" file
FILEPATH = 'C:\\TEMP\\users_full.csv'
with open(FILEPATH, 'r') as userfile:
    masterlist = [line.split(',') for line in userfile]
    
#create an AD_object for each user while ignoring disabled users
for user in list(masterlist):# had to prune out disabled users first
    u = active_directory.find_user(user[1])
    if 'ADS_UF_ACCOUNTDISABLE' in u.userAccountControl:
        masterlist.remove(user)

for user in masterlist:
    u = active_directory.find_user(user[1])
    user.insert(2, u.firstName.encode('ascii','ignore'))
    user.insert(3, u.lastName.encode('ascii','ignore'))
    user.remove('')

### ++Notes about above queries on AD_object++
### variable = active_directory.find_user("morfordg")
### can view all it's properties with object.properties
### can call individual properties...
### variable.firstName returns u'Greg'
### variable.lastName returns u'Morford'
### note these return unicode strings
### to convert from UTF to ASCII use encode() as seen above
   

# for each user in list, write to a new csv file in this format:
### userlevel,username,Fname,Lname
NEWPATH = 'C:\\TEMP\\new_users_full.csv'
with open(NEWPATH, 'w') as newfile:
    for item in masterlist:
        for p in item:
            if p == '\n':
                
            newfile.write(p+",")
            

#Note, the above write() had to be cleaned up in notepad++ to get rid of extra
#commas. Didn't have to time to fix script to cleanly write the csv file.
            
            
