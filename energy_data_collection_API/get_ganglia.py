# -*- coding: utf-8 -*-
"""
 Adapted from wmcfadden's load_ganglia.py
 Usage: get_ganglia.py host start-time end-time
 start-time and end-time are in the format produced by sacct, ie 2015-05-12T10:43:20
 @author: sdjacobs
"""

import requests
from requests.auth import HTTPBasicAuth
from time import strptime, strftime
from get_slurm import get_sacct_data
import sys

import pandas as pd


def usage():
    print """Usage: python get_ganglia.py host start-time end-time
where
* host is a node on midway, ie midway252
* start-time and end-time are time strings in the format returned by sacct, ie 2015-05-12T10:43:20
OR
python -j <jobnum>
where jobnum is a slurm job number."""


# Change this line to get different metrics.
metric = 'ambient_temp|avg_power|bytes_in|bytes_out|cpu_user|hdd_inlet_temp|mem_free|mezz_card_temp|pib_ambient_temp|pkts_in|pkts_out|proc_run|swap_free|swap_total'

with open ("/home/wmcfadden/.ganglia", "r") as myfile:
    data=myfile.readlines()

user = data[0].rstrip()
pwd = data[1].rstrip()
autho = HTTPBasicAuth(user, pwd)

slurm_fmt = '%Y-%m-%dT%H:%M:%S'
ganglia_fmt = "%m/%d/%Y+%H:%M"

def time_convert(s):
    t = strptime(s, slurm_fmt)
    return strftime(ganglia_fmt, t)

def get_ganglia_data(host, start, end):
    t_start = time_convert(start)
    t_end = time_convert(end)
    url = 'https://midway-mgt.rcc.uchicago.edu/ganglia/graph.php?cs='+t_start+'&ce='+t_end+'&hreg[]='+host+'&mreg[]='+metric+'&aggregate=1&csv=1'
    r = requests.get(url, auth=autho, verify=False)
    return r.text
   
def format_ganglia_data(text):
    file_ ="_tmp.csv" 
    with open(file_, "w") as csv_file:
        csv_file.write(text)
        
    df = pd.read_csv(file_,index_col=0)
    mn = df.mean(axis=0)
    mn.index = [s.split()[1] for s in mn.index]
    toprint = ''
    toprint = toprint + str(mn['ambient_temp']) + ','
    toprint = toprint + str(mn['ac_avg_power']) + ','
    toprint = toprint + str(mn['mem_avg_power']) + ','
    toprint = toprint + str(mn['cpu_avg_power']) + ','
    toprint = toprint + str(mn['bytes_in']) + ','
    toprint = toprint + str(mn['bytes_out']) + ','
    toprint = toprint + str(mn['cpu_user']) + ','
    toprint = toprint + str(mn['mem_free']) + ','
    toprint = toprint + str(mn['pkts_in']) + ','
    toprint = toprint + str(mn['pkts_out']) + ','
    toprint = toprint + str(mn['proc_run']) + ','
    toprint = toprint + str(mn['swap_free']) + ','
    toprint = toprint + str(mn['swap_total']) 
    
    return toprint

def main():
    if len(sys.argv) == 4:
        print get_ganglia_data(*sys.argv[1:])
    elif len(sys.argv)==3 and sys.argv[1] == "-j":
        data = get_sacct_data(sys.argv[2], format="node,start,end")
        text = get_ganglia_data(*data)
        print format_ganglia_data(text)
    else:
        usage()

if __name__ == "__main__":
    main()

 

