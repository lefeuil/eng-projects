## Lab 4 code by Kay Burnham
# ID 20220414
# Feature Extraction: Question 2, corresponding to report part 7

import pandas as pd
import numpy as np
import scipy as sp
import os 

dataset_path = os.path.join(os.path.dirname(__file__), 'raw_accelerometer_dataset.csv')

def extract_features(filename, 
                     segment_size):

    # Read raw data
    raw_data = pd.read_csv(filename, delimiter=',')

    # Initialize parameters
    feature_set = pd.DataFrame()
    event = 0
    classes = raw_data['Class'].unique()

    for task, class_name in enumerate(classes):
        # Filter data for current class/activity
        class_data = raw_data[raw_data['Class'] == class_name].iloc[:, 1:4]
        
        # Create group IDs
        num_samples = len(class_data)
        group_id = np.repeat(np.arange(event, event + np.ceil(num_samples/segment_size)), 
                            segment_size)[:num_samples]
        event += len(np.unique(group_id))
        
        class_data['group_id'] = group_id
        
        # Initialize feature containers
        features = []

        
        # Calculate features per segment
        for g_id, group in class_data.groupby('group_id'):
            data = group.iloc[:, :3]

            # Normalize data for entropy 
            # Calculate the mean and standard deviation:
            m_data = np.mean(data, axis=0)
            s_data = np.std(data, axis=0)

            # Perform normalization
            norm_data = (data - m_data) / s_data

            feature_row = [
                *np.max(data, axis=0), # max_x, max_y, max_z
                *np.min(data, axis=0),
                *np.mean(data, axis=0),
                *np.std(data, axis=0),
                *sp.stats.skew(data, axis=0),
                *sp.stats.entropy(norm_data, axis=0)
            ]
            
            features.append(feature_row)
        
        # Create feature DataFrame for current class
        columns = [
            'max_x', 'max_y', 'max_z',
            'min_x', 'min_y', 'min_z',
            'mean_x', 'mean_y', 'mean_z',  
            'std_x', 'std_y', 'std_z',
            'skew_x', 'skew_y', 'skew_z',
            'entropy_x', 'entropy_y', 'entropy_z',
        ]
        
        class_features = pd.DataFrame(features, columns=columns)
        class_features['activity'] = task
        
        feature_set = pd.concat([feature_set, class_features], ignore_index=True)

    # Save results
    feature_set.to_csv(f'features_{segment_size}.csv', index=False)
    return feature_set

if __name__=='__main__':

    # TODO: please update the code to extract additional features.
    extract_features(filename=dataset_path, 
                     segment_size = 250)

    extract_features(filename=dataset_path, 
                     segment_size = 500)