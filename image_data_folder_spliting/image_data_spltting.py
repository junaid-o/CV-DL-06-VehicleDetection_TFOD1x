#pip install split-folders tqdm


from Levenshtein import ratio
import spitfolders
#import split_folders
import os

# Split with a ratio
# To split into training and validatation set, set the tuple to ratio i.e (0.8, 0.2)

#splitfolders.ratio(dir_path, output="output", seed=1337, ratio= (0.8, 0.1, 0.1), group_prefix=None)
splitfolders.ratio("input", output="output", seed=1337, ratio= (0.8, 0.1, 0.1), group_prefix=None)


