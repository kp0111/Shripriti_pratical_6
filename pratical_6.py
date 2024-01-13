#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

# Sample data
languages = ['Python', 'Java', 'JavaScript', 'C#', 'PHP', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create a bar chart
plt.bar(languages, popularity, color='skyblue')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')
plt.show()


# In[2]:


import matplotlib.pyplot as plt

# Sample data
languages = ['Python', 'Java', 'JavaScript', 'C#', 'PHP', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create a pie chart
plt.pie(popularity, labels=languages, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Popularity of Programming Languages')
plt.show()


# In[ ]:




