
# In[1]:

from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[37]:

# Get the SciPy data, courtesy of BeautifulSoup
r  = requests.get("https://conference.scipy.org/scipy2014/participate/presentations/")
data = r.text
soup = BeautifulSoup(data)

# Some lists to hold the scraped data
title = []
names = []
category = []

# There are 3 columns in the table: know which column the entry
# belongs to by its number, modulo 3
number = 0

for tr in soup.find_all('td'):
    if number % 3 == 0:
        title.append(str(tr.contents[0]))
    elif number % 3 == 1:
        names.append(str(tr.contents[0]))
    elif number % 3 == 2:
        category.append(str(tr.contents[0]))
    number +=1

title_s = pd.Series(title)    
names_s = pd.Series(names)
categories_s = pd.Series(category)

scipy_df = pd.DataFrame({'title':title_s,'presenter':names_s,'track':categories_s})

# Split presenters into first & last names
scipy_df['first_name'] = scipy_df.presenter.apply(lambda x: x.split(' ')[0])
scipy_df['last_name'] = scipy_df.presenter.apply(lambda x: x.split(' ')[1])
del scipy_df['presenter']

# Take a look at the DF
scipy_df.head()


# Out[37]:

#                                                    title   track first_name  \
#     0  airspeed velocity: tracking performance of Pyt...    gen2    Michael   
#     1                Neural Networks for Computer Vision     viz       Kyle   
#     2    A success story in using Python in a graduat...     eng       John   
#     3  Scientific Computing in the Undergraduate Mete...    edu2       Alex   
#     4  SociaLite: Python-integrated query language fo...  poster      Jiwon   
#     
#         last_name  
#     0  Droettboom  
#     1     Kastner  
#     2     Kitchin  
#     3     DeCaria  
#     4         Seo  

# In[41]:

scipy_df.groupby('track').count()


# Out[41]:

#              title  track  first_name  last_name
#     track                                       
#     astro        7      7           7          7
#     bioinfo      4      4           4          4
#     edu1         4      4           4          4
#     edu2         4      4           4          4
#     edu3         4      4           4          4
#     edu4         4      4           4          4
#     eng          4      4           4          4
#     gen1         4      4           4          4
#     gen2         4      4           4          4
#     gen3         4      4           4          4
#     gen4         4      4           4          4
#     geo          4      4           4          4
#     gis1         4      4           4          4
#     gis2         4      4           4          4
#     gis3         4      4           4          4
#     gis4         4      4           4          4
#     poster      42     42          42         42
#     soc          2      2           2          2
#     viz          8      8           8          8

# In[ ]:



