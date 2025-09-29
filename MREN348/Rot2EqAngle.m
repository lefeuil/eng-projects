% MREN 348 Assignment 1
% Kay Burnham 
% ID 20220414
% NetID 19kob1


%% QUESTION 2A 
function Rot2EqAngle(RotMatrix)
nu = acos((RotMatrix(1,1)+RotMatrix(2,2)+RotMatrix(3,3)-1)/2) * 180/pi;
a = 1/(2*sin(nu));
r = [a * (RotMatrix(3,2)-RotMatrix(2,3));
     a * (RotMatrix(1,3)-RotMatrix(3,1));
     a * (RotMatrix(2,1)-RotMatrix(1,2))];

if (nu == 0)
    % display message describing case
    fprintf("No rotation, r is arbitrary \n");
    % recalculate 
    
    % display results [Nu (in degrees) and R (vector)]
    fprintf("Nu: %0.2f \n r: [", nu);
    fprintf(" %0.2g " , r);
    fprintf("] \n ");
elseif (nu == 180) 
    % display message describing case
    fprintf("Y' rotation of 180 degrees: r flipped \n");
    %recalculate 

    % display results [Nu (in degrees) and R (vector)]
    fprintf("Nu: %0.2f \n r: [", nu);
    fprintf(" %0.2g " , r);
    fprintf("] \n ");
else 
    % display results [Nu (in degrees) and R (vector)]
    fprintf("Nu: %0.2f \n r: [", nu);
    fprintf(" %0.2g " , r);
    fprintf("] \n ");
end
