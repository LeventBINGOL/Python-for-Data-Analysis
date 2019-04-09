#!/usr/bin/env python
# coding: utf-8

#  <a href="http://cocl.us/topNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/yfe6h4az47ktg2mm9h05wby2n7e8kei3.png" width = 750, align = "center"></a>
# 
# 
# 

#  <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# 
# 
# 
# <h1 align=center><font size = 5>TUPLES IN PYTHON</font></h1>

# <a id="ref0"></a>
# <center><h2>About the Dataset</h2></center>

# 
# ## Table of Contents
# 
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <li><a href="#ref0">About the Dataset</a></li>
# <li><a href="#ref1">Tuples</a></li>
# <li><a href="#ref2">Quiz on Tuples</a></li>
# 
# <p></p>
# Estimated Time Needed: <strong>15 min</strong>
# </div>
# 
# <hr>

# Imagine you received album recommendations from your friends and compiled all of the recomendations into a table, with specific information about each album.
# 
# The table has one row for each movie and several columns:
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
# <br>
# 
# The dataset can be seen below:
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

# <hr>

# <a id="ref1"></a>
# <center><h2>Tuples</h2></center>
# 
# In Python, there are different data types: string, integer and float. These data types can all be contained in a tuple as follows:
# 
# 

# <img src = "https://ibm.box.com/shared/static/t2jw5ia78ulp8twr71j6q7055hykz10c.png" width = 750, align = "center"></a>
# 
# 

# In[1]:


tuple1=("disco",10,1.2 )
tuple1


# The type of variable is a **tuple**. 

# In[2]:


type(tuple1)


#  Each element of a tuple can be accessed via an index. The following table represents the relationship between the index and the items in the tuple. Each element can be obtained by the name of the tuple followed by a square bracket with the index number:

# <img src = "https://ibm.box.com/shared/static/83kpang0opwen5e5gbwck6ktqw7btwoe.gif" width = 750, align = "center"></a>
# 
# 

# We can print out each value in the tuple:

# In[3]:


print( tuple1[0])
print( tuple1[1])
print( tuple1[2])


# We can print out the **type** of each value in the tuple:
# 

# In[4]:


print( type(tuple1[0]))
print( type(tuple1[1]))
print( type(tuple1[2]))


# We can also use negative indexing. We use the same table above with corresponding negative values:

#  <img src = "https://ibm.box.com/shared/static/uwlfzo367bekwg0p5s5odxlz7vhpojyj.png" width = 750, align = "center"></a>
# 

# We can obtain the last element as follows (this time we will not use the print statement to display the values):

# In[5]:


tuple1[-1]


# We can display the next two elements as follows:

# In[6]:


tuple1[-2]


# In[7]:


tuple1[-3]


# We can concatenate or combine tuples by using the **+** sign:

# In[8]:


tuple2=tuple1+("hard rock", 10)
tuple2


# We can slice tuples obtaining multiple values as demonstrated by the figure below:

# <img src = "https://ibm.box.com/shared/static/s9nofy728bcnsgnx3vh159bu16w7frnc.gif" width = 750, align = "center"></a>
# 

# We can slice tuples, obtaining new tuples with the corresponding elements: 

# In[9]:


tuple2[0:3]


# We can obtain the last two elements of the tuple:

# In[10]:


tuple2[3:5]


# We can obtain the length of a tuple using the length command: 

# In[11]:


len(tuple2)


# This figure shows the number of elements:

# 
# <img src = "https://ibm.box.com/shared/static/apxe8l3w42f597yjhizg305merlm4ijf.png" width = 750, align = "center"></a>
# 

#  Consider the following tuple:

# In[12]:


Ratings  =(0,9,6,5,10,8,9,6,2)


#  We can assign the tuple to a 2nd variable:
#  

# In[13]:


Ratings1=Ratings
Ratings


# We can sort the values in a tuple and save it to a new tuple: 

# In[14]:


RatingsSorted=sorted(Ratings )
RatingsSorted


# A tuple can contain another tuple as well as other more complex data types.  This process is called 'nesting'. Consider the following tuple with several elements: 

# In[15]:


NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))


# Each element in the tuple including other tuples can be obtained via an index as shown in the figure:

# <img src = "https://ibm.box.com/shared/static/estqe2bczv5weocc4ag4mx9dtqy952fp.png" width = 750, align = "center"></a>
# 

# In[16]:


print("Element 0 of Tuple: ",   NestedT[0])
print("Element 1 of Tuple: ",  NestedT[1])
print("Element 2 of Tuple: ",  NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])


# We can use the second index to access other tuples as demonstrated in the figure:

# <img src = "https://ibm.box.com/shared/static/j1orgjuasaaj3d0feymedrnoqv8trqyo.png" width = 750, align = "center"></a>
# 

#  We can access the nested tuples :

# In[17]:


