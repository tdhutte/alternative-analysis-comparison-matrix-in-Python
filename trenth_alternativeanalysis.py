# -*- coding: utf-8 -*-
"""TrentH_AlternativeAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-UTTVzeRlYgyoTLzkVu3oHrMMW-FeAyQ
"""

import pandas as pd

#create a datagrame for our Alternative Analysis
AA=pd.DataFrame(columns=['criteria','weight','ratingA','ratingB','scoreA','scoreB'])
print(AA)

# first step: identify a set of criteria

AA['criteria']=['risk','ROI', 'feasibility', 'customer satisfaction', 'strategic alignment']
print(AA)

# step 2: is to assign weights
# weights show relative importance of each criterion
# the weights should add up to 1 or 100

AA['weight']=[0.1,0.15,0.3,0.15,0.3]
print(AA)

# step 3: rate each alternative across all criteria
# choose a scale: 1-3, 1-5, ... etc
# higher number: an alternative is doing better regarding the given criterion

AA['ratingA']=[4,1,2,1,5]
AA['ratingB']=[3,4,2,3,2]

# step 4: calculate partial scores by ratings*weights
# using iterrows is a bad idea - called an anti pattern. for small data frame, its ok

for index, row in AA.iterrows():
  AA['scoreA'][index]=row['weight']*row['ratingA']
  AA['scoreB'][index]=row['weight']*row['ratingB']

print(AA)

# step 5: add up partial scores to get a total score
# the alternative with the highest total score should be proposed/is the winner

totalScoreA=0
totalScoreB=0

for index, row in AA.iterrows():
  totalScoreA+=row['scoreA']
  totalScoreB+=row['scoreB']

print('The total score for alternative A is {:.2f} and for alternative B is {:.2f}'.format(totalScoreA,totalScoreB))