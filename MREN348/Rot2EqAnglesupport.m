%% support file 

Rot4 = [ 0.9063 0 0.4226
         0 1.0000 0
        -0.4226 0 0.9063 ];

fprintf("rotation matrix 4: \n");
Rot2EqAngle(Rot4);

Rot5 = [ -0.7778 0.4444 0.4444
         0.4444 -0.1111 0.8889
         0.4444 0.8889 -0.1111];

fprintf("rotation matrix 5: \n");
Rot2EqAngle(Rot5);

Rot6 = [ 1 0 0
         0 1 0
         0 0 1];

fprintf("rotation matrix 6: \n");
Rot2EqAngle(Rot6);