function nodeList = bfs(source, target, startNode, targetNode)
 % Initialize visited list, queue and nodeList
 nodeList = [];
 visited = [];
 queue = [];

 % Set starting node as current node and add it to visited list
 visited(end+1) = startNode;
 queue(end+1) = startNode;
 iterations = 0;

 while ~isempty(queue)
 % Pop the first item from queue
 currentNode = queue(1);
 queue(1) = []; % This is how you pop the first element of a vector

 % check the current node and add it to visited list
 iterations = iterations + 1;
 nodeList(end+1) = currentNode;
 if currentNode == targetNode
 return
 end
 visited(end+1) = currentNode;

 % Get all the children of the current node and add them to the queue if not
visited
 children = getChildren(source, target, currentNode);
 for i = 1:numel(children)
 if ~any(visited==children (i))
 queue(end+1) = children(i);
 end
 end
 end

 nodeList = -1;
 disp('Target not found!')
 end

 % Helper function to get the children of a node
 function children = getChildren(source, target, node)
 children = target(source == node);
 end