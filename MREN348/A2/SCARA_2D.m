%% SCARA plotting function 

function SCARA_2D
x_end = [];
y_end = [];
pause on;

for i = -85:5:115
    for j = -140:5:85
        % calculate new position
        [x1, y1, x2, y2, z_end] = SCARA_step(i, j);
        x_end(end+1) = x2;
        y_end(end+1) = y2;
        %pause(1); % leftover from printing each angle step at a time
    end
end

%draw figure
plot(x_end, y_end, '.');
axis equal
axis([-2.5 2.5 -2.5 2.5])

end

function [x1, y1, x2, y2, z_end] = SCARA_step(mu_1, mu_2)
% calculates positions of joints at given inputs 

% hardcoded link lengths and set angles: 
a_1 = 1.8; 
a_2 = 0.17;
d_3 = 0;
mu_4 = 0;

% joint limits: 
mu_1_min =  -85; mu_1_max = 115; % Degrees
mu_2_min = -140; mu_2_max = 85;  % Degrees

mu_1 = max(min(mu_1, mu_1_max), mu_1_min);
mu_2 = max(min(mu_2, mu_2_max), mu_2_min);

mu_1 = deg2rad(mu_1);
mu_2 = deg2rad(mu_2);


% joint positions: 
x1 = a_1 * cos(mu_1);
y1 = a_1 * sin(mu_1);

x2 = x1 + a_2 * cos(mu_1 + mu_2);
y2 = y1 + a_2 * sin(mu_1 + mu_2);

z_end = d_3; % end effector position 

end
