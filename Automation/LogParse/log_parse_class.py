import re
from collections import Counter
import os
import argparse
import csv


# parser = argparse.ArgumentParser(description='IP Count Utility')
# # Declare an argument (`--file`), saying that the 
# # corresponding value should be stored in the `logfile` 
# # field, and using a default value if the argument 
# # isn't given
# parser.add_argument('-file', help='Please pass the file name as argument' ,action="store", dest='file')
# args = parser.parse_args()
# logfile=args.file


class LogParse:
    def __init__(self, logfile):
        self.logfile = logfile
        self.reg_expr="\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
        print(self.logfile)
    
    def get_ip_list(self):
        print(self.logfile)
        with open(self.logfile) as f:
            output=f.read()
            ip_list = re.findall(self.reg_expr,output)
        # print(ip_list)
        return(ip_list)

    def get_count(self,ip_list):
        ip_dict={}
        for ip in ip_list:
            if ip not in ip_dict:
                ip_dict[ip] = 1
            else:
                ip_dict[ip]+=1
        return ip_dict

    def write_to_csv(self,ip_dict, csvfile):
        with open(csvfile,'w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(["IP Address", "Count"])
            for ip in ip_dict:
                csvwriter.writerow([ip,ip_dict[ip]])
    
# logfile='log.txt'
# print(logfile)

log_parse = LogParse('log.txt')
ip_list = log_parse.get_ip_list()
ip_dict = log_parse.get_count(ip_list)
log_parse.write_to_csv(ip_dict, 'sample.csv')


    # print(f.read())
# count = Counter(ip_list)
# print(count)