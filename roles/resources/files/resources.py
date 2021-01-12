#!/usr/bin/env python3
import os  
import pandas as pd 
from datetime import datetime

# csv generate function
def generatecsv(data,filename):
    newfile = pd.DataFrame(data, index=[0])
    if not os.path.isfile('/opt/%s.csv'% filename):
       newfile.to_csv (r'/opt/%s.csv'% filename, encoding='utf-8', sep = ",", index = None, header=True)
    else:
       newfile.to_csv (r'/opt/%s.csv'% filename, encoding='utf-8', sep = ",", mode='a', index = None, header=False)

# cpu utlization
def cpuutlization(): 
    with open("/proc/stat", "r")  as f:
        state = f.readlines()
    cpuAll = state[0].split()
    cpuactive = float(cpuAll[1])+float(cpuAll[2])+float(cpuAll[3])+float(cpuAll[7])+float(cpuAll[8])
    cputotal = float(cpuAll[1])+float(cpuAll[2])+float(cpuAll[3])+float(cpuAll[4])+float(cpuAll[5])+float(cpuAll[7])+float(cpuAll[8])
    cpu = {}
    cpu["Timestamp"] = datetime.now()
    cpu["CPU Utlization"] = str(round(((cpuactive / cputotal)*100),2)) + "%"
    return cpu


#memory free precentage
def memoryfree():
    with open("/proc/meminfo", "r") as f:
        lines = f.readlines()
    totalmem = [float(s) for s in ''.join(lines[0]).split() if s.isdigit() ]
    freemem = [float(s) for s in ''.join(lines[1]).split() if s.isdigit() ]
    memory = {}
    memory["Timestamp"] = datetime.now()
    memory["Free Memory percentage"] = str(round((float(freemem[0])/float(totalmem[0]))*100,2)) + "%"
    return memory

#disk free precentage    
def diskfree():
    rootSpace = os.popen("df -h | grep  '/$'").readlines()
    disk = {}
    disk["Timestamp"] = datetime.now()
    disk["Free Disk percentage"] = str (100 - int(''.join(rootSpace).split()[4].strip("%"))) + "%"
    return disk

def main():
    cpu = cpuutlization()
    memory = memoryfree()
    disk = diskfree()
    generatecsv(cpu,"CPU")
    generatecsv(memory,"MEM")
    generatecsv(disk,"DISK")
    
if __name__ == "__main__":
    main()
