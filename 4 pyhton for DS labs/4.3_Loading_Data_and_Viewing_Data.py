#!/usr/bin/env python
# coding: utf-8

# <a href="http://cocl.us/topNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/yfe6h4az47ktg2mm9h05wby2n7e8kei3.png" width = 750, align = "center"></a>
# 
# 
# 

# # <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# <h1 align=center><font size = 5>Introduction to Pandas  Python</font></h1>

# # Table of Contents
# 
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <li><a href="#ref0">About the Dataset</a></li>
# <li><a href="#ref1">Importing Data</a></p></li>
# <li><a href="#ref2">Viewing Data and Accessing Data </a></p></li>
# <br>
# <p></p>
# Estimated Time Needed: <strong>15 min</strong>
# </div>
# 
# <hr>

# <a id="ref0"></a>
# <h2 align=center>About the Dataset</h2>

# 
# 
# The table has one row for each album and several columns
# 
# - **artist** - Name of the artist
# - **album** - Name of the album
# - **released_year** - Year the album was released
# - **length_min_sec** - Length of the album (hours,minutes,seconds)
# - **genre** - Genre of the album
# - **music_recording_sales_millions** - Music recording sales (millions in USD) on [SONG://DATABASE](http://www.song-database.com/)
# - **claimed_sales_millions** - Album's claimed sales (millions in USD) on [SONG://DATABASE](http://www.song-database.com/)
# - **date_released** - Date on which the album was released
# - **soundtrack** - Indicates if the album is the movie soundtrack (Y) or (N)
# - **rating_of_friends** - Indicates the rating from your friends from 1 to 10
# <br>
# 
# You can see the dataset here:
# 
# <font size="1">
# <table font-size:xx-small style="width:25%">
#   <tr>
#     <th>Artist</th>
#     <th>Album</th> 
#     <th>Released</th>
#     <th>Length</th>
#     <th>Genre</th> 
#     <th>Music recording sales (millions)</th>
#     <th>Claimed sales (millions)</th>
#     <th>Released</th>
#     <th>Soundtrack</th>
#     <th>Rating (friends)</th>
#   </tr>
#   <tr>
#     <td>Michael Jackson</td>
#     <td>Thriller</td> 
#     <td>1982</td>
#     <td>00:42:19</td>
#     <td>Pop, rock, R&B</td>
#     <td>46</td>
#     <td>65</td>
#     <td>30-Nov-82</td>
#     <td></td>
#     <td>10.0</td>
#   </tr>
#   <tr>
#     <td>AC/DC</td>
#     <td>Back in Black</td> 
#     <td>1980</td>
#     <td>00:42:11</td>
#     <td>Hard rock</td>
#     <td>26.1</td>
#     <td>50</td>
#     <td>25-Jul-80</td>
#     <td></td>
#     <td>8.5</td>
#   </tr>
#     <tr>
#     <td>Pink Floyd</td>
#     <td>The Dark Side of the Moon</td> 
#     <td>1973</td>
#     <td>00:42:49</td>
#     <td>Progressive rock</td>
#     <td>24.2</td>
#     <td>45</td>
#     <td>01-Mar-73</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
#     <tr>
#     <td>Whitney Houston</td>
#     <td>The Bodyguard</td> 
#     <td>1992</td>
#     <td>00:57:44</td>
#     <td>Soundtrack/R&B, soul, pop</td>
#     <td>26.1</td>
#     <td>50</td>
#     <td>25-Jul-80</td>
#     <td>Y</td>
#     <td>7.0</td>
#   </tr>
#     <tr>
#     <td>Meat Loaf</td>
#     <td>Bat Out of Hell</td> 
#     <td>1977</td>
#     <td>00:46:33</td>
#     <td>Hard rock, progressive rock</td>
#     <td>20.6</td>
#     <td>43</td>
#     <td>21-Oct-77</td>
#     <td></td>
#     <td>7.0</td>
#   </tr>
#     <tr>
#     <td>Eagles</td>
#     <td>Their Greatest Hits (1971-1975)</td> 
#     <td>1976</td>
#     <td>00:43:08</td>
#     <td>Rock, soft rock, folk rock</td>
#     <td>32.2</td>
#     <td>42</td>
#     <td>17-Feb-76</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
#     <tr>
#     <td>Bee Gees</td>
#     <td>Saturday Night Fever</td> 
#     <td>1977</td>
#     <td>1:15:54</td>
#     <td>Disco</td>
#     <td>20.6</td>
#     <td>40</td>
#     <td>15-Nov-77</td>
#     <td>Y</td>
#     <td>9.0</td>
#   </tr>
#     <tr>
#     <td>Fleetwood Mac</td>
#     <td>Rumours</td> 
#     <td>1977</td>
#     <td>00:40:01</td>
#     <td>Soft rock</td>
#     <td>27.9</td>
#     <td>40</td>
#     <td>04-Feb-77</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
# </table></font>

# <a id="ref1"></a>
# <h2 align=center> Importing Data </h2>

# We can import the libraries  or dependency like Pandas  using the following command:

# In[78]:


import pandas as pd


# After the import command, we now have access to a large number of pre-built classes and functions. This assumes the library is installed; in our lab environment all the necessary libraries are installed. One way pandas allows you to work with data is a dataframe. Let's go through the process to go from a comma separated values (**.csv** ) file to a dataframe. This variable **csv_path** stores the path of the  **.csv** ,that is  used as an argument to the **read_csv** function. The result is stored in the object ** df**, this is a common short form used for a variable referring to a Pandas dataframe. 

