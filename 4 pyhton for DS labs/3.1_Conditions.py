#!/usr/bin/env python
# coding: utf-8

#  <a href="http://cocl.us/topNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/yfe6h4az47ktg2mm9h05wby2n7e8kei3.png" width = 750, align = "center"></a>
# 
# 
# 

# <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# <h1 align=center><font size = 5>LOOPS AND CONDITIONAL EXECUTION IN PYTHON</font></h1>

# ## Table of Contents
# 
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <li><a href="#ref1">Comparison Operators </a></li>
# <li><a href="#ref2">Branching</a></li>
# <li><a href="#ref3">Logic Operation </a></li>
# <br>
# <p></p>
# Estimated Time Needed: <strong>15 min</strong>
# </div>
# 
# <hr>

# <a id="ref1"></a>
# <center><h2>COMPARISON OPERATORS</h2></center>

# Comparison operations compare some value or operand and, based on a condition, they produce a Boolean. When comparing two values you can use these operators:
# 
# <ul>
# <li>equal: `==`
# <li>not equal: `!=`
# <li>greater than: `>`</li>
# <li>less than: `<`</li>
# <li>greater than or equal to: `>=`</li>
# <li>less than or equal to: `<=`</li>
# </ul>
# 
# 

# Let's say we assign **a** a value of 6. We can use the equality operator denoted with two equal (**==**) signs to determine if two values are equal.

# In[1]:


a=5

a==6


#  The result is false, as 5 does not equal 6.

# Consider the following equality comparison operator **i>5**. If the value of the left operand, in this case the variable **i**, is higher than the value of the right operand, in this case 5, then the condition becomes **True** or else we get a **False**.  If we set **i** equal to 6, we see that 6 is larger than 5 and as a result, we get **True**.  
# 

# In[2]:


i=6
i>5


# If we set **i=2** the condition is false as 2 is less than 5:

# In[3]:


i=2
i>5


#  Let's display some values for **i** in the figure. Set the values greater than 5 in green and the rest in red. The green region represents where the condition is **True**, the red where the statement is false. If the value of **i** is 2, we get **False** as the 2 falls in the red region. Similarly, if the value for **i** is 6 we get a **True** as the condition falls in the green region. 

# <a ><img src = "https://ibm.box.com/shared/static/xr028o5qcvxgdn3i1rqsjbxwaq5gb4ki.gif" width = 500, align = "center"></a>
#   <h4 align=center> 
#   </h4>
# 

#  The inequality test uses an exclamation mark preceding the equal sign, if two operands are not equal then the condition becomes **True**.  For example, the following condition will produce **True** as long as the value of **i** is not equal to 6:
# 

# In[4]:


i=2
i!=6


# When **i** equals  six the expression produces **False**. 

# In[5]:


i=6
i!=6


#  We can use a number line as before, when the condition is **True** the corresponding numbers are marked in green and for where the condition is **False** the corresponding number is marked in red.  If we set **i** equal to 2  the operator is true as 2 is in the green region. If we set **i** equal to 6 we get a **False** as the condition falls in the red region.

#  <a ><img src = https://ibm.box.com/shared/static/pf6rvks8eh4e1riwki59gx7s9rvmidu4.gif width = 500, align = "center"></a>
#   <h4 align=center> 
#   </h4>
# 

#  We can use the same methods on strings, for example, if we use an equality operator on two different strings. As the strings are not equal, we get a **False**.

# In[6]:


"ACDC"=="Michael Jackson"


#  If we use the inequality operator, we get a **True** as the strings are not equal.

# In[7]:


"ACDC"!="Michael Jackson"


#  We can also perform inequality operations, the order of the letter depends on the ASCII value. The decimal value shown in the following table represents  the order of the character:
# 

#  <a ><img src =https://ibm.box.com/shared/static/4grvg0o9bvhp80u88lkfcsdlvg4whvzs.svg width = 1000, align = "center"></a>
#   <h4 align=center> 
#   </h4>

# For example, the decimal equivalent of **!** is 21, while the decimal equivalent of **+** is 43. Therefore **+** is larger than **!**.

# In[8]:


'+'>'!'


#  Similarly, the value for  **A** is 101, and the value for  **B** is 102 therefore:

# In[9]:


'B'>'A'


#  When there are multiple letters, the first letter takes precedence in ordering:

# In[10]:


'BA'>'AB'


