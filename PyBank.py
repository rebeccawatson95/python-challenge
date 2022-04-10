#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv
import numpy as np
import pandas as pd
#open and read csv
budget_csv = "C:/Users/rebec/Desktop/UCI/Week 3/budget_hwdata.csv"
with open (budget_csv, encoding='utf') as csvfile:
    #read the header row first and skip
    csv_reader=csv.reader(csvfile,delimiter=',')
    next(csv_reader,None)
budget_df=pd.read_csv("C:/Users/rebec/Desktop/UCI/Week 3/budget_hwdata.csv")


# In[3]:


#total number of months in the data set:
budget_df["Profit/Losses"].count()


# In[4]:


#total net amount of profit/loss over the period
budget_df["Profit/Losses"].sum()


# In[5]:


#the changes in "Profit/Losses" over the entire period, and then the average of those changes
budget_df["Profit/Losses"].diff()


# In[6]:


#the average of those changes
budget_df["Profit/Losses"].diff().mean()


# In[7]:


#the greatest increase in profits (date and amount) over the entire period:
budget_df["Profit/Losses"].diff().max()
print (budget_df.max())


# In[8]:


#the greatest decrease in profits (date and amount) over the entire period:
budget_df["Profit/Losses"].diff().min()
print (budget_df.min())

