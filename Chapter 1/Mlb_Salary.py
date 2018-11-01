import pandas as pd
import numpy as np
import csv

with open('mlb.txt','r') as mlb:#chercher le fichier dans le foutoir

    #read the file mlb.txt
    file = mlb.readlines()
    print(file)

    #define the lists to put all the data into by column
    play = []
    team = []
    pos = []
    sal = []

    #split the data from the tabulation as they appear in the .readlines() method
    for i in file:
        a,b,c,d = i.split('\t')
        play.append(a)
        team.append(b)
        pos.append(c)
        sal.append(d)


    #regroup the data in a list of 4 dimension tuples
    res = zip(play,team,pos,sal)
    result = list(res)
    print(result)

    #put all the data directly ordered in a csv file
    with open('mlb_csv.csv','w') as mlbc:
        mlbcWriter = csv.writer(mlbc)
        for i in result:
            mlbcWriter.writerow(i)

        mlbc.close()
