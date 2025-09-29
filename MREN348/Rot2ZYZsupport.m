%% support file 

Rot1 = [ 0.6552, 0.7550, 0.0250;
        -0.7526, 0.6553, -0.0651;
        -0.0655, 0.0239, 0.9976];

fprintf("rotation matrix 1: \n");
Rot2ZYZ(Rot1);

Rot2 = [ -0.9816, -0.1908, 0.0000;
         -0.1908, 0.9816, 0.0000;
         -0.0000, 0.0000, -1.0000];

fprintf("rotation matrix 2: \n");
Rot2ZYZ(Rot2);

Rot3 = [ -0.1219, -0.9925, 0;
          0.9925, -0.1219, 0;
          0, 0, 1.0000];

fprintf("rotation matrix 3: \n");
Rot2ZYZ(Rot3);