%% Question 1
% forward kinematic solutions of three robots 
% (spherical arm)

function Sph_Direct(mu_1, mu_2, d_3)
% assume inputs are in deg, deg, metres
% hardcoded link offset: 
d_2 = 4.2; 

%convert input deg to radians
mu_1 = deg2rad(mu_1);
mu_2 = deg2rad(mu_2);

% H. Transform matrices
A01 = [cos(mu_1), -sin(mu_1), 0, d_2*cos(mu_1);
       sin(mu_1),  cos(mu_1), 0, d_2*sin(mu_1);
       0,          0,         1, 0;
       0,          0,         0, 1];

A12 = [ cos(mu_2), 0, sin(mu_2), 0;
        0,        1,  0,       0;
       -sin(mu_2), 0, cos(mu_2), 0;
        0,        0, 0,        1];

A23 = [1, 0, 0, 0;
       0, 1, 0, 0;
       0, 0, 1, d_3;
       0, 0, 0, 1];

% Final transform 
A03 = A01 * A12 * A23;
disp(A03);

end


