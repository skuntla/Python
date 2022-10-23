from log_parse_class import LogParse 

log_parse = LogParse('log.txt')
ip_list = log_parse.get_ip_list()
ip_dict = log_parse.get_count(ip_list)
log_parse.write_to_csv(ip_dict, 'test.csv')
