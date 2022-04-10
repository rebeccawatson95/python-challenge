#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import csv
import numpy as np
import pandas as pd
#open and read csv
election_csv = "C:/Users/rebec/Desktop/UCI/Week 3/election_hwdata.csv"
#count = 0
#with open (election_csv, encoding='utf') as csvfile:
    #read the header row first and skip
    #csv_reader=csv.reader(csvfile,delimiter=',')
    #next(csv_reader,None)
    #for row in csv_reader:
        #count +=1
        
#print (count)
election_df=pd.read_csv("C:/Users/rebec/Desktop/UCI/Week 3/election_hwdata.csv")


# In[5]:


#the total number of votes cast
#print(f"Total Votes: {len(election_csv)}") 
#type (election_csv)


# In[6]:


#the total number of votes cast
election_df["Ballot ID"].count()


# In[7]:


#a complete list of candidates who received votes
election_df['Candidate'].unique()


# In[10]:


#the percentage of votes each candidate won
election_df['Candidate'].value_counts()/election_df["Ballot ID"].count()*100


# In[23]:


#the total number of votes each candidate won
election_df['Candidate'].value_counts()


# In[23]:


#the winner of the election based on popular vote.
election_df['Candidate'].mode()


# In[ ]:




