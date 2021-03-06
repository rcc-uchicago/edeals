from subprocess import Popen, PIPE
import sys

allfmt="Start,End,TotalCPU,UserCPU,SystemCPU,ReqCPUS,AllocCPUS,NCPUS,ReqCPUFreq,AveCPUFreq,AveDiskRead,AveDiskWrite,AvePages,AveRSS,AveVMSize,MaxDiskRead,MaxDiskWrite,MaxPages,MaxRSS,MaxVMSize,Reserved"

def get_sacct_data(jobid, format=allfmt):
    cmd=["sacct", "--format", format, "-j", jobid, "-nP"] # -n : no header, -p : pipe-separated output
#    cmd=["sacct", "--format", format, "-j", jobid+".batch", "-nP"] # -n : no header, -p : pipe-separated output
    process = Popen(cmd, stdout=PIPE)
    out, err = process.communicate()
    return out.strip().split('\n')[0].split('|')
   
def get_sacct_jobs_bytime(strt_t, stp_t):
    cmd=["sacct", "--format", "JobID", "--user", "wmcfadden", "-P", "--allocations", "-T", "--state", "running", "--starttime", strt_t, "--endtime", stp_t] # -n : no header, -p : pipe-separated output
    process = Popen(cmd, stdout=PIPE)
    out, err = process.communicate()
    return out.strip().split('\n')[1:]
    
def get_scontrol_stats(jobid):
    cmd=["scontrol", "show", "job", jobid] # -n : no header, -p : pipe-separated output
    process = Popen(cmd, stdout=PIPE)
    out, err = process.communicate()
    return [s.split("=") for s in out.split()]

def main():
    data = get_sacct_data(sys.argv[1])
    print ','.join(data)
    
if __name__ == "__main__":
    main()
