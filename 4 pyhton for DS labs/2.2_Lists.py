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
# <h1 align=center><font size = 5>LISTS  IN PYTHON</font></h1>

# 
# ## Table of Contents
# 
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <li><a href="#ref0">About the Dataset</a></li>
# <li><a href="#ref1">Lists</a></li>
# <li><a href="#ref2">Quiz</a></li>
# <br>
# <p></p>
# Estimated Time Needed: <strong>15 min</strong>
# </div>
# 
# <hr>

# <a id="ref0"></a>
# <center><h2>About the Dataset</h2></center>

# Imagine you received many music recommendations from your friends and compiled all of the recommendations into a table, with specific information about each movie.
# 
# The table has one row for each album and several columns:
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
# <center><h2>Lists</h2></center>
# 
# We are going to take a look at lists in Python. A list is a sequenced collection of different objects such as integers, strings, and other lists as well. The address of each element within a list is called an 'index'. An index is used to access and refer to items within a list.
# 

# <a ><img src = "https://ibm.box.com/shared/static/eln445fv5nzv3wlm4u8dnfhbrcrv0hff.png" width = 1000, align = "center"></a>
#   <h4 align=center> Representation of a list  
#   </h4> 
# 
# 
# 
# 

#  To create a list, type the list within square brackets **[ ]**, with your content inside the parenthesis and separated by commas. Let’s try it!

# In[1]:


L = ["Michael Jackson" , 10.1,1982]
L


# We can use negative and regular indexing with a list :

#  <a ><img src = "https://ibm.box.com/shared/static/a7ac9lnvmcaz29n86ffez4as27fl3n9m.png" width = 1000, align = "center"></a>
#   <h4 align=center> Representation of a list  
#   </h4> 
# 

# In[2]:


print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )


# Lists can contain strings, floats, and integers. We can nest other lists, and we can also nest tuples and other data structures. The same indexing conventions apply for nesting:    
# 

# In[3]:


[ "Michael Jackson", 10.1,1982,[1,2],("A",1) ]


#  We can also perform slicing in lists. For example, if we want the last two elements, we use the following command:

# In[4]:


L = [ "Michael Jackson", 10.1,1982,"MJ",1]
L


# 
# <a ><img src = "https://ibm.box.com/shared/static/pt3pfp1sg5okwuwwpy0dnj8e94fl2mwy.png" width = 1000, align = "center"></a>
#   <h4 align=center> Representation of a list  
#   </h4> 

# In[5]:


L[3:5]


# We can use the method "extend" to add new elements to the list:

# In[6]:


L = [ "Michael Jackson", 10.2]
L.extend(['pop',10])
L


# Another similar method is 'appended'. If we apply 'appended' instead of 'extended', we add one element to the list:

# In[8]:


L = [ "Michael Jackson", 10.2]
L.append(['pop',10])
L


#  Each time we apply a method, the list changes. If we apply "extend" we add two new elements to the list. The list **L** is then modified by adding two new elements:

# In[9]:


L = [ "Michael Jackson", 10.2]
L.extend(['pop',10])
L


# If we append the list  **['a','b']** we have one new element consisting of a nested list:

# In[10]:


L.append(['a','b'])
L


# As lists are mutable, we can change them. For example, we can change the first element as follows:

# In[11]:


A = ["disco",10,1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)


#  We can also delete an element of a list using the **del** command:

# In[ ]:


print('Before change:', A)
del(A[0])
print('After change:', A)


#  We can convert a string to a list using 'split'.  For example, the method **split** translates every group of characters separated by a space into an element in a list:
# 

# In[12]:


'hard rock'.split()


# We can use the split function to separate strings on a specific character. We pass the character we would like to split on into the argument, which in this case is a comma.  The result is a list, and each element corresponds to a set of characters that have been separated by a comma: 

# In[13]:


'A,B,C,D'.split(',')


#  When we set one variable  **B** equal to **A**;  both **A** and **B** are referencing the same list in memory :

# In[16]:


A = ["hard rock",10,1.2]
B = A
print('A:', A)
print('B:', B)


#  <a ><img src = 'https://ibm.box.com/shared/static/7g2u8hqqb4birdwn7m9uir4s9wfj8mko.png' width = 1000, align = "center"></a>
#   

#  Initially, the value of the first element in ** B** is set as hard rock. If we change the first element in **A**  to 'banana', we get an unexpected side effect.  As **A** and **B ** are referencing the same list, if we change list **A**, then list **B** also changes.  If we check the first element of **B** we get banana instead of hard rock:

# In[17]:


print('Before changing A[0], B[0] is ',B[0])
B[0] = "banana"
print('After changing A[0], A[0] is ',A[0])
print('After changing A[0], B[0] is ',B[0])


# This is demonstrated in the following figure: 

#  <a ><img src = https://ibm.box.com/shared/static/thdu6y5pzh99qpun4tu2fjvj86st0hbu.gif width = 1000, align = "center"></a>
# 
# 
# 

# You can clone list  **A** by using  the following syntax:

# In[18]:


B = A[:]
B


#  Variable **B** references a new copy or clone of the original list; this is demonstrated in the following figure:

# 
#  <a ><img src = https://ibm.box.com/shared/static/gwx86gaoeizqjvx7xj96cb8i9hn684ei.gif width = 1000, align = "center"></a>
# 
# 
# 

# Now if you change **A**, **B** will not change: 
# 

# In[19]:


print('Before changing A[0], B[0] is ',B[0])
A[0] = "apple"
print('After changing A[0], A[0] is ',A[0])
print('After changing A[0], B[0] is ',B[0])


# In[ ]:





#  <a id="ref2"></a>
# <center><h2>Quiz</h2></center>

# #### Create a list 'a_list' , with the following elements 1, “hello”, [1,2,3 ] and True. 

# In[32]:


l_list=[1,"hello", [1,2,3 ],True]
l_list


#  <div align="right">
# <a href="#q1" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# </div>
# <div id="q1" class="collapse">
# ```
# a_list=[1, 'hello', [1,2,3 ] , True]
# a_list
# 
# ```
# </div>

# ####  Find the value stored at index 1 of 'a_list'.

# In[33]:


l_list[1]


#  <div align="right">
# <a href="#q2" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# </div>
# <div id="q2" class="collapse">
# ```
# a_list[1]
# 
# 
# ```
# </div>

# ####  Retrieve the elements stored at index 1 and 2 of 'a_list'.

# In[26]:


l_list[1:3]


#  <div align="right">
# <a href="#q3" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# </div>
# <div id="q3" class="collapse">
# ```
# a_list[1:3]
# 
# ```

# #### 4) Concatenate the following lists A=[1,'a'] abd B=[2,1,'d']:

# In[42]:


A=[1,"a"]
B=[2,1,"d"]
A+=B
A


#  <div align="right">
# <a href="#q4" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# </div>
# <div id="q4" class="collapse">
# ```
# A=[1,'a'] 
# B=[2,1,'d']
# A+B
# ```

#  <a href="http://cocl.us/bottemNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/irypdxea2q4th88zu1o1tsd06dya10go.png" width = 750, align = "center"></a>

# # About the Authors:  
# 
#  [Joseph Santarcangelo]( https://www.linkedin.com/in/joseph-s-50398b136/) has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact 
#  ]human cognition. Joseph has been working for IBM since he completed his PhD.
# 

#  <hr>
# Copyright &copy; 2017 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).​

# In[ ]:




