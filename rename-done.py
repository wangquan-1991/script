#!/usr/bin/env python
# coding: utf-8

# In[20]:


import os


# In[21]:


folder_name = 'ttt'


# In[22]:


dir_list = os.listdir(folder_name)


# In[23]:


retval = os.getcwd()


# In[5]:


retval


# In[19]:


for folder in dir_list:
    target_path = retval+'/ttt/'+folder
    #print(target_path)
    floder_name = target_path.split('/')[-1] 
    #print(floder_name)
    files_name = os.listdir(target_path)
    #print(files_name)
    for folder2 in list(files_name):
        target2_path = target_path+'/'+folder2
        #print(target2_path)
        folder2_name = target2_path.split('/')[-1]
        print(folder2_name)
        #print(files)
        os.chdir(target2_path)
        files = os.listdir(target2_path)
        #print(files)
        for name in files:
            os.rename(name,folder2_name+'-'+name)
            print(name)





