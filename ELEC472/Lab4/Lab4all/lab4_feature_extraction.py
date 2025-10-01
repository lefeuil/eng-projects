
import pandas as pd
import numpy as np

def extract_features(filename="raw_accelerometer_dataset.csv", 
                     segment_size = 250):

    # Read raw data
    raw_data = pd.read_csv(filename)

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
            feature_row = [
                *np.max(data, axis=0) # max_x, max_y, max_z
                # TODO: modify this to extract other features ...
            ]
            
            features.append(feature_row)
        
        # Create feature DataFrame for current class
        columns = [
            'max_x', 'max_y', 'max_z',
            # TODO: you also need to modify here accordingly
        ]
        
        class_features = pd.DataFrame(features, columns=columns)
        class_features['activity'] = task
        
        feature_set = pd.concat([feature_set, class_features], ignore_index=True)

    # Save results
    feature_set.to_csv(f'features_{segment_size}.csv', index=False)
    return feature_set



if __name__=='__main__':

    # TODO: please update the code to extract additional features.
    extract_features(filename="raw_accelerometer_dataset.csv", 
                     segment_size = 250)