%% dls 

function [nodeList, result] = dls(source, target, startNode, targetNode, depth)
    nodeList = startNode;
    result = 0;

    if (startNode == targetNode)
        result = 1;
        return 
    end
    if (depth == 0)
        % for DLS: 
        result = 0;
        fprintf("depth limit reached\n");
        return
    end
    
    children = getChildren(source, target, startNode);
    for i = 1:numel(children)
        [ns, r] = dls(source, target, children(i), targetNode, depth-1);
        nodeList = [nodeList ns];
        result = r;
        if (result == 1) 
            return
        % uncomment for IDS: 
        % else
        %     depth = depth + 1;
        %     fprintf(" Depth limit reached. \n New depth: %f \n", depth);
        end
    end
end



 function children = getChildren(source, target, node)
    children = target(source == node);
 end