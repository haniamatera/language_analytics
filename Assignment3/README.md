# Assignment 3

## Description of the assignment

The main task in this assignment was to calculate and visualize the evolution of sentiment scores calculated from the dataset of over a million headlines taken from the Australian news source ABC within the time period of 19.02.2003 and 31.12.2020. The Python script that I have created in order to perform the assignment task: 
-	Calculates the sentiment score for every headline in the data using the spaCyTextBlob approach,
-	Creates and saves a plot of sentiment over time with a 1-week rolling average,
-	Creates and saves a plot of sentiment over time with a 1-month rolling average.


___Data___


Data can be found and downloaded from an online source Kaggle.com and can be accessed [here]:https://www.kaggle.com/therohk/million-headlines
rises a transcript from 100 most popular novels written in English. It can be viewed and downloaded from the 'data' folder. 

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
