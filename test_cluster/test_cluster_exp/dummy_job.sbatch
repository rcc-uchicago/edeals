#!/bin/bash

#SBATCH --part=westmere
#SBATCH --reservation=energy
#SBATCH --ntasks=3

#SBATCH --output=JOB.OUT
#SBATCH --time=00:5:00

module load lammps

mpirun -np 3 lmp_intelmpi -in in.lj
