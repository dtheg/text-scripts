import csv
import os
import numpy as np
import pandas as pd
import random

df = pd.DataFrame(index=np.arange(31), columns= ['Date', 'Name', 'Media', 'Muting', 'Host', 'CoHost', 'Attendant'])
bros = ['Jonah','David','Johnny','Jonathan', 'Edgar', 'Ricky']


df['Name'] = [random.choice(bros) for i in df.Name]


print(df)

#df.to_csv('/Users/leodgaray/Documents/congregation/Zoom Assignment Schedule.csv', index=False)

#print('Schedule created')  