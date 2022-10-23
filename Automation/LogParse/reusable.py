// This file is created to use the Class created in log_parse_class,py file

from log_parse_class import LogParse 

log_parse = LogParse('log.txt')
ip_list = log_parse.get_ip_list()
ip_dict = log_parse.get_count(ip_list)
log_parse.write_to_csv(ip_dict, 'test.csv')
