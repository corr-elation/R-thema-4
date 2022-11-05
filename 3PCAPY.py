from sklearn import datasets
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import csv
from math import fabs

## csv data ##
data= pd.read_csv('/Users/vasileioskogkos/Documents/MSc ASssignments/Big Data/winequality-white.csv',sep=";", header=0)
print(data)
print(data.dtypes)

pcadata = data.loc[:, :"alcohol"]
print(pcadata)
variables = []

## PCA ##
pca = decomposition.PCA(n_components=11)
pca.fit(pcadata)
transdata= pca.transform(pcadata)
print('Wines_Transformed')
print(transdata)
cov_mat = np.cov(transdata)

## eigenvectors ##
eigen = []
z = 0
for eigenvector in pca.components_:
z += 1
print(f"Eigenvector {z} : {eigenvector}")
eigen.append(eigenvector)
variables = []
    
for col in pcadata.columns:
variables.append(col)
print(variables)

for i in range(len(eigen)):
    print(f'New variable {i + 1}= ')
for j in range(len(variables)):
    if eigen[i][j] >= 0:
        print(f'+({eigen[i][j]} * {variables[j]})',)
    else:
        print(f'-({fabs(eigen[i][j])} * {variables[j]})',)
print('\n')

## eigenvalues ##
for i in range(len(pca.explained_variance_)):
print(f"λ{i+1}: {pca.explained_variance_[i]}")

## variance ratio ##
for i in range(len(pca.explained_variance_ratio_)) :
print(f"The variance ratio for λ{i+1} is {pca.explained_variance_ratio_[i]}")


















