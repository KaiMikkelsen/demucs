import musdb
import museval

# # initiate musdb
# mus = musdb.DB(root="/Users/kaimikkelsen/canada_compute/data/MUSDB18-7")

# # evaluate an existing estimate folder with wav files
# scores = museval.eval_mus_dir(
#     dataset=mus,  # instance of musdb
#     estimates_dir="/Users/kaimikkelsen/canada_compute/demucs/separated/htdemucs",  # path to estimate folder
#     output_dir='/Users/kaimikkelsen/canada_compute/demucs/results',  # set a folder to write eval json files
#     ext='wav'
# )

# #args = parser.parse_args()
# method = museval.EvalStore(frames_agg="median", tracks_agg="median")
# method.add_eval_dir("/Users/kaimikkelsen/canada_compute/demucs/results")
# print(method)

# initiate musdb
mus = musdb.DB(root="../data/MUSDB18")

# evaluate an existing estimate folder with wav files
scores = museval.eval_mus_dir(
    dataset=mus,  # instance of musdb
    estimates_dir="/separated/htdemucs",  # path to estimate folder
    output_dir='/results',  # set a folder to write eval json files
    ext='wav'
)

#args = parser.parse_args()
method = museval.EvalStore(frames_agg="median", tracks_agg="median")
method.add_eval_dir('/home/kaim/projects/def-ichiro/kaim/demucs/results')
print(method)

