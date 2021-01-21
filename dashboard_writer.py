# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:32:44 2020
@author: mayank.shinde
"""


import pygsheets
import os
import pandas as pd
import datetime
from datetime import timedelta
import boto3
from tempfile import NamedTemporaryFile

def downloadFileFromS3(bucket, path):
  s3 = boto3.resource('s3').Bucket(bucket)
  tmp = NamedTemporaryFile(delete=False)
  s3.download_fileobj(path, tmp)
  return tmp.name

print('FUNCTION DEFINED')

gc_cred_file = downloadFileFromS3('prod-datapl-r-scheduler','team/usa_revenue_analytics/mayank.shinde/usa-revenue-update.json')
print('CREDENTIALS READ')

gc = pygsheets.authorize(service_file=gc_cred_file, outh_nonlocal=True)
print('SHEETS AUTHORISED')

sh = gc.open_by_key('1hN_aVpaP-Fff-0JQRKOQLrqXw1LN48Q_X1e2EMHUtao')
print('SHEETS OPENED')

############################################### upload
wks1 = sh.worksheet_by_title("360_data_Jan")

print('TAB OPENED')

start1 = downloadFileFromS3('prod-datapl-r-scheduler','team/usa_revenue_analytics/mayank.shinde/prepayment_impact_analysis/US.csv')


df1 = pd.read_csv(start1)

wks1.clear()

df1.shape
df1.info()
df1.fillna(0,inplace=True)


wks1.set_dataframe(df1,(1,1))

print('DATA PASTED')