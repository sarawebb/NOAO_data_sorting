#!/bin/sh
#SBATCH -N 1      # nodes requested
#SBATCH --mem=10  # memory in Mb

#SBATCH --output=Err_funpack_all.out
#SBATCH --error=Err_funpack_all.err

#SBATCH --partition=skylake
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=8G

module load funpack 

python funpack_all_fits.py 
