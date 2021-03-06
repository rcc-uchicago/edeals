# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:27:02 2015

@author: wmcfadden
"""

from get_slurm import get_sacct_data
from get_ganglia import get_ganglia_data
from get_ganglia import format_ganglia_data
import sys



def main():
    data = get_sacct_data(sys.argv[1], format="node,start,end")
    gang = get_ganglia_data(*data)
    slurm = get_sacct_data(sys.argv[1])
    print "=SPLIT(\"" +str(data[0])+','+sys.argv[1] +','+ ','.join(slurm) +','+ (gang) + "\",\",\")"

if __name__ == "__main__":
    main()
