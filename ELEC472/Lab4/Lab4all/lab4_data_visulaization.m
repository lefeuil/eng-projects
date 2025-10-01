clear all;
close all;
clc;

% import raw accelerometer data 
raw_data = readtable("raw_accelerometer_dataset.csv");

% see the columns in the dataset 
disp(raw_data.Properties.VariableNames);

% fetch the activity classes
class = unique(raw_data.Class);  
disp(class);
 
% we are visualizing the x axis of the accelerometer data for all the available classes.
for task = 1:numel(class)
    
    % fetching the rows belonging to a particular class
    selected_task = strcmp(raw_data.Class, class{task,1}); 
    
    % select the axis (X=2, Y=3, Z=4)
    signal = table2array(raw_data(selected_task, 2));      
    
    % create subplot
    subplot(numel(class),1,task);
    
    % plot a small segment
    plot(signal(1:5000));
    ylabel(class{task,1}, 'fontsize', 12); 
end

xlabel('time', 'fontsize', 12);
sgtitle('Accelerometer X-axis', 'fontsize', 12);

