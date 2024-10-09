#!/bin/bash
#SBATCH --gres=gpu:1       # Request GPU "generic resources"
#SBATCH --cpus-per-task=6  # Refer to cluster's documentation for the right CPU/GPU ratio
#SBATCH --mem=32000M       # Memory proportional to GPUs: 32000 Cedar, 47000 Béluga, 64000 Graham.

source ../ENV/bin/activate

demucs run_separation_demucs.sh

# ls -d $SLURM_TMPDIR

# cp  -r $SLURM_TMPDIR/* /project/def-ichiro/kaim/demucs/job_outputs/

# echo 'hello'
