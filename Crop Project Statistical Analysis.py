#!/usr/bin/env python
# coding: utf-8

# # Student: Ronald Carter Jr.
# MS candidate in Applied Data Science & Analytics, Howard University Class of 2024
# 
# ### Class: Data Science for Social Impact, Spr.24
# 
# ### Professor: Ms.Berry
# 
# ### Project: Upov Crop Yieled and Production Project Analysis 
# 
# ### Group Research Question: 
# - How does membership in the UPOV affect crop yields for specific grains & cassava in East Africa
# - Focusing on UPOV member countries (Egypt, Kenya, and Tanzania) versus non-UPOV member countries in the region?
# 
# ### Notebook Focus: Statistical Analysis of Crop Yield and Production Values

# In[1]:


# Importing libraries  
import numpy as np 
import pandas as pd 


# In[2]:


# Importing cleaned df from previous notebook 
path ='/users/mariocart/Desktop/DS_SI/east_africa_final.csv'
east_africa = pd.read_csv(path)
east_africa.head()


# In[3]:


# Seperating Upov members from Non Upov members 
upov_members = east_africa[east_africa['Area'].isin(['Egypt', 'Kenya', 'United Republic of Tanzania'])]
non_upov_members = east_africa[~east_africa['Area'].isin(['Egypt', 'Kenya', 'United Republic of Tanzania'])]


# ## Statistical Analysis 
# 

# ## Important Reminder 
# - Yield & Production difference columns mean: difference from previous year 

# In[6]:


# Sorting the data based on yield difference column in descending order
yield_sorted_upov = upov_members.sort_values(by='Yield Difference', ascending=False)

# Displaying the top 10 rows of sorted data
yield_sorted_upov.head(10)


# In[7]:


# Sorting the data based on yield difference column in ascending order
yield_sorted_upov2 = upov_members.sort_values(by='Yield Difference', ascending=True)

# Displaying the bottom 10 rows of sorted data
yield_sorted_upov2.head(10)


# In[8]:


# Sorting the data based on production difference column in descending order
production_sorted_upov = upov_members.sort_values(by='Production Difference', ascending=False)

# Displaying the top 10 rows of sorted data
production_sorted_upov.head(10)


# In[9]:


# Sorting the data based on yield difference column in ascending order
production_sorted_upov2 = upov_members.sort_values(by='Production Difference', ascending=True)

# Displaying the bottom 10 rows of the sorted data
production_sorted_upov2.head(10)


# ## Repeating the same steps for Non Upov members in East Africa 
# 

# In[10]:


# Sorting the data based on yield difference column in descending order
yield_sorted_non_upov = non_upov_members.sort_values(by='Yield Difference', ascending=False)
# Displaying the top 10 rows of sorted data
yield_sorted_non_upov.head(10)


# In[11]:


# Sorting the data based on yield difference column in ascending order
yield_sorted_non_upov2 = non_upov_members.sort_values(by='Yield Difference', ascending=True)

# Displaying the bottom 10 rows of sorted data
yield_sorted_non_upov2.head(10)


# In[12]:


# Sorting the data based on production difference column in descending order
production_sorted_non_upov = non_upov_members.sort_values(by='Production Difference', ascending=False)

# Displaying the top 10 rows of the sorted data
production_sorted_non_upov.head(10)


# In[13]:


# Sorting the data based on production difference column in ascending order
production_sorted_non_upov2 = non_upov_members.sort_values(by='Production Difference', ascending=True)

# Displaying the bottom 10 rows of sorted data
production_sorted_non_upov2.head(10)


