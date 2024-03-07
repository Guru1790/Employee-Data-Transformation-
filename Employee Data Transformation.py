#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd


# In[2]:


input_file_path = "C:\\Users\\91762\\Downloads\\input.csv"
df = pd.read_csv(input_file_path)


# In[3]:


df.head()


# In[5]:


# Sort DataFrame by employee and effective date
df.sort_values(by=['Employee Code', 'Date of Joining'], inplace=True)


# In[6]:


# Create a new DataFrame for transformed data
transformed_df = pd.DataFrame(columns=['Employee Code', 'Effective Date', 'End Date', 'Compensation', 'Review', 'Engagement'])


# In[13]:


# Iterate through rows to transform data
for index, row in df.iterrows():
    # Initialize variables
    employee_id = row['Employee Code']
    effective_date = row['Date of Joining']
    end_date = row['Date of Exit']

    # Compensation
    compensation = row['Compensation']
    compensation_date = row['Date of Joining']
    transformed_df = transformed_df.append({'Employee Code': employee_id, 'Effective Date': effective_date, 'End Date': end_date, 'Compensation': compensation}, ignore_index=True)
# Review 1
    review_1 = row['Review 1']
    review_1_date = row['Review 1 date']
    if not pd.isna(review_1) and not pd.isna(review_1_date):
        transformed_df = transformed_df.append({'Employee Code': employee_id, 'Effective Date': review_1_date, 'End Date': end_date, 'Review': review_1}, ignore_index=True)

    # Review 2
    review_2 = row['Review 2']
    review_2_date = row['Review 2 date']
    if not pd.isna(review_2) and not pd.isna(review_2_date):
        transformed_df = transformed_df.append({'Employee Code': employee_id, 'Effective Date': review_2_date, 'End Date': end_date, 'Review': review_2}, ignore_index=True)
 # Engagement 1
    engagement_1 = row['Engagement 1']
    engagement_1_date = row['Engagement 1 date']
    if not pd.isna(engagement_1) and not pd.isna(engagement_1_date):
        transformed_df = transformed_df.append({'Employee Code': employee_id, 'Effective Date': engagement_1_date, 'End Date': end_date, 'Engagement': engagement_1}, ignore_index=True)

    # Engagement 2
    engagement_2 = row['Engagement 2']
    engagement_2_date = row['Engagement 2 date']
    if not pd.isna(engagement_2) and not pd.isna(engagement_2_date):
        transformed_df = transformed_df.append({'Employee Code': employee_id, 'Effective Date': engagement_2_date, 'End Date': end_date, 'Engagement': engagement_2}, ignore_index=True)


# In[14]:


# Fill missing values with the most recent past record for the same employee
transformed_df.fillna(method='ffill', inplace=True)


# In[15]:


# Assign a far-future date for the latest record
transformed_df.loc[transformed_df['End Date'].isna(), 'End Date'] = '2100-01-01'


# In[16]:


# Write the transformed data to a new CSV file
output_file_path = "C:\\Users\\91762\\Downloads\\output.csv"
transformed_df.to_csv(output_file_path, index=False)


# In[ ]:




