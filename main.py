import json
import numpy as np
import pandas as pd
import sys


assert(len(sys.argv) > 1)
json_path = sys.argv[1]
passenger_column = "S12_025"

df = []

for row in json.load(open(json_path))['features']:
    props = row['properties']
    center_coor = np.mean(row['geometry']['coordinates'], axis=0)
    df.append([center_coor[0], center_coor[1], props[passenger_column]])
    
df = pd.DataFrame(data=df, columns=['longitude', 'latitude', 'passenger'])
df.to_csv('output.csv')