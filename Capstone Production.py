#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import keras


# In[2]:


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


# In[3]:


vocab_size=5000
sentence_length=20
embed_size=100


# In[4]:


from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense,GRU,Dropout,Embedding
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split as tts
from keras.models import Sequential,load_model


# In[5]:


lem = WordNetLemmatizer()
stopword = stopwords.words('english')


# In[6]:


inputs=[i for i in input().split(',')]


# In[7]:


def preprocess(text):
    corpus=[]
    words=""
    for i in text:
        word = re.sub('[^a-z_A-Z]',' ',i)
        #print(words)
        word = word.lower()
        #words = words.split()
        if word not in set(stopword):
            word = lem.lemmatize(word) 
        words = ' '.join(word)
    corpus.append(words.lstrip())
    return corpus


# In[8]:


dis={0: 'Drug Reaction',
     1: 'Malaria',
     2: 'Allergy',
     3: 'Hypothyroidism',
     4: 'Psoriasis',
     5: 'GERD',
     6: 'Chronic cholestasis',
     7: 'hepatitis A',
     8: 'Osteoarthristis',
     9: '(vertigo) Paroymsal  Positional Vertigo',
     10: 'Hypoglycemia',
     11: 'Acne',
     12: 'Diabetes',
     13: 'Impetigo',
     14: 'Hypertension',
     15: 'Peptic ulcer diseae',
     16: 'Dimorphic hemorrhoids(piles)',
     17: 'Common Cold',
     18: 'Chicken pox',
     19: 'Cervical spondylosis',
     20: 'Hyperthyroidism',
     21: 'Urinary tract infection',
     22: 'Varicose veins',
     23: 'AIDS',
     24: 'Paralysis (brain hemorrhage)',
     25: 'Typhoid',
     26: 'Hepatitis B',
     27: 'Fungal infection',
     28: 'Hepatitis C',
     29: 'Migraine',
     30: 'Bronchial Asthma',
     31: 'Alcoholic hepatitis',
     32: 'Jaundice',
     33: 'Hepatitis E',
     34: 'Dengue',
     35: 'Hepatitis D',
     36: 'Heart attack',
     37: 'Pneumonia',
     38: 'Arthritis',
     39: 'Gastroenteritis',
     40: 'Tuberculosis'}


# In[9]:


def word_to_model(inputs):
    corp = preprocess(inputs)
    one_hot_representation = [one_hot(word,vocab_size)for word in corp]
    embedding_doc = pad_sequences(one_hot_representation,maxlen=sentence_length,padding='pre')
    return embedding_doc


# In[10]:


def model_predict(inputs):
    words = word_to_model(inputs)
    model = load_model('E:\\NLP data\\NLP_MODEL\\model.h5')
    pred = model.predict(words)
    idx = (np.argmax(pred,axis=1))
    return dis[idx[0]]


# In[11]:


print(model_predict(inputs))

