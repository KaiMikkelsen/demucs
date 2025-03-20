git pull

module load python/3.10 cuda/12.2 cudnn/8.9.5.29
export XLA_FLAGS=--xla_gpu_cuda_data_dir=$CUDA_HOME

source demucs_env/bin/activate

module load soundtouch/2.3.3

dora run -d model=htdemucs

