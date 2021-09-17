import csv
import os
import numpy as np
import pandas as pd
import random

df = pd.DataFrame(index=np.arange(31), columns= ['Date', 'Name', 'Media', 'Muting', 'Host', 'CoHost', 'Attendant'])
bros = ['Jonah','David','Johnny','Jonathan', 'Edgar', 'Ricky']

# Yield successive n-sized
# chunks from l.
# def divide_chunks(l, n):

# # # looping till length l
# # 	for i in range(0, len(l), n): 
# # 		yield l[i:i + n]



def chunks(l, n):
#Yield n number of sequential chunks from l."""
	d, r = divmod(len(l), n)
	for i in range(n):
		si = (d+1)*(i if i < r else r) + d*(0 if i < r else i - r)
		yield l[si:si+(d+1 if i < r else d)]


# # How many elements each
# # list should have
# n = 3

# bros_chunked = list(divide_chunks(bros, n))

# for i in range(len(bros_chunked)):
# 	for x in bros_chunked:
#         print(x[i], end =' ')

#bros_shuffled = random.shuffle(bros)

# def assign():

#df['Name'] = [random.choice(bros) for i in df.Name]
sched = chunks(df.Name, 31)


print(sched)

#df.to_csv('/Users/leodgaray/Documents/congregation/Zoom Assignment Schedule.csv', index=False)

#print('Schedule created')  