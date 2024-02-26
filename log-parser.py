#file log_file.txt has the source IP - Same port trying to access same destination, different port 
#Read file
log_lines = []
log_file = open('log_file.txt', 'r', encoding='utf-8')
log_lines = log_file.readlines()

#Cleaning extra \n empty lines
log_lines = list(map(lambda s: s.strip(), log_lines))

#cleaning empty values from the list
while ("" in log_lines):
      log_lines.remove("")

print("Log line files")
print(log_lines)

#Setting Preivous values as None
previous_sourceip = ""
previous_destip = ""
source_port = ""
dest_port= ""

#Function to set previous values of log lines
def set_value(sip, sport, dip, dport) :
     global previous_sourceip
     global source_port
     global previous_destip
     global dest_port
     previous_sourceip = sip
     source_port = sport
     previous_destip = dip     
     dest_port = dport

for l in log_lines :        
       l = l.split(" >> ")        
       print(l)
       if previous_destip == "" and  previous_sourceip =="" :
            temp_sourceip = l[0].split(":")
            temp_destip = l[1].split(":")            
            set_value(temp_sourceip[0], temp_sourceip[1],temp_destip[0],temp_destip[1])
       else: 
            if previous_sourceip in l[0] and previous_destip in l[1] :
                temp_destip = l[1].split(":")
                if dest_port not in temp_destip[1] and dest_port not in source_port:                    
                    print("There is a suspicious activity from " + previous_sourceip + " IP address")
                    print("This source IP " +previous_sourceip + ":" +source_port+ "  is trying " + dest_port + " and  " +temp_destip[1]+ "  ports" )
       temp_sourceip = l[0].split(":")
       temp_destip = l[1].split(":")       
       set_value(temp_sourceip[0], temp_sourceip[1],temp_destip[0],temp_destip[1])