# Assignment 7  

## Description of the assignment

Using the text corpus called 100-english-novels which contains transcripts of 100 most popular English novels, this assignment’s task was to create a Python script which would do the following:
  - Calculate the total word count for each novel
  - Calculate the total number of unique words for each novel
  - Save result as a single file consisting of three columns: filename, total_words, unique_words


___Data___

Data used in the current study comprises a transcript from 100 most popular novels written in English. It can be viewed and downloaded from the 'data' folder. 

## The method
In order to perform the assignment task, I have created a Python script with a loop that splits the text corpus on whitespaces, thus producing the count of individual words and counts unique words in the corpus using numpy package. Both, total word count and the total number of unique words for each novel are then pasted into distinct columns in a data frame using pandas and saved as a .csv file.



## Results and evaluation
The detailed results (saved as word_count_df.csv) can be viewed and downloaded from the ‘out’ folder in GitHub repository under the link specified below. ![image](https://user-images.githubusercontent.com/54862257/119623116-27b32600-be08-11eb-8652-46b048c795f9.png)


## Repository structure and files
This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```out``` | Contains the outputs with a .csv file containing information extracted from the text corpus.
```word_count.py```| The script to be executed from the terminal.
```create_visual_venv.sh``` | A bash script which automatically generates a new virtual environment 'network_env', and install all the packages contained within 'requirements.txt'
```requirements.txt``` | A list of packages along with the versions that are required.
```README.md``` | This readme file.
```data```| A folder with .txt files with transcripts of the English novels


## Usage (reproducing the results)

### Virtual environment
In order to run the script, one is required to set up the virtual environment with all necessary packages installed. Please clone the repo, navigate to the folder for this assignment, run the bash script to set up the environment, and lastly activate it. The following code should be executed from the terminal:

```bash
git clone https://github.com/haniamatera/language_analytics.git
cd Assignment1
bash ./create_visual_venv.sh
source ./network_env/bin/activate
```

### Execute the script 
Now, the script can be executed:

```bash
python word_count.py  

```
