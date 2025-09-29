%% Question 1
% forward kinematic solutions of three robots 
% (cylindrical arm)

function Cyl_Direct(mu_1, d_2, d_3)
% assume inputs are in deg, metres, metres

%convert input deg to radians
mu_1 = deg2rad(mu_1);

% H. Transform matrices
A01 = [cos(mu_1), -sin(mu_1), 0, 0;
       sin(mu_1),  cos(mu_1), 0, 0;
       0,          0,         1, 0;
       0,          0,         0, 1];

A12 = [1, 0, 0, d_2;
       0, 1, 0, 0;
       0, 0, 1, 0;
       0, 0, 0, 1];

A23 = [1, 0, 0, 0;
       0, 1, 0, 0;
       0, 0, 1, d_3;
       0, 0, 0, 1];

% Final transform 
A03 = A01 * A12 * A23;
disp(A03);

end