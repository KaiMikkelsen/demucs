import musdb
import museval
import os
import platform
import datetime


dataset_folder = "../data/MUSDB18"

estimates_directory = "/Users/kaimikkelsen/canada_compute/demucs/separated/htdemucs"
output_directory = '/Users/kaimikkelsen/canada_compute/demucs/results'

estimates_directory = "/home/kaim/projects/def-ichiro/kaim/demucs/separated/htdemucs"
output_directory = '/home/kaim/projects/def-ichiro/kaim/demucs/results/'

mus = musdb.DB(root=dataset_folder, subsets="test")

# evaluate an existing estimate folder with wav files
scores = museval.eval_mus_dir(
    dataset=mus,  # instance of musdb
    estimates_dir=estimates_directory,  # path to estimate folder
    output_dir=output_directory,  # set a folder to write eval json files
    ext='wav'
)

#args = parser.parse_args()
method = museval.EvalStore(frames_agg="median", tracks_agg="median")
method.add_eval_dir(output_directory)
print(method)

# Get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get machine name
machine_name = platform.node()

# Path for the output file
output_file = os.path.join(output_directory, 'results.txt')

# Open the file to write the result with additional information
with open(output_file, 'a') as f:
    f.write(f"Date and Time: {current_datetime}\n")
    f.write(f"Machine Name: {machine_name}\n\n")
    f.write("Method Evaluation Results:\n")
    f.write(str(method))

print(f"Method result saved to {output_file}")