# ## Comparision Analysis:
# ## Reminder: 
# - East Africa Upov Members: Kenya, Tanzania, Egypt
# - East Africa Non Upov Members(from ones we selected: Burundi, Comoros, Madagascar, Malawi, Mauritius, Mozambique, Rwanda, Seychelles, Somalia, Uganda, Zambia, Zimbabwe
# 
# 
# ## Summary of Top Ten Yield differences for Upov Members (100 g/ha)
# 1. Kenya,Cassava(1984-1985): 77,049
# 2. Kenya,Cassava(2007-2008): 63,173
# 3. Kenya,Cassava(2010-2011): 59,788
# 4. Tanzania,Cassava(2017-2018): 51,644 
# 5. Kenya,Cassava(1982-1983): 48,000
# 6. Kenya,Cassava(1980-1981): 40,166
# 7. Tanzania,Cassava(1989-1990): 39,693
# 8. Kenya,Cassava(2017-2018): 38,177
# 9. Tanzania,Cassava(1976-1977): 33,858
# 10. Kenya,Cassava(2003-2004): 31,985
# ## Summary of Top Ten Yield differences for Non Upov Members (100 g/ ha)
# 1. Malawi,Cassava (1999-2000): 100,042
# 2. Zambia, Cassava (2015-2016): 97,030
# 3. Mauritius Cassava(1965-1966): 87,087
# 4. Seychelles, Cassava(1990-1991): 82,151
# 5. Rwanda, Cassava (2020-2021): 79,865
# 6. Mauritius, Cassava (1980-1981): 78,000
# 7. Zambia, Cassava (2016-2017): 75,522
# 8. Rwanda, Cassava (1963-1964): 75,331
# 9. Zambia, Cassava (2014-2015): 74,016
# 10. Rwanda, Cassava (2009-2010): 71,292
# _____________________________________________________________________________________________________________
# 
# ## Summary of Bottom Ten Yield differences from Upov Members (100 g/ha)
# 1. Kenya,Cassava(1981-1982): - 67,048
# 2. Kenya,Cassava(2009-2010): - 63,910
# 3. Kenya,Cassava(1983-1984): - 50,000
# 4. Kenya,Cassava(1985-1986): - 41,784	
# 5. Tanzania,Cassava(2002-2003): - 32,658
# 6. Kenya,Cassava(1999-2000): - 32,652
# 7. Kenya,Cassava (2020-2021): - 27,269
# 8. Egypt, Maize(corn)(2018-2019): - 25,649	
# 9. Kenya,Cassava(2006-2007): - 21,671
# 10. Kenya,Cassava (2008-2009): -20,927
# ## Summary of Bottom Ten Yield differences from Non Upov Members (100 g/ha)
# 1. Mauritius,Cassava (1981-1982): - 116,667
# 2. Uganda, Cassava (2007-2008): - 56,582
# 3. Rwanda, Cassava (1979-1980): - 44,857
# 4. Rwanda, Cassava (1987-1988): - 44,462
# 5. Mauritius, Cassava (2004-2005): - 40,357
# 6. Burundi, Cassava (2016-2017): - 38,409
# 7. Mauritius, Cassava (2001-2002): - 35,385
# 8. Zambia, Cassava (2018-2019): - 30,322
# 9. Mauritius, Cassava (1979-1980): - 30,222	
# 10. Malawi, Cassava (1982-1983): -29,608
# _____________________________________________________________________________________________________________
# 
# ## Summary of Top Ten Production differences for Upov Members (Tonnes)
# 1. Tanzania,Cassava(2017-2018): 4,346,952
# 2. Egypt, Maize (corn)(2018-2019): 2,481,904
# 3. Tanzania,Maize (corn)(2003-2004): 2,037,400
# 4. Tanzania, Maize (corn)(2007-2008): 1,781,710
# 5. Tanzania, Maize (corn)(2003-2002): 1,755,610
# 6. Tanzania, Maize (corn)(2009-2010): 1,406,870
# 7. Tanzania, Maize (corn)(1994-1995): 1,388,600
# 8. Tanzania, Maize (corn)(2013-2014): 1,380,847
# 9. Tanzania,Cassava(1974-1975): 1,300,760
# 10. Tanzania,Cassava(1982-1983): 1,236,000
# ## Summary of Top Ten Production differences for Non Upov Members (Tonnes)
# 1. Mozambique, Cassava (2002-2003): 2,703,857
# 2. Mozambique, Cassava (2017-2018): 2,479,023
# 3. Malawi, Cassava (1999-2000): 1,888,187
# 4. Mozambique, Cassava (2008-2009): 1,831,331
# 5. Uganda, Maize(Corn)(2019-2020): 1,800,000
# 6. Zimbabwe, Maize(Corn)(1992-1993): 1,701,103
# 7. Zimbabwe, Maize(Corn)(1984-1985): 1,695,197
# 8. Uganda, Cassava(1998-1999): 1,671,000
# 9. Uganda, Cassava(2017-2018): 1,660,971
# 10. Zambia, Cassava(2016-2017): 1,472,338.35
# _______________________________________________________________________________________________________________
# 
# 
# ## Summary of Bottom Ten Production differences for Upov Members (Tonnes)
# 1. Egypt, Maize (corn)(2017-2018): - 3,431,399
# 2. Tanzania, Maize (corn)(2008-2009): - 2,114,510
# 3. Tanzania, Maize (corn)(2002-2003): - 1,794,450
# 4. Tanzania, Maize (corn)(2004-2005): - 1,519,760
# 5. Tanzania,Cassava(2009-2010): - 1,368,500
# 6. Tanzania,Cassava(1986-1987): - 1,286,400
# 7. Tanzania,Cassava(2019-2020): - 1,264,608.54
# 8. Tanzania,Cassava (1994-1995): - 1,240,400
# 9. Tanzania,Cassava(2002-2003): - 1,214,050
# 10. Tanzania,Cassava(20016-2017): 1,176,186.35
# ## Summary of Bottom Ten Production differences for Non Upov Members (Tonnes)
# 1. Mozambique,Cassava (2001-2002): - 2,528,547
# 2. Uganda, Cassava (2007-2008): - 2,097,381
# 3. Mozambique,Cassava (2011-2012): -1,901,000
# 4. Malawi, Cassava (2001-2002): -1,822,218 
# 5. Uganda, Maize (Corn)(2020-2021): - 1,760,000
# 6. Uganda, Cassava (2018-2019): - 1,730,231
# 7. Mozambique, Cassava (2004-2005): - 1,630,339
# 8. Zimbabwe, Maize(Corn)(1986-1987): -1,414,760
# 9. Zimbabwe, Maize(Corn)(1972-1973): - 1,361,809
# 10. Zimbabwe, Maize(Corn)(1994-1995): -1,224,321

