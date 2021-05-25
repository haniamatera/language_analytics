#!/usr/bin/env python
# coding: utf-8

# # #____Assignment 3___###
# __Dictionary-based sentiment analysis with Python__

 
# Data downloaded the following CSV file from Kaggle:
# https://www.kaggle.com/therohk/million-headlines



#importing the necessary packages 
import os 
import spacy
import matplotlib.pyplot as plt
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob

#assigning shorcuts to specific functions
nlp=spacy.load("en_core_web_sm")
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)



#reading a data file and saving it in a data frame with pandas
in_file = os.path.join ("data","abcnews-date-text.csv")
data= pd.read_csv(in_file)


#subsetting the data 
sample = data.sample(10000)


#changing the date format to yyyy-mm-dd (timestamp):
#creating an empty list of dates where the changed date formats are gonna be pasted as a list
all_dates=[]

#looping over each row and changing the date format (to dash-separated)
for index, row in sample.iterrows():
    
    
    date = str(row['publish_date'])

    time_df = pd.DataFrame({'year': [int(date[0:4])],
                   'month': [int(date[4:6])],
                   'day': [int(date[6:8])]})
    time_df = pd.to_datetime(time_df)
    
    #appending the changed dates to all_dates list 
    all_dates.append(time_df[0])
    
#overwriting the column "publish_date" with a new one all_dates 
sample["publish_date"]= all_dates 


#an empty list: output 
output=[]

#looping over the headlines and calculating the sentiment plarity per headline
for doc in nlp.pipe(sample["headline_text"]):
    output.append(doc._.sentiment.polarity)


# putting the computed scores into a previously created list (output)
sample["scores"]=output


#plotting the sentiment scores over time with a 1-week rolling average
plt.plot(sample.groupby("publish_date").mean("sentiment_score").rolling(7).mean())

#add title 
plt.title("Sentiment over time with a mean rolling average of one week")

#add xlabel 
plt.xlabel("Time")

#add ylabel 
plt.ylabel("Sentiment score")

#saving the plot
plt.savefig("visuals/mean_sent_1w_roll_avg.png")


# plotting sentiment over time with a 1-month rolling average
plt.plot(sample.groupby("publish_date").mean("sentiment_score").rolling(30).mean())

#add title 
plt.title("Sentiment over time with a mean rolling average of one month")

#add xlabel 
plt.xlabel("Time")

#add ylabel 
plt.ylabel("Sentiment score")

#saving the plot
plt.savefig("visuals/mean_sent_1m_roll_avg.png")


#extra: plottig sentiment over a period of one year 
plt.plot(sample.groupby("publish_date").mean("sentiment_score").rolling(365).mean())

#add title 
plt.title("Mean sentiment over time with a mean rolling average of one year")

#add xlabel 
plt.xlabel("Time")

#add ylabel 
plt.ylabel("Sentiment score")

#saving the plot
plt.savefig("visuals/mean_sent_1y_roll_avg.png")


# __Summary__
# 
# 1) Plots description 
# 
# 2) What (if any) are the general trends?
# 
# 3) What (if any) inferences might you draw from them?
# 
# 
# 
# 1. The three plots show how the mean sentiment score calculated on the bases of the Australian ABC news headlines changes over time (2003-2020). In each of the plots the mean score of the headlines (which can span from -1 to 1) is plotted on the -axis against time. The mean score is calculated differently for each of the plots and is as follows:
# 
# - plot 1: 1-week rolling average: the mean sentiment score is calculated from all headlines of the ABC news over he course of one week (7 days)
# 
# - plot 2: 1-month rolling average: the mean sentiment score is calculated from all headlines of the ABC news over he course of one month (30 days) 
# 
# - plot 1: 1-year rolling average: the mean sentiment score is calculated from all headlines of the ABC news over he course of one year.
# 
# 
# 2. General trends
# 
# 
# - plot 1: it is difficult to interpret this plot as there plenty o data points plotted on the same figure. It is apparent that the fluctuations between negative and positive scores are large without any evident trends. The only visible thrend is unusually large negative spike around one week in 2016, followed by a large positive spike in 2017. 
# 
# - plot 2: Similarly, it is difficult to observe any apparent trend in the plot with a rolling average of one month. However, here we can see a couple of unusually large positive spikes in 2014, 2015 and 2017 and a negative spike in 2017 (which is an opposite phenomenon than what we have seen in the plot 1 and what might sugget that the cancelling effect implied by very variant sentiment in the days os this one particular week in 2017)
# 
# - plot 3: When we plot the sentiment with a rolling mean of 1 year we can see a general trend that periods of positive average sentiment score are followed by periods of time when the mean sentiment score is predominantly negative. We can also see that the most positive spike occured around years 2014-2017 and negative spikes occured around years 2008-2010 and 2016-2017.
# 
# 
# 3. General inferrences 
# 
# - sentiment is very variant
# - periods of predominantly negative sentiment scores are followed by periods of predominantly positive sentiment 
# - there seems to be quite extreme trends (either very positive or very negative) around years 2014 - 2017. 
# 



