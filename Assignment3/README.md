# Assignment 3

## Description of the assignment

The main task in this assignment was to calculate and visualize the evolution of sentiment scores calculated from the dataset of over a million headlines taken from the Australian news source ABC within the time period of 19.02.2003 and 31.12.2020. The Python script that I have created in order to perform the assignment task: 
-	Calculates the sentiment score for every headline in the data using the spaCyTextBlob approach,
-	Creates and saves a plot of sentiment over time with a 1-week rolling average,
-	Creates and saves a plot of sentiment over time with a 1-month rolling average.


___Data___

Data can be found and downloaded from an online source Kaggle.com under the following [link](https://www.kaggle.com/therohk/million-headlines). The complete .csv file can be also accessed in the 'data' folder in th ecurrent GitHub repository.

## The method
Before calculating the sentiment scores across time, the date format of news headlines had to be changed into a dash-separated format. That has been done by constructing a loop which iterates over all articles and changes the dates. Subsequently, the data was fed into another loop that ran over each of the headlines and calculated the sentiment polarity score using nlp pipeline. In this assignment, I employed spacy's pipeline ```en_core_web_sm```. After completing all the preprocessing steps, I have made three different visualizations displaying the polarity score evolution over time, with the mean rolling average of one week, one month and one year.   


## Results and evaluation
The three plots show how the mean sentiment score calculated on the bases of the Australian ABC news headlines changes over time (2003-2020). In each of the plots the mean score of the headlines (which can span from -1 to 1) is plotted on the -axis against time. The plots with the results can be viewed in the 'visuals' folder.


## Repository structure and files
This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```visuals``` | Contains the visual output with graphs showing the evolution of mean sentiment score across different time intervals.
```sentiment.py```| The script to be executed from the terminal.
```create_visual_venv.sh``` | A bash script which automatically generates a new virtual environment 'sentiment_env', and install all the packages contained within 'requirements.txt'
```requirements.txt``` | A list of packages along with the versions that are required.
```README.md``` | This readme file.
```data```| A folder with a .csv file containing news headlines 


## Usage (reproducing the results)

### Virtual environment
In order to run the script, one is required to set up the virtual environment with all necessary packages installed. Please clone the repo, navigate to the folder for this assignment, run the bash script to set up the environment, and lastly activate it. The following code should be executed from the terminal:

```bash
git clone https://github.com/haniamatera/language_analytics.git
cd Assignment3
bash ./create_visual_venv.sh
source ./sentiment_env/bin/activate
```

### Execute the script 
Now, the script can be executed:

```bash
python sentiment.py  

```