# In[79]:


csv_path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/top_selling_albums.csv'
df = pd.read_csv(csv_path)


#  <div class="alert alert-block alert-info" style="margin-top: 20px">
#  <a href="http://cocl.us/object_storage_corsera"><img src = "https://ibm.box.com/shared/static/6qbj1fin8ro0q61lrnmx2ncm84tzpo3c.png" width = 750, align = "center"></a>

# We can use the method **head()** to examine the first five rows of a dataframe: 
# 

# In[87]:


df.head(5)


# The process for loading an excel file is similar, we use the path of the excel file and the function **read_excel**. The result is a data frame as before:

# In[89]:


#dependency  needed to install file 
get_ipython().system('pip install xlrd')


# In[90]:


xlsx_path='https://ibm.box.com/shared/static/mzd4exo31la6m7neva2w45dstxfg5s86.xlsx'

df = pd.read_excel(xlsx_path)
df.head()


# We can access the column "Length" and assign it a new dataframe 'x':
# 

# In[93]:


x=df[['Length']][0:1]
x


#  The process is shown in the figure: 

#  <img src = "https://ibm.box.com/shared/static/bz800py5ui4w0kpb0k09lq3k5oegop5v.png" width = 750, align = "center"></a>

#  <a id="ref2"></a>
# <h2 align=center> Viewing Data and Accessing Data </h2>

# You can also assign the value to a series, you can think of a Pandas series as a 1-D dataframe. Just use one bracket: 

# In[99]:


x=df['Length'][0:2]
x


# You can also assign different columns, for example, we can assign the column 'Artist':

# In[8]:


x=df[['Artist']]
x


# #### Assign the variable 'q' to the dataframe that is made up of the column 'Rating':
# 

# In[ ]:





#  <div align="right">
# <a href="#q1" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="q1" class="collapse">
# ```
# q=df[['Rating']]
# q
# ```
# </div>

# You can do the same thing for multiple columns; we just put the dataframe name, in this case, **df**, and the name of the multiple column headers enclosed in double brackets. The result is a new dataframe comprised of the specified columns:

# In[9]:


y=df[['Artist','Length','Genre']]
y


# The process is shown in the figure:

#  <img src = "https://ibm.box.com/shared/static/dh9duk3ucuhmmmbixa6ugac6g384m5sq.png" width = 1100, align = "center"></a>

# In[10]:


df[['Album','Released','Length']]


# #### Assign the variable 'q' to the dataframe that is made up of the column 'Released' and 'Artist':

#  <div align="right">
# <a href="#q2" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="q2" class="collapse">
# ```
# q=df[['Released','Artist']]
# q
# ```
# </div>

# One way to access unique elements is the 'ix' method, where you can access the 1st row and first column as follows :

# In[152]:


#**ix** will be deprecated, use **iloc** for integer indexes 
#df.ix[0,0]
df.loc[0:0,'Artist']


# You can access the 2nd  row and first column as follows:

# In[158]:


#**ix** will be deprecated, use **iloc** for integer indexes
#df.ix[1,0]
df.iloc[0:1,0]


#  You can access the 1st row 3rd column as follows: 

# In[13]:


#**ix** will be deprecated, use **iloc** for integer indexes
#df.ix[0,2]
df.iloc[0,2]


# #### Access the 2nd row  3rd column:

# In[23]:


df.iloc[1,2]


#  <div align="right">
# <a href="#q3" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="q3" class="collapse">
# ```
# df.ix[1,2]
#     
# or df.iloc[0,2]
# ```
# </div>

# You can access the column using the name as well, the following are the same as above: 

# In[16]:


#**ix** will be deprecated, use **loc** for label-location based indexer
#df.ix[0,'Artist']
df.loc[0,'Artist']


# In[25]:


#**ix** will be deprecated, use **loc** for label-location based indexer
#df.ix[1,'Artist']
df.loc[1,'Artist']


# In[24]:


#**ix** will be deprecated, use **loc** for label-location based indexer
#df.ix[0,'Released']
df.loc[0,'Released']


# In[26]:


#**ix** will be deprecated, use **loc** for label-location based indexer
#df.ix[1,'Released']
df.loc[1,'Released']


# In[28]:


df.iloc[1,2]


# You can perform slicing using both the index and the name of the column:

# In[77]:


#**ix** will be deprecated, use **loc** for label-location based indexer
#df.ix[0:2, 0:3]
df.iloc[2:3,0:2]


# In[76]:


#**ix** will be deprecated, use **loc** for label-location based indexer
#df.ix[0:2, 'Artist':'Released']
df.loc[2:3, 'Artist':'Album']


# 
#  <a href="http://cocl.us/bottemNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/irypdxea2q4th88zu1o1tsd06dya10go.png" width = 750, align = "center"></a>

# ### About the Authors:  
# 
#  [Joseph Santarcangelo]( https://www.linkedin.com/in/joseph-s-50398b136/) has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 

# Copyright &copy; 2017 [cognitiveclass.ai](https:cognitiveclass.ai). This notebook and its source code are released under the terms of the [MIT License](cognitiveclass.ai).
