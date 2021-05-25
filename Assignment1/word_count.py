###___Assignment1###___
###___word_count___###


#installing neccessary packages 
import os
from pathlib import Path
import pandas as pd
import numpy as np


#defining data path 
data_path = os.path.join("data","100_english_novels")

# Count the length of the path to isolate filename in the loop
path_len = len(data_path)



# Defining a function that reads the files from the folder, calculates the wordcount and number of unique words.Lastly it appends the results to a data frame and saves it as a data frame

# making an empty dataframe using pandas
word_count_df = pd.DataFrame(columns = ['filename', 'total_words', 'unique_words'])

# for loop to split and count words
for filename in Path(data_path).glob("*.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        loaded_text = file.read()
        # split on whitespaces
        split_text = loaded_text.split()
        # save word count
        total_words = len(split_text)
        # count unique words with numpy
        values, unique = np.unique(split_text, return_counts=True)
        unique_words = len(unique)
        # saving the filename, total_words and unique_words in a temporary dataframe (this will be overwritten by new iteration)
        temp_df = ({'filename': filename, 'total_words': total_words, 'unique_words': unique_words})
        # appending the temporary dataframe to the empty dataframe
        word_count_df = word_count_df.append(temp_df, ignore_index=True)


#saving the results

# defining the path for results
path2results = os.path.join("out","word_count_df.csv")
# saving the dataframe as csv file
word_count_df.to_csv(path2results)


