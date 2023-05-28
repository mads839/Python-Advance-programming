#!/usr/bin/env python
# coding: utf-8

# In[7]:


#1. Create a function that transposes a 2D matrix.

def transpose_matrix(l):
    l2=[]
    for i in range (len(l[0])):
        l1=[]
        for j in range(len(l)):
            l1.append(l[j][i])
        l2.append(l1)
    return(l2)
        


# In[8]:


transpose_matrix([
  [5, 5],
  [6, 7],
  [9, 1]
]) 

#2. Create a function that determines whether a string is a valid hex code.
# A hex code must begin with a pound key # and is exactly 6 characters in length. Each character must be a digit from 0-9 or an alphabetic character from A-F. All alphabetic characters may be uppercase or lowercase.
# In[ ]:



def is_valid_hex_code(s):
    if len(s)==7 and s[0]=="#":
        for letter in s[1:]:
            if letter.lower() not in "abcdef" and  not letter.isdigit():                
                return False
            else:
                return True
        
    else:
        return False


# In[26]:


is_valid_hex_code("#CD5C5C") 


# In[27]:


is_valid_hex_code("#EAECEE")


# In[28]:


is_valid_hex_code("#CD5C58C") 

#3. Given a list of math equations (given as strings), return the percentage of correct answers as a string. Round to #the nearest whole number.
# In[ ]:




def mark_maths(l):
    count=0
    for i in l:
        l1=i.split("=")
        if(eval(l1[0])==int(l1[1])):
            count+=1
    return str(round((count/len(l))*100))+"%"


# In[42]:


mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"])


# In[39]:





# In[38]:


mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"])

# 5. From point A, an object is moving towards point B at constant velocity va (in km/hr). From point B, another object is moving towards point A at constant velocity vb (in km/hr). Knowing this and the distance between point A and B (in km), write a function that returns how much time passes until both objects meet.
# In[ ]:



def lets_meet(dis,vel1,vel2):
    time=(dis/(vel1+vel2))*60
    hours, seconds=divmod(time*60, 3600)
    minutes, seconds=divmod(seconds, 60)
    return str(round(hours))+"h "+str(round(minutes))+"min "+str(round(seconds))+"sec"


# In[58]:


lets_meet(100, 10, 30) 


# In[59]:


lets_meet(280, 70, 80) 


# In[ ]:




