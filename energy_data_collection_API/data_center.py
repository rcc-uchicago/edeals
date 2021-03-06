# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:10:11 2015

@author: wmcfadden
"""
import csv
import sys
import get_slurm as gs
import save_gang_big as sg
import pandas as pd
import glob

def usage():
    print """Usage: python data_center.py start-time end-time
where
* start-time and end-time are time strings in the format returned by sacct, ie 2015-05-12T10:43:20
"""


def data_concat():
    path ='../data/data_big/gang_data/' # use your path
    allFiles = glob.glob(path + "/*.csv")
    list_ = []
    for file_ in allFiles:
        try:
            df = pd.read_csv(file_,index_col=0)
            list_.append(df)
        except:
            pass
    return pd.concat(list_,axis=1)
    
def conv_str(a):
    sp_str = a.split('T')
    sp0_str = sp_str[0].split('-')
    sp1_str = sp_str[1].split(':')
    return sp0_str[1]+'-'+sp0_str[2]+'-'+sp0_str[0]+'+'+sp1_str[0]+':'+sp1_str[1]
    
def main():
    if(len(sys.argv)==3):
        all_jobs = gs.get_sacct_jobs_bytime(*sys.argv[1:])
        print "got all jobs"
        save_slurm = []
        for job in all_jobs:
            slurm = gs.get_sacct_data(job,format='node,'+gs.allfmt+',jobid')
            print 'finished job '+job
            if(len(slurm)>2):
                save_slurm.append(slurm)
        with open("../data/data_big/slurm_data.csv", "w") as csv_file:
            a = csv.writer(csv_file, delimiter=',')
            a.writerows(save_slurm)
        print "saved slurm data"
#        sg.save_data(conv_str(sys.argv[1]),conv_str(sys.argv[2]))
#        sg.concat_data()
#        print "saved ganglia data"
    else:
        print usage()

if __name__ == "__main__":
    main()
