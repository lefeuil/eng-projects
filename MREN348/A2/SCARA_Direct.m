%% Question 1
% forward kinematic solutions of three robots 
% (SCARA manipulator)

function SCARA_Direct(mu_1, mu_2, d_3, mu_4)
% assume inputs are in deg, deg, metres, deg
% note: mu_4 doesn't influence location, only end effector orientation 

% hardcoded link lengths: 
a_1 = 3.4; 
a_2 = 0.12;

%convert input deg to radians
mu_1 = deg2rad(mu_1);
mu_2 = deg2rad(mu_2);

% H. Transform matrices
A01 = [cos(mu_1), -sin(mu_1), 0, a_1*cos(mu_1);
       sin(mu_1),  cos(mu_1), 0, a_1*sin(mu_1);
       0,          0,         1, 0;
       0,          0,         0, 1];

A12 = [cos(mu_2), -sin(mu_2), 0, a_2*cos(mu_2);
       sin(mu_2),  cos(mu_2), 0, a_2*sin(mu_2);
       0,          0,         1, 0;
       0,          0,         0, 1];

A23 = [1, 0, 0, 0;
       0, 1, 0, 0;
       0, 0, 1, d_3;
       0, 0, 0, 1];

% Final transform 
A03 = A01 * A12 * A23;
disp(A03);

end

