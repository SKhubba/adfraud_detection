# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from pandas import Series, DataFrame, Panel

# Read in the sample training data frame (n = 100,000)
df = pd.read_csv("train_sample.csv")
df.head()

## TIME

# Start and end date of the range
min_date = pd.to_datetime(df['click_time']).min()
max_date = pd.to_datetime(df['click_time']).max()

# Create a time series from start to end of the range consisting of clicks per second
dates = pd.date_range(start=min_date, end=max_date, freq='S')
date_series = Series(0, index=dates).fillna(0)

click_df = df['click_time'].value_counts()
click_series = Series(click_df, index = pd.to_datetime(click_df.index))
final_series = pd.Series.align(date_series, click_series, join = 'left')[1].fillna(0)

# Start and end date of the range
min_date = pd.to_datetime(df['click_time']).min()
max_date = pd.to_datetime(df['click_time']).max()

# Create a time series from start to end of the range consisting of clicks per second
dates = pd.date_range(start=min_date, end=max_date, freq='S')
date_series = Series(0, index=dates).fillna(0)

click_df = df['click_time'].value_counts()
click_series = Series(click_df, index = pd.to_datetime(click_df.index))
final_series = pd.Series.align(date_series, click_series, join = 'left')[1].fillna(0)

# Plot the total clicks per second for the whole date range, as well as for 1 day

plt.subplot(221)
plt.plot(final_series, 'maroon')
plt.xlabel('Time (seconds)')
plt.ylabel('clicks')
plt.ylabel('clicks')
plt.title('Clicks per second in data sample')
plt.grid(True)

ax = plt.subplot(222)
ax.plot(final_series['2017-11-08 00:00:00':'2017-11-08 23:59:59'], 'orange')
myFmt = DateFormatter("%H:%M")
ax.xaxis.set_major_formatter(myFmt)
plt.xlabel('Time')
plt.ylabel('clicks')
plt.title('Clicks per second in data sample (11/8/2017)')
plt.grid(True)

plt.subplots_adjust(left = 1, right = 3, bottom = 0, top = 2)
plt.show()

# Collapse the series into 1 minute intervals
minute_series = final_series.resample('60S').sum()

# Plot the total clicks per second for the whole date range, as well as for 1 day
plt.subplot(221)
plt.plot(minute_series, 'teal')
plt.xlabel('Time (seconds)')
plt.ylabel('clicks')
plt.ylabel('clicks')
plt.title('Clicks per minute in data sample')
plt.grid(True)

ax = plt.subplot(222)
ax.plot(minute_series['2017-11-08 00:00:00':'2017-11-08 23:59:59'], 'violet')
myFmt = DateFormatter("%H:%M")
ax.xaxis.set_major_formatter(myFmt)
plt.xlabel('Time')
plt.ylabel('clicks')
plt.title('Clicks per minute in data sample (11/8/2017)')
plt.grid(True)

plt.subplots_adjust(left = 1, right = 3, bottom = 0, top = 2)
plt.show()

# Converted series to arrays to superimpose the lines
plt.plot(np.array(minute_series['2017-11-08 00:00:00':'2017-11-08 23:59:59']), 'violet')
plt.xlabel('Time')
plt.ylabel('clicks')
plt.title('Clicks per minute in data sample (11/8/2017 and 11/7/2017)')

plt.plot(np.array(minute_series['2017-11-07 00:00:00':'2017-11-07 23:59:59']), 'orange')