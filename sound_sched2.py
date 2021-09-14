import csv
import os
import numpy as np
import pandas as pd
import random

df = pd.DataFrame(index=np.arange(31), columns= ['Date', 'Name', 'Media', 'Muting', 'Host', 'CoHost', 'Attendant'])
bros = ['Jonah','David','Johnny','Jonathan', 'Edgar', 'Ricky']

# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):

# looping till length l
	for i in range(0, len(l), n): 
		yield l[i:i + n]

# How many elements each
# list should have
n = 3

bros_chunked = list(divide_chunks(bros, n))

# for i in range(len(bros_chunked)):
# 	for x in bros_chunked:
#         print(x[i], end =' ')


bros_shuffled = random.choice(bros_chunked)

# def assign():

df['Name'] = [bros_shuffled for Name in df.Name]
# assign()


print(df)

#df.to_csv('/Users/leodgaray/Documents/Zoom Assignment Schedule.csv', index=False)

#print('Schedule created')  
