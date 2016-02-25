#!/bin/bash
# possible tw = 16 17 18 20

#SBATCH --time=24:00:00


for tw in 14 16 18 20
do
  export tw
  sbatch run_dummies.sbatch
  sleep 4h
done
