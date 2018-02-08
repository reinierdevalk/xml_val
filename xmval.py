#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Validates a batch of XML files.
    
Mandatory argument:
arg_schema_path -- the path to the XML schema to validate against
    
Optional arguments:
arg_folder_path -- the path to the folder ('' yields the current path)
arg_subfolder -- a subfolder constraint: only subpaths containing this subfolder are checked ('' yields no subfolder)
"""

import sys
import os
import subprocess
from sys import argv

script, arg_schema_path, arg_folder_path, arg_subfolder = argv

print('... validation in progress ...')

# args
schema_path = arg_schema_path
folder_path = None
if arg_folder_path != '':
    folder_path = arg_folder_path
subfolder = None
if arg_subfolder != '':
    subfolder = arg_subfolder

# paths
if schema_path.startswith('~'):
    schema_path = os.path.expanduser(schema_path)
# print('schema_path = ' + schema_path)
    
path = ''
if folder_path == None:
    path = os.getcwd()
else:
    if folder_path.startswith('~'):
        folder_path = os.path.expanduser(folder_path)
    path = folder_path
# print('path = ' + path)
    
# make bash command
bash_cmd = 'cd ' + path + ' && '
mid = ''
if subfolder != None:
    mid = 'grep ' + subfolder + ' | '
    
bash_cmd += 'find ./* -type f -name "*.xml" | ' + mid + 'xargs xmllint --noout --schema ' + schema_path
#print('bash_cmd = ' + bash_cmd)
    
# get shell output
enc = sys.getdefaultencoding() # this is utf-8
proc = subprocess.Popen(bash_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
(res, err) = proc.communicate()
output = res.decode(enc) # see http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
# get number of files checked
bash_cmd = bash_cmd[:bash_cmd.index('xmllint')] + '| wc -w'
proc = subprocess.Popen(bash_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
(res, err) = proc.communicate()
num_files = res.decode(enc).strip()

# write the results into a file saved in the current path or, if a path is specified, the specified path
with open(path + '/xmlval-report.txt', 'w') as f:
    s =  'XML schema   : ' + schema_path + '\r\n'
    s += 'folder       : ' + path + '\r\n'
    sf = ''
    if (subfolder != None):
        sf = subfolder
    s += 'subfolder    : ' + sf + '\r\n'
    val = output.count('validates')
    inval = output.count('fails to validate')
    total = num_files
    s += 'XML files    : ' + str(total) + '\r\n'
    s += '  valid      : ' + str(val) + '\r\n'
    s += '  invalid    : ' + str(inval) + '\r\n\r\n\r\n'
    s += output
    f.write(s)

print(num_files + ' files successfully validated')
print('validation report written to ' + path)

#print(output)
