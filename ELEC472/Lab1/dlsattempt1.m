function [nodeList, result] = dls(source, target, startNode, targetNode, depth)
% Initialize visited list, queue and nodeList 
% added: cdepth = current depth 
 nodeList = [];
 visited = [];
 queue = [];
 cdepth = [];

 % Set starting node as current node and add it to visited list
 visited(end+1) = startNode;
 queue(end+1) = startNode;
 cdepth(1) = 0;
 iterations = 0;

 while ~isempty(queue)
     % Pop the first item from queue
     currentNode = queue(1);
     queue(1) = []; % This is how you pop the first element of a vector
     currentDepth = cdepth(1);
     cdepth(1) = [];

     if (currentDepth >= depth)
        fprintf("depth limit reached\n");
        return
        % convert to IDS by uncommenting this:
        % depth = depth + 1;
        % fprintf("depth limit reached. New depth: %f", depth);
     end 
    
     % check the current node and add it to visited list
     iterations = iterations + 1;
     nodeList(end+1) = currentNode;
     if currentNode == targetNode
        return
     end
     visited(end+1) = currentNode;
    
     
     % Get all the children of the current node 
     % add them to the queue if not visited
     children = getChildren(source, target, currentNode);

     for i = 1:numel(children)
         fprintf("%d\n", currentDepth);
         if ~any(visited==children(i)) 
             % go down a layer if node has unvisited children
             d = dls(source, target, children(i), targetNode, depth);
             if (d == 1)
                 return
             end
             visited(end+1) = children(i);
             queue = [children(i), queue]; 
         end
     end
     cdepth(end+1) = currentNode;
 end

 nodeList = -1;
 disp('Target not found!')
 end

 % Helper function to get the children of a node
 function children = getChildren(source, target, node)
    children = target(source == node);
 end