#!/usr/bin/env python
# coding: utf-8

# In[10]:


1+1


# In[9]:


print ("hello")


# In[2]:


mystring = "Hello world"


# In[3]:


mystring[6]


# In[4]:


name = "Sam"


# In[5]:


name.capitalize()


# In[6]:


name.upper()


# In[7]:


name * 3


# In[8]:


"my name is " + name


# In[14]:


last_letters = name[1:]


# In[15]:


"p" = last_letters


# In[16]:


last_letters


# In[17]:


"p" + last_letters


# In[34]:


letters = " asdfs fgsdsdf  dfgsdfgdsf"


# In[26]:


letters * 10


# In[28]:


letters.swapcase()


# In[35]:


letters.split()


# In[37]:


letters.split("f")


# In[40]:


print('The {q} {b} {f}' .format(f="fox",b="brown" ,q="quick"))


# In[45]:


print("this is a 'string' {2} {1} {0}" .format("fox","brown","quick") )


# In[48]:


result = 100/777


# In[49]:


result


# In[60]:


print ("the result was {r:1.7f}" .format(r=result))


# In[61]:


myset = set()


# In[62]:


myset


# In[65]:


myset.add(1)


# In[66]:


myset.pop()


# In[67]:


myset


# In[68]:


myset.add(1)


# In[69]:


myset


# In[70]:


myset.add(2)


# In[71]:


myset


# In[76]:


set1 =("mississippi")


# In[77]:


set1


# In[84]:


True


# In[85]:


False


# In[86]:


type(False)


# In[87]:


2 > 4


# In[88]:


2==4


# In[89]:


b = None


# In[90]:


b


# In[130]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'helllo this is a text file\nthis is the 2nd line\nthis is the 3rd line')


# In[94]:


myfile = open("myfile.txt")


# In[95]:


pwd


# In[96]:


clear


# In[97]:


ls


# In[98]:


ls -a 


# In[104]:


cd "/Users/dell/Downloads/My Python Stuff"


# In[106]:


pwd


# In[109]:


nano myfile.txt


# In[110]:


pwd


# In[131]:


myfile = open("myfile.txt")


# In[133]:


myfile.read()


# In[153]:


myfile.seek(0)


# In[154]:


myfile.readlines()


# In[155]:


myfile.close()


# In[156]:


with open("myfile.txt",mode="r") as myfile:
    content = myfile.read()


# In[157]:


content


# In[ ]:




