#!/usr/bin/env python3

import sys
import csv
import operator
import re

#define the per_user and error as a dictionary
per_user = {}
error = {}
#define the files which needed
log_file = "syslog.log"
error_file = 'error_message.csv'
user_file = 'user_statistics.csv'

#regex
def regex(result):
    #Errors Type
    if result.group(2) not in error.keys():
      error[result.group(2)] = 0
    error[result.group(2)] += 1
    #Username
    if result.group(3) not in per_user.keys():
      per_user[result.group(3)] = {}
      per_user[result.group(3)]["INFO"] = 0
      per_user[result.group(3)]["ERROR"] = 0
    if result.group(1) == "INFO":
      per_user[result.group(3)]["INFO"] += 1
    elif result.group(1) == "ERROR":
      per_user[result.group(3)]["ERROR"] += 1

with open(log_file, 'r') as file:
  for log in file:
    pattern = r"ticky: ([\w]*) ([\w' ]*) [\[\d#\]]* ?\((.*)\)$"
    result = re.search(pattern, log)
    regex(result)

error = sorted(error.items(), key = operator.itemgetter(1), reverse = True)
per_user = sorted(per_user.items())

error.insert(0, ('Error', 'Count'))

with open(error_file, 'w') as file:
  for err in error:
    typ,count = err
    file.write(str(typ)+','+str(count)+'\n')

with open(user_file, 'w') as file:
  file.write("Username,INFO,ERROR\n")
  for user in per_user:
    typ,stat = user
    file.write(typ + ',' + str(stat['INFO']) + ',' + str(stat["ERROR"]) + '\n')