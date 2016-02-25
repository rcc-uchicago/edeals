#!/bin/bash

#SBATCH --output=RUN.OUT
#SBATCH --time=03:30:00

N=$((12420/$tw))

for x in $(seq 1 $N)
do
  sbatch dummy_job.sbatch
  sleep $tw
done


