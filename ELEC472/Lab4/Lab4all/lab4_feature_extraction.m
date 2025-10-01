clear all;
close all;
clc;

% import raw_accelerometer data 
raw_data        = readtable("raw_accelerometer_dataset.csv");
feature_set     = table;            % variable initialization
event           = 0;                % variable initialization
segment_size    = 500;              % window size of each segment
class           = unique(raw_data.Class);   % getting the available classes

disp('extracting features ...');
for task = 1:numel(class)
    activity     = task;
    group_id     = [];
    db_table     = raw_data(strcmp(raw_data.Class, class{task,1}), 2:4);  % selected rows of a particular activity class
    for k        = 1:segment_size:size(db_table,1)
        event    = event + 1;
        ID       = repmat(event, segment_size,1);
        group_id = vertcat(group_id, ID); % adding an extra column which we will need later.
    end
    group_id            = group_id(1:size(db_table, 1));
    db_table.group_id   = group_id;
    
    % initialize feature table
    max_feature_table   = [];
    min_feature_table   = [];
    mean_feature_table  = [];
    std_feature_table   = [];
    skewness_feature_table  = [];
    unique_group            = unique(db_table.group_id);
    
    for cal_k = 1:size(unique_group, 1)
        data             = table2array(db_table(db_table.group_id ==unique_group(cal_k),1:size(db_table,2)-1));
        max_feature      = max(data);   % calculate max of each segmented signal
        % appending features to the table
        max_feature_table       = [max_feature_table; max_feature]; 

    end
    
    label                                       = repmat(activity, length(unique(group_id)), 1);   % duplicating label same as extracted features
    tmp_feature_table                           = [max_feature_table];   % stacking all the extracted features in one single table
    tmp_feature_table                           = array2table(tmp_feature_table);
    tmp_feature_table.Properties.VariableNames  = {'max_x','max_y','max_z',...
                                                }; % adding column names to the feature table
    tmp_feature_table.activity                  = label;   % adding activity labels to the feature table

    feature_set                                 = vertcat(feature_set, tmp_feature_table); % storing extracted features of all subjects all activities in single table.

end


