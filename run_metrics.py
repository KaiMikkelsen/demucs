import musdb
import museval
import os
import platform
from datetime import datetime

dataset_path = "../data/MUSDB18"
#eval_dir = '/Users/kaimikkelsen/canada_compute/demucs/results'
eval_dir = '/home/kaim/projects/def-ichiro/kaim/demucs/results'
mus = musdb.DB(root=dataset_path)

# evaluate an existing estimate folder with wav files
scores = museval.eval_mus_dir(
    dataset=mus,  # instance of musdb
    estimates_dir="/separated/htdemucs",  # path to estimate folder
    output_dir='/results',  # set a folder to write eval json files
    ext='wav'
)

#args = parser.parse_args()
method = museval.EvalStore(frames_agg="median", tracks_agg="median")
method.add_eval_dir(eval_dir)
print(method)

output_file = os.path.join(eval_dir, 'results.txt')
# Get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get machine name
machine_name = platform.node()

with open(output_file, 'a') as f:
    f.write(f"Date and Time: {current_datetime}\n")
    f.write(f"Machine Name: {machine_name}\n\n")
    f.write("Method Evaluation Results:\n")
    f.write(str(method))

print(f"Method result saved to {output_file}")