print("Element 2,0 of Tuple: ",   NestedT[2][0])
print("Element 2,1 of Tuple: ",   NestedT[2][1])
print("Element 3,0 of Tuple: ",   NestedT[3][0])
print("Element 3,1 of Tuple: ",   NestedT[3][1])
print("Element 4,0 of Tuple: ",   NestedT[4][0])
print("Element 4,1 of Tuple: ",   NestedT[4][1])


# We can access strings in the second nested tuples using a third index:

# In[18]:


NestedT[2][1][0]


# In[19]:


NestedT[2][1][1]


#  We can use a tree to visualise the process. Each new index corresponds to a deeper level in the tree:

#  <img src ='https://ibm.box.com/shared/static/vjvsygpzpwcr6czsucgno1wukyhk5vxq.gif'  width = 750, align = "center"></a>

# Similarly, we can access elements nested deeper in the tree with a fourth index:

# In[20]:


NestedT[4][1][0]


# In[21]:


NestedT[4][1][1]


# The following figure shows the relationship of the tree and the element **NestedT[4][1][1]**:

#  <img src ='https://ibm.box.com/shared/static/9y5s7515zwzc9v6i4f67yj3np2fv9evs.gif'width = 750, align = "center"></a>

#  <a id="ref2"></a>
# <h2 align=center> Quiz on Tuples </h2>

# Consider the following tuple:

# In[22]:


genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock",                 "R&B", "progressive rock", "disco") 
genres_tuple


# #### Find the length of the tuple, "genres_tuple":

# In[23]:


len(genres_tuple)


# <div align="right">
# <a href="#String1" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# 
# 
# <div id="String1" class="collapse">
# 
# "len(genres_tuple)"
#  <a ><img src = "https://ibm.box.com/shared/static/n4969qbta8hhsycs2dc4n8jqbf062wdw.png" width = 1100, align = "center"></a>
# ```
# 
# 
# ```
# </div>
# 

# #### Access the element, with respect to index 3: 

# In[26]:


genres_tuple[
3]


# <div align="right">
# <a href="#2" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# 
# 
# <div id="2" class="collapse">
# 
# 
#  <a ><img src = "https://ibm.box.com/shared/static/s6r8v2uy6wifmaqv53w6adabqci47zme.png" width = 1100, align = "center"></a>
# 
# </div>
# 
# 
# 

# ####   Use slicing to obtain indexes 3, 4 and 5:

# In[27]:


genres_tuple[3:6]


# 
#   <div align="right">
# <a href="#3" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# 
# 
# <div id="3" class="collapse">
# 
# 
#  <a ><img src = "https://ibm.box.com/shared/static/nqo84vydw6eixdex0trybuvactcw7ffi.png" width = 1100, align = "center"></a>
# 
# </div>

# #### Find the first two elements of the tuple "genres_tuple":

# In[28]:


genres_tuple[:2]


#  <div align="right">
# <a href="#q5" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# </div>
# <div id="q5" class="collapse">
# ```
# genres_tuple[0:2]
# 
# ```
# 

# #### Find the first index of 'disco':

# In[32]:


genres_tuple.index("disco")


#  <div align="right">
# <a href="#q6" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# </div>
# <div id="q6" class="collapse">
# ```
# genres_tuple.index("disco") 
# 
# ```

# <hr>

# ####  Generate a sorted List from the Tuple C_tuple=(-5,1,-3):

# In[36]:


C_tuple=(-5,1,-3)
sortedList=sorted(C_tuple)
sortedList


#  <div align="right">
# <a href="#q7" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# </div>
# <div id="q7" class="collapse">
# ```
# C_tuple = (-5,1,-3)
# C_list = sorted(C_tuple)
# C_list
# 
# ```

#  <hr></hr>
# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# <h4> [Tip] Saving the Notebook </h4>  
# 
# Your notebook saves automatically every two minutes. You can manually save by going to **File** > **Save and Checkpoint**. You can come back to this notebook anytime by clicking this notebook under the "**Recent Notebooks**" list on the right-hand side.   
# 
# 
# </div>
# <hr></hr>
# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# <h4> [Tip] Notebook Features </h4>  
#   
# Did you know there are other **notebook options**? Click on the **>** symbol to the left of the notebook:
# 
# <img src =https://ibm.box.com/shared/static/otu40m0kkzz5hropxah1nnzd2j01itom.png width = 35%>
# 
# 
# <p></p>
# 
# </div>
# <hr></hr>

#  <a href="http://cocl.us/bottemNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/irypdxea2q4th88zu1o1tsd06dya10go.png" width = 750, align = "center"></a>

# # About the Authors:  
# 
#  [Joseph Santarcangelo]( https://www.linkedin.com/in/joseph-s-50398b136/) has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 

#  <hr>
# Copyright &copy; 2017 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).​

# In[ ]:




