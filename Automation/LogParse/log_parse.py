import re
from collections import Counter
import os
import argparse
import csv


parser = argparse.ArgumentParser(description='IP Count Utility')
# Declare an argument (`--file`), saying that the 
# corresponding value should be stored in the `logfile` 
# field, and using a default value if the argument 
# isn't given
parser.add_argument('-file', help='Please pass the file name as argument' ,action="store", dest='file')
args = parser.parse_args()
logfile=args.file

# logfile='log.txt'
print(logfile)

reg_expr="\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"

def get_ip_list(logfile):
    with open(logfile) as f:
        output=f.read()
        ip_list = re.findall(reg_expr,output)
    # print(ip_list)
    return(ip_list)


def get_count(ip_list):
    ip_dict={}
    for ip in ip_list:
        if ip not in ip_dict:
            ip_dict[ip] = 1
        else:
            ip_dict[ip]+=1

    return ip_dict


def write_to_csv(ip_dict):
    with open('log.csv','w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(["IP Address", "Count"])
        for ip in ip_dict:
            csvwriter.writerow([ip,ip_dict[ip]])


ip_list = get_ip_list(logfile)
ip_dict ={}
ip_dict = get_count(ip_list)
write_to_csv(ip_dict)

    # print(f.read())
# count = Counter(ip_list)
# print(count)