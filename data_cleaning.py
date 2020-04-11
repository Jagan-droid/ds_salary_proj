#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:44:47 2020

@author: jagannathan
"""
import pandas

df = pd.read_csv("/Users/jagannathan/Documents/ds_salary_proj/datascience_jobs.csv")

#Salary Parsing


#Company Name Text Only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis = 1) 
print(df.columns)

#State Field - With Chennai the difference is not seen here. However, in the American version State Names come out separately with this statement
df['job_state'] = df['Location'].apply(lambda x:x.split(',')[0])
print(df.columns)
df.job_state.value_counts()

#Checking If HQ is in the same state?
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#HQ Country
df['hq_country'] = df['Headquarters'].apply(lambda x: x.split(',')[-1])
print(df.columns)

#Age of Company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2020 - x)

#Parsing of Job Description (If certain tool skills like Python, R-studio, AWS, Excel are mentioned)

#If Python is a requirement in the JD
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

#R-studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#Spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark_yn.value_counts()

#AWS
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_yn.value_counts()

#Excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel_yn.value_counts()

df.columns

#Removing unnecessary columns from Ken Jee's video(Unnamed: 0)/ The column is already not present here. So, I have deleted an erroneous column 'job_state'
df_out = df.drop(['job_state'], axis=1)
df_out.columns

#Saving the Cleaned data frame as csv file
df_out.to_csv("/Users/jagannathan/Documents/ds_salary_proj/jobdata_cleaned.csv", index=False)

#Validating the saved file
pd.read_csv("/Users/jagannathan/Documents/ds_salary_proj/jobdata_cleaned.csv")
