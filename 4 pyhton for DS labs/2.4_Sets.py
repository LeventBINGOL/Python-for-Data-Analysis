#!/usr/bin/env python
# coding: utf-8

#  <a href="http://cocl.us/topNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/yfe6h4az47ktg2mm9h05wby2n7e8kei3.png" width = 750, align = "center"></a>
# 
# 
# 
# 

#  <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# <h1 align=center><font size = 5>Sets and Dictionaries</font></h1>

# 
# ## Table of Contents
# 
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <li><a href="#ref1">Sets</a></li>
# 
# <br>
# <p></p>
# Estimated Time Needed: <strong>20 min</strong>
# </div>
# 
# <hr>

# <a id="ref1"></a>
# <center><h2>Sets</h2></center>
# 
# In this lab, we are going to take a look at sets in Python. A set is a unique collection of objects in Python. You can denote a set with a curly bracket **{}**. Python will remove duplicate items:
# 

# In[1]:


set1={"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1


# The process of mapping is illustrated in the figure:
# 

# <a ><img src = https://ibm.box.com/shared/static/i0xb9qbetek7kbh17krx05i4lqmywahm.png width = 1100, align = "center"></a>
# 

#  You can also  create a set from a list as follows:

# In[2]:


album_list =[ "Michael Jackson", "Thriller", 1982, "00:42:19",               "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]

album_set = set(album_list)             
album_set


# Now let us create a set of  genres:

# In[3]:


music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul",                     "progressive rock", "soft rock", "R&B", "disco"])
music_genres


# #### Convert the following list to a set ['rap','house','electronic music', 'rap']:

# In[5]:


set(['rap','house','electronic music', 'rap'])


#   <div align="right">
# <a href="#q10" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="q10" class="collapse">
# ```
# set(['rap','house','electronic music','rap'])
# ```
# </div>

# Notice that the duplicates are removed and the output is sorted.

# Let us get the sum of the claimed sales:

# #### Consider the list A=[1,2,2,1] and set B=set([1,2,2,1]), does sum(A)=sum(B) 

# In[6]:


A=[1,2,2,1]  
B=set([1,2,2,1])
print("the sum of A is:",sum(A))
print("the sum of B is:",sum(B))


#  <div align="right">
# <a href="#2" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="2" class="collapse">
# ```
# No, when casting a list to a set, the new set has no repeat elements. Run the following code to verify:
# A=[1,2,2,1]  
# B=set([1,2,2,1])
# print("the sum of A is:",sum(A))
# print("the sum of B is:",sum(B))
# ```
# </div>
# 

# Now let's determine the average rating:

# ### Set Operations 

#  Let us go over Set Operations, as these can be used to change the set. Consider the set **A**:

# In[7]:


A = set(["Thriller","Back in Black", "AC/DC"] )
A


#  We can add an element to a set using the **add()** method: 

# In[8]:


A.add("NSYNC")
A


#  If we add the same element twice, nothing will happen as there can be no duplicates in a set:
# 

# In[9]:


A.add("NSYNC")
A


#  We can remove an item from a set using the remove method:

# In[10]:


A.remove("NSYNC")
A


#  We can verify if an element is in the set using the **in** command :

# In[11]:


"AC/DC"  in A


# ### Working with sets

# Remember that with sets you can check the difference between sets, as well as the symmetric difference, intersection, and union:

#  Consider the following two sets:

# In[13]:


album_set1 = set(["Thriller",'AC/DC', 'Back in Black'] )
album_set2 = set([ "AC/DC","Back in Black", "The Dark Side of the Moon"] )


#  <a ><img src = "https://ibm.box.com/shared/static/bl6ijga6g8r7bdfkl17qw7zh62czte47.png" width = 850, align = "center"></a>
#   <h4 align=center>  Visualizing the sets as two circles 
#  
#   </h4> 

# In[14]:


album_set1, album_set2


#  As both sets contain 'AC/DC' and 'Back in Black' we represent these common elements with the intersection of two circles.    
# 

#  <a ><img src = "https://ibm.box.com/shared/static/7ttuf8otui4s6axm23csmb4s3pxz16y2.png" width = 650, align = "center"></a>
#   <h4 align=center>  Visualizing common elements with the intersection of two circles.
#  
#   </h4> 

# We can find the common elements of the sets as follows:

# In[15]:


album_set_3=album_set1 & album_set2
album_set_3


# We can find all the elements that are only contained in **album_set1** using the **difference** method:

# In[16]:


album_set1.difference(album_set2)  


# We only consider elements in **album_set1**; all the elements in **album_set2**, including the intersection, are not included.
# 

#  <a ><img src = "https://ibm.box.com/shared/static/osmxw1qnb5t9odon2cx94wxhfzlkn1n8.png" width = 650, align = "center"></a>
#   <h4 align=center>  The difference of “album_set1” and   “album_set2
#  
#   </h4> 

# The difference between **album_set2** and **album_set1** is given by:

# In[17]:


album_set2.difference(album_set1)  


# <a ><img src = "https://ibm.box.com/shared/static/klgc09bgpsjudr9v3wtl8yk9s2lya3hl.png" width = 650, align = "center"></a>
#   <h4 align=center>  The difference of **album_set2** and   **album_set1**
#  
#   </h4> 

# We can also find the intersection, i.e in both **album_list2** and **album_list1**, using the intersection command :

# In[18]:


album_set1.intersection(album_set2)   


#  This corresponds to the intersection of the two circles:

#  <a ><img src = "https://ibm.box.com/shared/static/s2xfytq43twp6jsvbvr4o2fir7wdablo.png" width = 650, align = "center"></a>
#   <h4 align=center>  Intersection of set
#  
#   </h4> 

#  The union corresponds to all the elements in both sets, which is represented by colouring  both circles:
# 

#  <a ><img src = "https://ibm.box.com/shared/static/vkczce5jh50g0oh53xn0ilgriflcrog0.png" width = 650, align = "center"></a>
#   <h4 align=center> Figure 7:  Union of set
#  
#   </h4> 

#  The union is given by:

# In[19]:


album_set1.union(album_set2)


# And you can check if a set is a superset or subset of another set, respectively, like this:

# In[20]:


set(album_set1).issuperset(album_set2)   


# In[21]:


set(album_set2).issubset(album_set1)     


# Here is an example where **issubset()** is **issuperset()** is true:

# In[22]:


set({"Back in Black", "AC/DC"}).issubset(album_set1) 


# In[23]:


album_set1.issuperset({"Back in Black", "AC/DC"})   


# #### Create a new set “album_set3” that is the union of “album_set1” and “album_set2”:

# In[28]:


album_set3=album_set1.union(album_set2)
album_set3


# <div align="right">
# <a href="#4" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="4" class="collapse">
# ```
# album_set3=album_set1.union(album_set2)
# album_set3
# ```
# </div>

# #### Find out if  "album_set1" is a subset of "album_set3":

# In[29]:


album_set1.issubset(album_set2)


#  <div align="right">
# <a href="#5" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="5" class="collapse">
# ```
# album_set1.issubset(album_set3)  
# 
# ```
# </div>

# 
#  <a href="http://cocl.us/bottemNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/irypdxea2q4th88zu1o1tsd06dya10go.png" width = 750, align = "center"></a>

# 
# 
# # About the Authors:  
# 
#  [Joseph Santarcangelo]( https://www.linkedin.com/in/joseph-s-50398b136/) has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 
# 

#  <hr>
# Copyright &copy; 2017 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).
