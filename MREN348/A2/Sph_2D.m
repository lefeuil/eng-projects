%% Cylindrical plotting function 

function Sph_2D
x_end = [];
y_end = [];
z_end = [];
pause on;

for i = -80:4:65
    for j = -40:4:50
        for k = 3:2:16
            % calculate new position
            [x1, y1, x2, y2, z] = Sph_step(i, j, k);
            x_end(end+1) = x2;
            y_end(end+1) = y2;
            z_end(end+1) = z;
        end
    end
end

% draw figure
plot3(x_end, y_end, z_end, '.');
axis equal
axis([-15 15 -15 15 -0 15])

% change variables below for different azimuth, elevation
view(0, 90); 

end

function [x1, y1, x2, y2, z] = Sph_step(mu_1, mu_2, d_3)
% calculates positions of joints at given inputs 

% hardcoded link length: 2nd link fixed
d_2 = 9;

% joint limits: 
mu_1_min = -40; mu_1_max = 65; % Degrees
mu_2_min = -40; mu_2_max = 50;  % Degrees
d_3_min =    3; d_3_max =  16; % cm

mu_1 = max(min(mu_1, mu_1_max), mu_1_min);
mu_2 = max(min(mu_2, mu_2_max), mu_2_min);
d_3 = max(min(d_3, d_3_max), d_3_min);

mu_1 = deg2rad(mu_1);
mu_2 = deg2rad(mu_2);

d_total = d_2 + d_3;

% joint positions: base position is fixed
x1 = 0;
y1 = 0;

x2 = d_total * cos(mu_1) * cos(mu_2);
y2 = d_total * sin(mu_1) * cos(mu_2);

z = d_total * sin(mu_2); % end effector position 

end