# ## Investigating the difference in Yield and Production values before and after Upov membership for each country (Kenya, Tanzania, Egypt)

# ## Kenya

# In[21]:


# Filtering data to Kenya before Upov membership
kenya_before_upov = upov_members[(upov_members['Area'] == 'Kenya') & (upov_members['Year'] < 1999)]

# Filtering data to Kenya after Upov membership
kenya_after_upov = upov_members[(upov_members['Area'] == 'Kenya') & (upov_members['Year'] >= 1999)]

# Calculating the average yield difference for Kenya before membership
ken_avg_yield_diff_before = kenya_before_upov['Yield Difference'].mean()

# Calculating the average yield difference for Kenya after membership
ken_avg_yield_diff_after = kenya_after_upov['Yield Difference'].mean()


# In[22]:


# Inspecting average yield difference before Upov membership for Kenya 
ken_avg_yield_diff_before


# In[23]:


# Inspecting average yield difference after Upov membership for Kenya 
ken_avg_yield_diff_after


# In[31]:


# Calculating the average yield difference for Kenya before membership
ken_avg_prod_diff_before = kenya_before_upov['Production Difference'].mean()

# Calculating the average yield difference for Kenya after membership
ken_avg_prod_diff_after = kenya_after_upov['Production Difference'].mean()


# In[32]:


# Inspecting average production difference before Upov membership for Kenya 
ken_avg_prod_diff_before


# In[33]:


# Inspecting average yield difference after Upov membership for Kenya 
ken_avg_prod_diff_after


# ## Tanzania

# In[25]:


