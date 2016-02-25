# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:46:49 2015

@author: wmcfadden
"""

import sys, glob, requests, os
from requests.auth import HTTPBasicAuth
import pandas as pd

with open ("/home/wmcfadden/.ganglia", "r") as myfile:
    data=myfile.readlines()

user = data[0].rstrip()
pwd = data[1].rstrip()
autho = HTTPBasicAuth(user, pwd)

def usage():
    print """Usage: python save_ganglia_big.py start-time end-time
where
* start-time and end-time are time strings in the format, 05-12-2015T01:30
"""



def save_data(t_st,t_en):
    path ='../data/data_big/gang_data/' # use your path
    filelist = glob.glob(path + "/*.csv")
    for f in filelist:
        os.remove(f)
    t_start = t_st.replace('-','%2F').replace(':','%3A').replace('T','+')
    t_end = t_en.replace('-','%2F').replace(':','%3A').replace('T','+')
    ext = ['-']
    ext.extend(range(8))
    #metric = 'cpu_user|cpu_system|cpu_idle'  #substring matching any metric separate with | to use multiple (regex)
    metric = 'ambient_temp|avg_power'
    for i in ext:
        host = 'midway'+str(i)  #substring matching any host
        # add '&r=hour' if you want it hourly
        url = 'https://midway-mgt.rcc.uchicago.edu/ganglia/graph.php?cs='+t_start+'&ce='+t_end+'&hreg[]='+host+'&mreg[]='+metric+'&aggregate=1&csv=1'
        r = requests.get(url, auth=autho, verify=False)
        
        with open(path+metric+"_"+host+".csv", "w") as csv_file:
            csv_file.write(r.text)
    
#    metric = 'cpu_avg_power|ac_avg_power|mem_avg_power'
#    for i in ext:
#        host = 'midway'+str(i)  #substring matching any host
#        # add '&r=hour' if you want it hourly
#        url = 'https://midway-mgt.rcc.uchicago.edu/ganglia/graph.php?cs='+t_start+'&ce='+t_end+'&hreg[]='+host+'&mreg[]='+metric+'&aggregate=1&csv=1'
#        r = requests.get(url, auth=autho, verify=False)
#        
#        with open(path+metric+"_"+host+".csv", "w") as csv_file:
#            csv_file.write(r.text)
    
    metric = 'system_level|domain_a_avgpwr|domain_b_avgpwr'
    for i in ext:
        host = 'midway'+str(i)  #substring matching any host
        # add '&r=hour' if you want it hourly
        url = 'https://midway-mgt.rcc.uchicago.edu/ganglia/graph.php?cs='+t_start+'&ce='+t_end+'&hreg[]='+host+'&mreg[]='+metric+'&aggregate=1&csv=1'
        r = requests.get(url, auth=autho, verify=False)
        
        with open(path+metric+"_"+host+".csv", "w") as csv_file:
            csv_file.write(r.text)
    
    metric = 'pwr_consumption|chassis_fan_pwr'
    for i in ext:
        host = 'midway'+str(i)  #substring matching any host
        # add '&r=hour' if you want it hourly
        url = 'https://midway-mgt.rcc.uchicago.edu/ganglia/graph.php?cs='+t_start+'&ce='+t_end+'&hreg[]='+host+'&mreg[]='+metric+'&aggregate=1&csv=1'
        r = requests.get(url, auth=autho, verify=False)
        
        with open(path+metric+"_"+host+".csv", "w") as csv_file:
            csv_file.write(r.text)
    
        
    metric = 'proc_run|cpu_user|cpu_system'
    for i in ext:
        host = 'midway'+str(i)  #substring matching any host
        # add '&r=hour' if you want it hourly
        url = 'https://midway-mgt.rcc.uchicago.edu/ganglia/graph.php?cs='+t_start+'&ce='+t_end+'&hreg[]='+host+'&mreg[]='+metric+'&aggregate=1&csv=1'
        r = requests.get(url, auth=autho, verify=False)
        
        with open(path+metric+"_"+host+".csv", "w") as csv_file:
            csv_file.write(r.text)
            
    metric = 'bytes_in|bytes_out|pkts_in|pkts_out'
    for i in ext:
        host = 'midway'+str(i)  #substring matching any host
        # add '&r=hour' if you want it hourly
        url = 'https://midway-mgt.rcc.uchicago.edu/ganglia/graph.php?cs='+t_start+'&ce='+t_end+'&hreg[]='+host+'&mreg[]='+metric+'&aggregate=1&csv=1'
        r = requests.get(url, auth=autho, verify=False)
        
        with open(path+metric+"_"+host+".csv", "w") as csv_file:
            csv_file.write(r.text)
            
    metric = 'hdd_inlet_temp|mezz_card_temp|pib_ambient_temp'
    for i in ext:
        host = 'midway'+str(i)  #substring matching any host
        # add '&r=hour' if you want it hourly
        url = 'https://midway-mgt.rcc.uchicago.edu/ganglia/graph.php?cs='+t_start+'&ce='+t_end+'&hreg[]='+host+'&mreg[]='+metric+'&aggregate=1&csv=1'
        r = requests.get(url, auth=autho, verify=False)
        
        with open(path+metric+"_"+host+".csv", "w") as csv_file:
            csv_file.write(r.text)
            
    metric = 'swap_free|swap_total' 
    for i in ext:
        host = 'midway'+str(i)  #substring matching any host
        # add '&r=hour' if you want it hourly
        url = 'https://midway-mgt.rcc.uchicago.edu/ganglia/graph.php?cs='+t_start+'&ce='+t_end+'&hreg[]='+host+'&mreg[]='+metric+'&aggregate=1&csv=1'
        r = requests.get(url, auth=autho, verify=False)
        
        with open(path+metric+"_"+host+".csv", "w") as csv_file:
            csv_file.write(r.text)

def save_proc_run(t_st,t_en):
    path ='../data/data_big/gang_data/' # use your path
    filelist = glob.glob(path + "/*.csv")
    for f in filelist:
        os.remove(f)
    t_start = t_st.replace('-','%2F').replace(':','%3A').replace('T','+')
    t_end = t_en.replace('-','%2F').replace(':','%3A').replace('T','+')
    ext = ['-']
    ext.extend(range(8))
    #metric = 'cpu_user|cpu_system|cpu_idle'  #substring matching any metric separate with | to use multiple (regex)
    metric = 'proc_run'
    for i in ext:
        host = 'midway'+str(i)  #substring matching any host
        # add '&r=hour' if you want it hourly
        url = 'https://midway-mgt.rcc.uchicago.edu/ganglia/graph.php?cs='+t_start+'&ce='+t_end+'&hreg[]='+host+'&mreg[]='+metric+'&aggregate=1&csv=1'
        r = requests.get(url, auth=autho, verify=False)
        
        with open(path+metric+"_"+host+".csv", "w") as csv_file:
            csv_file.write(r.text)
    


def concat_data():            
    path ='../data/data_big/gang_data/' # use your path
    allFiles = glob.glob(path + "/*.csv")
    frame = pd.DataFrame()
    list_ = []
    for file_ in allFiles:
        try:
            df = pd.read_csv(file_,index_col=0)
            list_.append(df)
        except:
            pass
    frame = pd.concat(list_,axis=1)    
    frame.to_csv('../data/data_big/gang_data.csv', sep=',')

def main():
    if len(sys.argv) == 3:
        save_data(*sys.argv[1:])
    else:
        usage()

if __name__ == "__main__":
    main()