# Assignment 2 

## Description of the assignment

The main task of this assignment is to create a Python Script set to calculate the word collocates of specific keywords extracted from a text corpus of 100-english novels containing transcripts of the most popular novels written in English. Ultimately, the script: 
- Takes a directory of text files, a keyword, and a window size (number of words) as input parameters, and an output file called out/{filename}.csv. All three parameters can be defined in the script itself;
-	Finds out how often each word collocates with the target across the corpus;
-	Calculates mutual information between the target word and all collocates across the corpus based on how often each word collocated with the keyword across the corpus;
- Saves the results as a single file consisting of three columns: collocate, raw_frequency, MI in the output folder. 


___Data___

Data used in the current study comprises a transcript from 100 most popular novels written in English. It can be viewed and downloaded from the 'data' folder. 

## The method
In order to solve the assignment, I have created a function that takes:
- a keyword (a word of user’s choice that creates a collocate pairs with all words across the corpus),
- a window size (the number of words that are taken into account when calculating the collocate),
- a file path (the directory of the text corpus data)
as input arguments which can be manipulated by the user.

First of all, the necessary text preprocessing had to be performed. This included tokenizing the words, making them uppercase and counting their raw frequency of appearance across the entire corpus. Subsequently, the O11 score signifying the co-occurrence of the given word and the keyword, the R1 score signifying the keyword’s general appearance in the text corpus, the O12 score signifying the frequency of the keyword appearance without the collocate word, the C1 signifying the frequency of the collocate word’s general appearance across the corpus, and finally the O21 signifying the frequency of collocate word’s appearance without the keyword, were calculated. This operation has enabled the calculation of MI score, which is a is a measure of collocational strength between the words.


## Results and evaluation
Data frame with the collocate word, its raw frequency and the MI score can be accessed in the output folder in the GitHub repository. 

## Repository structure and files
This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```out``` | Contains the outputs with a .csv file containing information about the collocate words of a specific keyword.
```collocation.py```| The script to be executed from the terminal.
```create_visual_venv.sh``` | A bash script which automatically generates a new virtual environment 'collocation_env', and install all the packages contained within 'requirements.txt'
```requirements.txt``` | A list of packages along with the versions that are required.
```README.md``` | This readme file.
```data```| A folder with .txt files with transcripts of the English novels


## Usage (reproducing the results)

### Virtual environment
In order to run the script, one is required to set up the virtual environment with all necessary packages installed. Please clone the repo, navigate to the folder for this assignment, run the bash script to set up the environment, and lastly activate it. The following code should be executed from the terminal:

```bash
git clone https://github.com/haniamatera/language_analytics.git
cd Assignment2
bash ./create_visual_venv.sh
source ./collocation_env/bin/activate
```

### Execute the script 
Now, the script can be executed:

```bash
python collocation.py  

```
