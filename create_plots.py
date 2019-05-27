# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

filename1 = sys.argv[1]
filename2 = sys.argv[2]

df1 = pd.read_csv(filename1, sep=' ', header=None, index_col=1,
           names = ['lang', 'page', 'views', 'bytes'])
df2 = pd.read_csv(filename2, sep=' ', header=None, index_col=1,
           names = ['lang', 'page', 'views', 'bytes'])

df1 = df1.sort_values(by=['views'], ascending=False)
print(df1)

df2 = df2.sort_values(by=['views'], ascending=False)
print(df2)

plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.title("Popularity Distribution")
plt.xlabel("Rank")
plt.ylabel("Views")
plt.plot(df1['views'].values)

plt.subplot(1, 2, 2)
final = pd.merge(df1, df2['views'], on='page')
print(final)
plt.title("Daily Correlation")
plt.xlabel("Day 1 Views")
plt.ylabel("Day 2 Views")
plt.scatter(final['views_x'].values, final['views_y'].values)
plt.xscale('log')
plt.yscale('log')

plt.savefig('wikipedia.png')
plt.show()