# Filtering data to Kenya before Upov membership
tanzania_before_upov = upov_members[(upov_members['Area'] == 'United Republic of Tanzania') & (upov_members['Year'] < 2015)]

# Filtering data to Kenya after Upov membership
tanzania_after_upov = upov_members[(upov_members['Area'] == 'United Republic of Tanzania') & (upov_members['Year'] >= 2015)]

# Calculating the average yield difference for Kenya before membership
tan_avg_yield_diff_before = tanzania_before_upov['Yield Difference'].mean()

# Calculating the average yield difference for Kenya after membership
tan_avg_yield_diff_after = tanzania_after_upov['Yield Difference'].mean()


# In[26]:


# Inspecting average yield difference before Upov membership for Tanzania
tan_avg_yield_diff_before


# In[27]:


# Inspecting average yield difference after Upov membership for Tanzania
tan_avg_yield_diff_after


# In[34]:


# Calculating the average production difference for Tanzania before membership
tan_avg_prod_diff_before = tanzania_before_upov['Production Difference'].mean()

# Calculating the average yield difference for Kenya after membership
tan_avg_prod_diff_after = tanzania_after_upov['Production Difference'].mean()


# In[35]:


# Inspecting average production difference before Upov membership for Tanzania
tan_avg_prod_diff_before


# In[36]:


# Inspecting average production difference after Upov membership for Tanzania
tan_avg_prod_diff_after


# ## Egypt

# In[28]:


# Filtering data to Kenya before Upov membership
egypt_before_upov = upov_members[(upov_members['Area'] == 'Egypt') & (upov_members['Year'] < 2019)]

# Filtering data to Kenya after Upov membership
egypt_after_upov = upov_members[(upov_members['Area'] == 'Egypt') & (upov_members['Year'] >= 2019)]

# Calculating the average yield difference for Kenya before membership
egypt_avg_yield_diff_before = egypt_before_upov['Yield Difference'].mean()

# Calculating the average yield difference for Kenya after membership
egypt_avg_yield_diff_after = egypt_after_upov['Yield Difference'].mean()


# In[29]:


# Inspecting average yield difference before Upov membership for Egypt
egypt_avg_yield_diff_before


# In[30]:


# Inspecting average yield difference after Upov membership for Egypt
egypt_avg_yield_diff_after


# In[37]:


# Calculating the average production difference for Egypt before membership
egypt_avg_prod_diff_before = egypt_before_upov['Production Difference'].mean()

# Calculating the average production difference for Egypt after membership
egypt_avg_prod_diff_after = egypt_after_upov['Production Difference'].mean()


# In[38]:


# Inspecting average production difference before Upov membership for Egypt
egypt_avg_prod_diff_before


# In[39]:


# Inspecting average production difference after Upov membership for Egypt
egypt_avg_prod_diff_after


# ## Summary & Work Moving forward 
# - This statistical summary give us good insight into the changes in yield and production values for our crops of interest from 1961-2021 however there are some limitations as well:
# - Uneven years of membership across countries: Because each of the Upov countries in East Africa joined Upov at different times(1999,2015,2019). This can possibly skew the average yield & production difference calculations.
# - Visualizations and researching historical context can help us understand the over picture of changes in yield and production for our crops of interest across consecutive years for ex:
# - Historical reseach ideas :
# 1. Changes in agricultural practices & technology
# 2. Environmental factors 
# 3. Weather conditions
# 4. Changes in economy
# 5. Different policy changes
# 6. Global market trends
# 7. Trade agreements
# 8. Natural disasters
# 9. Wars
# - This can help us to capture the full range of variability within each period and understand the data and changes better.
# - We can also look into using additional statistical measures like median, quartiles and standard deviation.
# - Continue dialogue about limiation factors and brainstorm ideas
# - The goal is to perform thorough analyses using a holistic approach.
# ## Work moving forward 
# - Have group member review this notebook 
# - Create some data stories from these statistics that can help guide our visuals
# - Visualizations/ Presentation 
# - Historical research 
# - Paper 
# - Modeling 
