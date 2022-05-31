import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

## Importing Textblob package
from textblob import TextBlob

# Importing CountVectorizer for sparse matrix/ngrams frequencies
from sklearn.feature_extraction.text import CountVectorizer

## Import datetime
import datetime as dt

import nltk.compat
import itertools
import chardet
##### Read the data file
filepath = "../excel/"


## Checking the encoding factor
with open(filepath,"rb") as mydata:
    result = chardet.detect(mydata.read(1000000))

filepath = "../input/ebi-finance-and-qlikview-incidents-data/Incident_2017_18_Final.csv"
train_incidents = pd.read_csv(filepath,encoding="Windows-1252")