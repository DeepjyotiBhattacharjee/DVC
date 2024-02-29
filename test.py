import pandas as pd

dataset = [
    {'name':'Deep',
     'age':29,
     'city':'siliguri'},

    {'name':'Ankita',
     'age':28,
     'city':'siliguri'},

    {'name':'Krish',
     'age':35,
     'city':'Bangalore'},

     {
         'name':'Caspy',
         'age':6,
         'city':'Bangalore'
     },
     {
         'name':'Sunny',
         'age':40,
         'city':'Bhopal'
     }
]

df = pd.DataFrame(dataset)

df.to_csv("data/data.csv",index=False)