# <a id="ref2"></a>
# <center><h2>Branching</h2></center>
# 
# 
# 

#  Branching allows us to run different statements for different inputs. It is helpful to think of an **if statement** as a locked room, if the statement is true you can enter the room and your program will run some predefined task, but if the statement is false your program will skip the task.
# 

#  For example, consider the blue rectangle representing an ACDC concert. If the individual is 18 or older, they can enter the ACDC concert. If they are under the age of 18 they cannot enter the concert. We have the if statement and we have the expression that can be **True** or **False**, the brackets are not necessary.  We have a colon within an indent; then we have the expression that is run if the condition is **True**. The statements after the **if statement** will run regardless of whether the condition is true or false.

# In[11]:


age=19
#age=18

#expression that can be true or false
if age>18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )


#The statements after the if statement will run regardless if the condition is true or false 
print("move on")


# **Try uncommenting the age variable**.
# 
# It is helpful to use the following diagram to illustrate the process. On the left side, we see what happens when the condition is **True**.  The person enters the ACDC concert representing the code in the indent being executed; they then move on. On the right side, we see what happens when the condition is **False**; the person is not granted access, and the person moves on. In this case, the segment of code in the indent does not run, but the rest of the statements are run. 
#  
# 

# <a ><img src =https://ibm.box.com/shared/static/l7y2t7evi5gy5n5qry718gyejkha2azk.gif width = 1000, align = "center"></a>
#   <h4 align=center> 
#   </h4>

# The **else** statement will run a different block of code if the same condition is false.  Let's use the ACDC concert analogy again. If the user is 17 they can not go to the ACDC concert,  but they can go to the Meatloaf concert.
# The syntax of the **else** statement is similar; we simply append the statement **else** with the new condition.
# Try changing the values of **age** to see what happens:  

# In[12]:


age=18
#age=19
if age>18:
    
    print("you can enter" )
 
else:
    print("go see Meat Loaf" )
    

print("move on")


# The process is demonstrated below, where each of the possibilities is illustrated on each side of the image. On the left is the case where the age is 17, we set the value of the variable age to 17, and this corresponds to the individual attending the Meatloaf concert. The right portion shows what happens when the individual is over 18, and the individual is granted access to the concert.

#  <a ><img src =https://ibm.box.com/shared/static/hkf892cpt2tx7vrt072jdp4khne0mv00.gif width = 1000, align = "center"></a>
#   <h4 align=center> 
#   </h4>

# The **elif** statement, short for else if, allows us to check additional conditions if the proceeding condition is false. If the condition is **True**, the alternate expressions will be run. Consider the concert example, where if the individual is 18 they will go to the Pink Floyd concert instead of attending the ACDC or Meat-loaf concert. The person of 18 years of age enters the area, and as they are not over 19 years of age they can not see ACDC, but as they are 18 years of age, they attend  Pink Floyd. After seeing Pink Floyd, they move on. The syntax of the **elif** statement is similar in that we merely add the statement **elif** with the condition. We then add the expression we would like to execute it the statement is **True**  with an indent.

# In[13]:


age=18
if age>18:
    
    print("you can enter" )
elif age==18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    

print("move on")


# The three combinations are shown in the figure below.  The left-most region shows what happens when the individual is less than 18 years of age. The central component shows when the individual is 18. The rightmost shows when the individual is over 18.

#  <a ><img src =https://ibm.box.com/shared/static/bfdcim06oly4u5t3x9dthskr0chxwyys.gif width = 1000, align = "center"></a>
#   <h4 align=center> 
#   </h4>

#  Look at the following code:
# 

# In[14]:


album_year = 1983
album_year=1970
if album_year > 1980:
    print("Album year is greater than 1980")
    
print("")
print('do something..')


# Feel free to change **`album_year`** value to other values -- you'll see that the result changes!

# Notice that the code in the above **indented** block will only be executed if the results are **True**. 

# ####  Write an if statement to determine if an album had a rating greater than 8. Test it using the rating for the album  “Back in Black” that had a rating of 8.5.   If the statement  is true print "this album is Amazing !"
# 

# In[ ]:





#  <div align="right">
# <a href="#q1" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="q1" class="collapse">
# ```
# rating=8.5
# 
# if rating>8:
#     print "this album is Amazing !"
# 
# ```
# </div>

# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# **Tip**: This syntax can be spread over multiple lines for ease of creation and legibility.
# </div>

