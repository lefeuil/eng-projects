% MREN 348 Assignment 1
% Kay Burnham 
% ID 20220414
% NetID 19kob1
%
% NOTE: called from Rot2ZYZsupport.m 
% file has provided matrices already entered to supply output 

%% QUESTION 1A 
% not considering special cases, there are two possible sets of ZYZ Euler
% angles -- one with angles of rotation of (a, b, c) and a second with
% (a+180, -b, c+180). 

%% QUESTION 1B 
function Rot2ZYZ(RotMatrix)
% calculate Euler angles from rotation matrix
phi = atan2(RotMatrix(2,3), RotMatrix(1,3)) * 180/pi;
nu  = atan2(sqrt(RotMatrix(1,3)^2+RotMatrix(2,3)^2), RotMatrix(3,3)) * 180/pi;
psi = atan2(RotMatrix(3,2), -RotMatrix(3,1)) * 180/pi;

%detect special cases
if (nu == 0)
    % display message describing case
    fprintf("No Y' rotation \n");
    %recalculate Z rotation angle 
    alpha = atan2(RotMatrix(2,1), RotMatrix(1,1)) * 180/pi;
    % display results in degrees
    fprintf("Total rotation about Z: %0.2f \n", alpha);
elseif (nu == 180) 
    % display message describing case
    fprintf("Y' rotation of 180 degrees: Z and Z'' aligned \n");
    %recalculate Z rotation angle 
    alpha = atan2(RotMatrix(2,1), RotMatrix(1,1)) * 180/pi;
    % display results in degrees
    fprintf("Total rotation about Z: %0.2f \n", alpha);
else 
    % display results in degrees 
    fprintf("Z: %0.2f \n Y': %0.2f \n Z'': %0.2f \n", phi, nu, psi);
end