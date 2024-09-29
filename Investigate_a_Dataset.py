#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: Investigate a Dataset -[ tmdb-movies]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# This data set contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue.
# 
# 
# 
# ### Question(s) for Analysis
# Q1:what gener have most revenues?
# 
# Q2:what is the top 5 rated movies?
# 
#  

# In[1]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('', 'matplotlib inline')
# While optional for current notebooks, if you are having trouble with visualizations,
#   remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# in this section i loaded the dataset , cheack for cleanliness, and then clean it and prepared for analysis
# 
# 
# ### General Properties
# This data set contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue

# In[2]:


# Load your data and print out a few lines. What is the size of your dataframe? 
#   Perform operations to inspect data types and look for instances of missing
#   or possibly errant data. 

df = pd.read_csv('Database_TMDb_movie_data/tmdb-movies.csv')
df.head(1)


# In[3]:


df.info()


# In[4]:


df.shape


# In[5]:


df.describe()


# 
# ### Data Cleaning
# before starting my analsis i cheack the dataset and found missing values,  inapropiate datatype I cleaned the database.
# 1) I removed the columns " cast, homepage, tagline, keywords, overview and imdb_id" to enhance database redability.
# 
# 2) 'Genres' and 'productions_companies' had multiple values in the same row of data, therefore in order to improve grouping and provide a cleaner representation for the analysis that follows, I chose to eliminate the values after the first '|' symbol.
# 
# 3) I converted the string "release_date" to a date datatype.
#  

# In[6]:


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.
df = df.drop(['cast','homepage','tagline','keywords','overview','imdb_id'], axis=1)


# In[7]:


df = df.dropna()
df.info()


# In[ ]:


df.dropna(inplace=True)
df.info()


# In[10]:


df['release_date'] = pd.to_datetime(df['release_date'])


# In[11]:


df['genres'] = df['genres'].apply(lambda x: x.split('|')[0])
df['production_companies'] = df['production_companies'].apply(lambda x: x.split('|')[0])


# In[12]:


df.head(3)


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# after cleansing the data set. I begin analyzing to find the answers to my questions:
# 
# 
# ###  Question 1 (what gener have most revenues?)

# In[13]:


# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.
genresrevenue = df.groupby(['genres'])['revenue'].sum()
print(genresrevenue)


# In[14]:


plt.subplots(figsize=(20,8))
plt.bar(genresrevenue.index, genresrevenue)
plt.title('genres revenues')


# ### Question 2  (what is the top 5 rated movies)

# In[15]:


# Continue to explore the data to address your additional research
#   questions. Add more headers as needed if you have more questions to
#   investigate.
five_top_rated_movies= df.sort_values(by=['vote_average'],ascending=False).head(5)
five_top_rated_movies.head()


# In[16]:


plt.subplots(figsize=(10,6))
plt.bar(five_top_rated_movies['original_title'],five_top_rated_movies['vote_average'] )
plt.title('five_top_rated_movies')
plt.xticks(rotation="vertical")


# <a id='conclusions'></a>
# ## Conclusions
# 
# In my first question I found that action movies get the most revenues, then adventure movies.
# 
# 
# In my second question i found the "Pink Floyd: Pulse" is the top rated movie with avrege vote 8.7 , “A Personal Journey with Martin Throug american movies, The Art of Flight, Queen - Rock Montreal" comes in a second place with avrege vote 8.5, and then comes The "Jinx: The Life and Deaths of Robert Durst" with avrege vote 8.4  
# 
# 

# In[17]:


# Running this cell will execute a bash command to convert this notebook to an .html file
get_ipython().system('python -m nbconvert --to html Investigate_a_Dataset.ipynb')


# In[ ]:




