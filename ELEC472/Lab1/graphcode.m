clc % clear screen
clear all % clear variables
source = [1, 1, 1, 2, 2, 2, 2, 8]; % Source Nodes
target = [3, 4, 2, 6, 5, 7, 8, 9]; % Target Nodes
names = {'A', 'B', 'C', 'D', 'E', 'F', 'Kay', 'H', 'I'}; % Node Names
weights = [200, 300, 900, 400, 0, 200, 100, 50]; % Edge Weights
G1 = graph(source,target,weights,names);
figure
plot(G1, 'EdgeLabel', G1.Edges.Weight)
