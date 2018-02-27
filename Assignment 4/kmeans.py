
# coding: utf-8

# # K-means Clustering
# 
# #### To classify News articles as belonging to 5 categories (binary classification)
# 
# Any editing needs to be done only in the cells marked with "Tune hyperparameters here"
# 
# 
# 
# 
# Useful notebook shortcuts:
# 
# Ctrl+Enter -> Run current cell
# 
# Shift+Enter -> Run current cell and go to next cell
# 
# Alt+Enter -> Run current cell and add new cell below

# In[18]:


#get_ipython().magic(u'load_ext autoreload')
#get_ipython().magic(u'autoreload 2')

import numpy as np
#from model import *
from feature import *
#from utils import *


# ### Load the training data

# In[19]:


# Change the path to the training data directory
data = readfiles1('joined')


# In[20]:


# Initialize the model and preprocess
bow = BagOfWordsFeatureExtractor()
bow.preprocess(data)


# In[36]:


# Extract fetures and create a numpy array of features
X_data_bow = bow.extract(data)


# In[34]:


from model import *

model1 = Kmeans()
#model1.train(X_train_bow, Y_train_bow, lr, reg_const)
labels = model1.cluster(X_data_bow, k=5, n_iter=25)


# ### Final Output Labels for above model get recorded
# 
# These labels will be your submission.

# In[6]:


import pickle
with open('submission.pickle','wb') as h:
    pickle.dump(labels,h)
print labels


# Using tf-idf features

# In[7]:


# Initialize the model and preprocess
tfidf = TfIdfFeatureExtractor()
tfidf.preprocess(data)


# In[8]:


# Extract fetures and create a numpy array of features
X_data_tfidf = tfidf.extract(data)


# In[9]:


model2 = Kmeans()
labels = model2.cluster(X_data_tfidf, k = 5)


# In[10]:


import pickle
with open('submission.pickle','wb') as h:
    pickle.dump(labels,h)
print labels

