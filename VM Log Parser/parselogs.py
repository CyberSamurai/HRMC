import glob
import os.path
import datetime

# Constants
LOG_SOURCE = "\\\\server\\share"

EVENT1 = 'EventType="BROKER_USER_AUTHFAILED_BAD_USER_PASSWORD"'
EVENT2 = 'EventType="BROKER_USERLOGGEDIN"'
EVENT3 = 'EventType="BROKER_USERLOGGEDOUT"'

year = datetime.date.today().isoformat()[:4]


logfilenames = [f for f in glob.glob("%s\\*.log" % LOG_SOURCE) if os.path.isfile(f)]
parsed_data = [] # Create list to dump clean results into
if len(logfilenames) > 0:
    for logfilename in logfilenames:
        
        with open(logfilename, 'r') as logfile:
            logdata = logfile.readlines()

            for line in logdata:
                if EVENT1 in line or EVENT2 in line or EVENT3 in line:
                    parsed_data.append(line)

            
        clean_parsed_data = []
        clean_parsed_data.append("Date "+"Time "+"EventType "+"UserName "+"IP-Address\n")
        expanded_parsed_data = [i.split(" ") for i in list(parsed_data)]
        for line in expanded_parsed_data:
            for substring in line:
                if substring.startswith(year+"-"):
                    clean_parsed_data.append(substring[:-10].replace('T',' ')+" ")
                if substring.startswith('EventType'):
                    clean_parsed_data.append(substring.replace('EventType="BROKER_USER',"").replace(
                        '_AUTHFAILED_BAD_USER_PASSWORD','AUTHFAILED').rstrip('"')+" ")
                if substring.startswith('UserDisplayName'):
                    clean_parsed_data.append(substring.replace('UserDisplayName="',"").rstrip('"]')+" ")
                if substring.startswith('ClientIpAddress'):
                    clean_parsed_data.append(substring.replace('ClientIpAddress="',"").rstrip('"]')+" ")
            clean_parsed_data.append("\n")
            
        parsed_filename = '\\\\server\\share\\temp\\parsed_logdata.txt'

        with open(parsed_filename, 'w') as cleanfile:
            cleanfile.writelines(clean_parsed_data)
