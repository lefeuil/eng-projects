## Lab 4 code by Kay Burnham
# ID 20220414
# PCA: Question 1, corresponding to report part 1-6

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os 

dataset_path = os.path.join(os.path.dirname(__file__), 'dataset.csv')
dataset_full=pd.read_csv(dataset_path, delimiter=';')

# We want to take a subset of the dataset (the entire dataset is too large).

x = np.array(dataset_full.values[155750:156250, 6:18], dtype=float)
x_names=list(dataset_full.columns)[6:18]

print('feature shape: ', x.shape)
print('feature names: ', x_names)

# We can plot the 12 dimensions. 
plt.figure()
t=[i for i in range(x.shape[0])]
for k in range(len(x_names)):
 plt.plot(t, x[:, k], label=x_names[k])

plt.legend(loc='upper right')
plt.title('Feature visualization')
plt.savefig('fig1.pdf')

# Calculate the mean and standard deviation:
m_x = np.mean(x, axis=0)
s_x = np.std(x, axis=0)

# Perform normalization
x_bar = (x - m_x) / s_x

plt.figure()
t=[i for i in range(x_bar.shape[0])]
for k in range(len(x_names)):
 plt.plot(t, x_bar[:, k], label=x_names[k])

plt.legend(loc='upper right')
plt.title('Normalized feature visualization')
plt.savefig('fig2.pdf')




def pca(x):
     # Step 1: Mean-center the data
        # Calculate the mean and standard deviation:
     m_x = np.mean(x, axis=0)
     s_x = np.std(x, axis=0)

        # Perform normalization
     x_bar = (x - m_x) / s_x

     # Step 2: Compute the covariance matrix (use np.cov)
     x_cov = np.cov(x_bar, rowvar=False)

     # Step 3: Perform eigen decomposition (use np.linalg.eigh)
     x_eigval, x_eigvect = np.linalg.eigh(x_cov)

     # Step 4: Sort the eigenvalues AND eigenvectors in decreasing order
     # (Hint: use np.argsort on eigenvalues)
     idx = np.argsort(x_eigval)[::-1] 
     x_eigval = x_eigval[idx]          
     x_eigvect = x_eigvect[:, idx]

     # Step 5: Select the sorted eigenvectors as principal components (pcs)
     k = 2 #assuming 2 principal components (becomes 2D for plotting)
     pcs = x_eigvect[:, :k]

     # Step 6: Compute the variance explained by each principal component (explained)
     explained = x_eigval / np.sum(x_eigval) 

     # Step 7: Project the data onto principal component axes to obtain scores
     scores = np.dot(x_bar, pcs)

     return pcs, scores, explained


pcs, scores, explained = pca(x)

plt.figure()
plt.scatter(scores[:, 0], scores[:, 1], alpha=0.7)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA: 2D Projection of Data")
plt.savefig('fig4.pdf')

plt.figure()
plt.bar(range(1, len(explained) + 1), explained * 100, alpha=0.7)
plt.xlabel("Principal Component")
plt.ylabel("Variance Explained (%)")
plt.title("Explained Variance by PCs")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('fig5.pdf')

plt.figure()
cumulative_variance = np.cumsum(explained)
plt.bar(range(1, len(explained) + 1), cumulative_variance * 100, alpha=0.7)
plt.xlabel("Number of Principal Components")
plt.ylabel("Cumulative Variance Explained (%)")
plt.title("Cumulative Explained Variance")
plt.axhline(y=98, color='gray', linestyle='--', label="98% threshold")
plt.legend()
plt.grid(alpha=0.7)
plt.savefig('fig6.pdf')