# As before, we can add an **else** block to the **if** block.  The code in the  **else** block will only be executed if the result is **False**.
# 
# 
# **Syntax:** 
# 
# if (condition):
#     # do something
# else:
#     # do something else

#  If the condition in the if statement is false, the statement after the else block will execute. This is demonstrated in the figure: 
# 

#  <a ><img src = "https://ibm.box.com/shared/static/zygha3mwjwrcfok2jrivu7z5iirt4xgt.png" width = 500, align = "center"></a>
#   <h4 align=center> 
#   </h4>
# 
# 
# 

# In[15]:


album_year = 1983
#album_year=1970
if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")
print("")
print('do something..')


# Feel free to change the **`album_year`** value to other values -- you'll see that the result changes based on it!

# #### Write an if-else statement that performs the following. If the rating is larger then eight print “this album is amazing”. If the rating is less, then or equal to 8 print “this album is ok”.   
# 

# In[ ]:





#  <div align="right">
# <a href="#q2" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="q2" class="collapse">
# ```
# rating = 8.5
# #try with this value
# #rating = 8
# if rating > 8:
#     print "this album is amazing"
# else:
#     print "this album is ok
# ```
# </div>

#  <a id="ref3"></a>
# <center><h2>Logical operators</h2></center>

# 
# Sometimes you want to check more than one condition at once. For example, you might want to check if one condition and another condition is **True**. Logical operators allow you to combine or modify conditions.
# <ul>
# <li> `and`
# <li> `or`
# <li> `not` 
# </ul>
# 
# These operators are summarized for two variables using the following truth tables:  

#  <a ><img src = "https://ibm.box.com/shared/static/kbkqfu6apx9wczu79j6ug8xs9c6tt3d3.png" width = 500, align = "center"></a>
#   <h4 align=center> 
#   </h4>
# 

#  The **and** statement is only **True** when both conditions are true. The **or** statement is true if one condition is **True**.    Finally the **not** statement outputs the opposite truth value.

# We would like to determine if an album was released after 1980 and before 1990. Both time periods between 1981 and 1989 satisfy this condition. This is demonstrated in the figure below. The green on lines **a** and **b** represents periods where the statement is **True**. The green on line **c** represents where both conditions are **True**, this corresponds to where the green regions overlap. 
# 
# 

#  <a ><img src = "https://ibm.box.com/shared/static/mtvdx315p1a2bp6e1vqv3uppnzp3wu2i.png" width = 500, align = "center"></a>
#   <h4 align=center> An example of an if else statement 
#   </h4>
# 

#  The block of code to perform this check is given by:

# In[16]:


album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1981 and 1989")
    
print("")
print("Do Stuff..")


# To determine if an album was released before 1980 or after 1990, we can use an **or** statement. Periods before 1981 or after 1989 satisfy this condition. This is demonstrated in the following figure, the color green in **a** and **b** represents periods where the statement is true. The color green in **c** represents where at least one of the conditions 
# are true.  
# 

#  <a ><img src = "https://ibm.box.com/shared/static/lw0zehvs2rrs9yjit5i0mf2zgtfe6rl1.png" width = 500, align = "center"></a>
#   <h4 align=center>  An example of an if else statement 
#   </h4>
# 

# The block of code to perform this check is given by:

# In[17]:


album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")


# The **not** statement checks if the statement is false:

# In[18]:


album_year = 1983

if not (album_year == '1984'):
    print ("Album year is not 1984")


# #### Write an if statement to determine if an album came out before 1980 or in the years: 1991 or 1993. If the condition is true print out the year the album came out.
# 

# In[ ]:





# # <div align="right">
# <a href="#q3" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="q3" class="collapse">
# ```
# album_year = 1993
# if (album_year<1980) or (album_year==1991) or (album_year==1993):
#     print "the year is",album_year 
# 
# ```
# </div>

# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# **Tip**: All the expressions will return the value in Boolean format -- this format can only house two values: true or false!
# </div>

# <hr>

# 
#  <a href="http://cocl.us/bottemNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/irypdxea2q4th88zu1o1tsd06dya10go.png" width = 750, align = "center"></a>

# 
# 
# # About the Authors:  
# 
#  [Joseph Santarcangelo]( https://www.linkedin.com/in/joseph-s-50398b136/) has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.

#  <hr>
# Copyright &copy; 2017 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).​
