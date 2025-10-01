## Lab 4 code by Kay Burnham
# ID 20220414
# Feature Extraction: Question 2, corresponding to report part 7

import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np
import os 

dataset_path = os.path.join(os.path.dirname(__file__), 'raw_accelerometer_dataset.csv')

if __name__=='__main__':

    raw_data=pd.read_csv(dataset_path, delimiter=',')

    # Display column names
    print(raw_data.columns)

    # Fetch unique activity classes
    classes = raw_data['Class'].unique()
    print(classes)

    # Visualize the x-axis of the accelerometer data for all available classes

    ##X AXIS 
    fig, axes = plt.subplots(len(classes), 1, figsize=(4, 2 * len(classes)))
    fig.suptitle('Accelerometer X-axis', fontsize=12)

    for i, task in enumerate(classes):
        # Fetch rows belonging to a particular class
        selected_task = raw_data[raw_data['Class'] == task]
        
        # Select the axis (X=2, Y=3, Z=4)
        signal = selected_task.iloc[:, 1].values  # Second column (X-axis)
        
        # Plot a small segment
        axes[i].plot(signal[:5000])
        axes[i].set_ylabel(task, fontsize=12)
    axes[-1].set_xlabel('time', fontsize=12)
    plt.savefig('fig7x.pdf')

    ## Y AXIS
    fig, axes = plt.subplots(len(classes), 1, figsize=(4, 2 * len(classes)))
    fig.suptitle('Accelerometer Y-axis', fontsize=12)

    for i, task in enumerate(classes):
        # Fetch rows belonging to a particular class
        selected_task = raw_data[raw_data['Class'] == task]
        
        # Select the axis (X=2, Y=3, Z=4)
        signal = selected_task.iloc[:, 2].values  # 3rd column (Y-axis)
        
        # Plot a small segment
        axes[i].plot(signal[:5000])
        axes[i].set_ylabel(task, fontsize=12)

    axes[-1].set_xlabel('time', fontsize=12)
    plt.savefig('fig7y.pdf')

    ## Z AXIS
    fig, axes = plt.subplots(len(classes), 1, figsize=(4, 2 * len(classes)))
    fig.suptitle('Accelerometer Z-axis', fontsize=12)

    for i, task in enumerate(classes):
        # Fetch rows belonging to a particular class
        selected_task = raw_data[raw_data['Class'] == task]
        
        # Select the axis (X=2, Y=3, Z=4)
        signal = selected_task.iloc[:, 3].values  # 4th column (Z-axis)
        
        # Plot a small segment
        axes[i].plot(signal[:5000])
        axes[i].set_ylabel(task, fontsize=12)
        
    axes[-1].set_xlabel('time', fontsize=12)
    plt.savefig('fig7z.pdf')

    plt.show()
