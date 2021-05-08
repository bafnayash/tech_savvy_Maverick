# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:09:40 2021

@author: Yash
"""

import numpy as np
import pandas as pd
from math import ceil, isnan

import matplotlib.pyplot as plt
import seaborn as sns
from pickle import load, dump
from sklearn import preprocessing

import folium
import geopy

data_frame = pd.read_csv("data_frame.csv", index_col = 0)
coorelation_df = pd.read_csv("coorelation_df.csv", index_col = 0)
purchase_df = pd.read_csv("purchase_df.csv", index_col = 0)
sim_df = pd.read_csv("sim_df.csv", index_col = 0)

with open("index_to_material.pkl", "rb") as f:
    index_to_material = load(f)

with open("wholesaler_loc.pkl", "rb") as f:
    wholesaler_loc = load(f)

with open("cluster_members.pkl", "rb") as f:
    cluster_members = load(f)

with open("maco_per_hl.pkl", "rb") as f:
    maco_per_hl = load(f)


def product_list(user_id):
  product_bought = []
  for i in range(purchase_df.shape[1]-1):
    #print(index_to_material[i])
    val = purchase_df._get_value(user_id, str(index_to_material[i]))
    #print("Done")
    if(val != 0):
      product_bought.append(index_to_material[i])
  return product_bought

def story_display(cluster_pred):
  x, y = "Latitude", "Longitude"
  size = "Total_HL"
  popup = "MACO"
  data = data_frame.copy()
  
  scaler = preprocessing.MinMaxScaler(feature_range = (2, 20))
  data["size"] = scaler.fit_transform(data[size].values.reshape(-1,1)).reshape(-1)

  scaler = preprocessing.MinMaxScaler(feature_range = (0, 100))
  data["popup"] = scaler.fit_transform(data[popup].values.reshape(-1,1)).reshape(-1)

  map = folium.Map(location = (47, 3), tiles = "cartodbpositron", zoom_start = 5)

  for i, row in data.iterrows():
    if(row["Cluster"] == cluster_pred):
      #print(row['Cluster'], row[x], row[y])
      folium.CircleMarker(location = [row[x], row[y]], popup = str("{:.2f}".format(row["popup"])), 
                          fill = True, radius = row["size"]).add_to(map)
                          
  return map


def predict(user_id):
  temp = wholesaler_loc[str(user_id)].split(", ")
  #x = float(temp[0])
  #y = float(temp[1])
  #print(x, y)
  #print(data_frame[data_frame['ID']==user_id])
  #print(len(data_frame.index[data_frame['ID']==user_id].to_list()))
  cluster_pred = data_frame._get_value(data_frame.index[data_frame['ID']==user_id].to_list()[0], "Cluster")     #model.predict([[x, y]])
  #print(cluster_pred)
  map_ = story_display(cluster_pred)
  possible_users = []
  for i in cluster_members[int(cluster_pred)]:
    if(i == user_id):
      continue
    similarity = sim_df.iloc[sim_df.columns.get_loc(str(user_id))-1, sim_df.columns.get_loc(str(i))]
    #print(similarity)
    possible_users.append([similarity, i])

  #print("Done")
  possible_users = sorted(possible_users, reverse = True)
  #print("Done")
  product_bought = product_list(user_id)
  possible_recomm = []
  
  for i in range(5):
    temp = product_list(possible_users[i][1])
    for j in temp:
      if(j not in set(product_bought) and j not in set(item[1] for item in possible_recomm)):
        possible_recomm.append([maco_per_hl[j], j])

  possible_recomm = sorted(possible_recomm, reverse = True)
  #print(possible_recomm)

  recommend = []

  for i in range(15):
    recommend.append(possible_recomm[i][1])
  
  amount = coorelation_df._get_value(user_id, "Mean")  
  return [amount, recommend, map_]

#amount, recommendations, map_ = predict(29606863)
#print(amount, recommendations)
#map_