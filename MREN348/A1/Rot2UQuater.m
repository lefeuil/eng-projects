% MREN 348 Assignment 1
% Kay Burnham 
% ID 20220414
% NetID 19kob1

%%QUESTION 3A
function Rot2UQuater(RotMatrix)
eta = 0.5 * sqrt(RotMatrix(1,1)+RotMatrix(2,2)+RotMatrix(3,3)+1);
esp = [0.5 * signum((RotMatrix(3,2)-RotMatrix(2,3))) * sqrt(RotMatrix(1,1)-RotMatrix(2,2)-RotMatrix(3,3)+1);
       0.5 * signum((RotMatrix(1,3)-RotMatrix(3,1))) * sqrt(RotMatrix(2,2)-RotMatrix(3,3)-RotMatrix(1,1)+1);
       0.5 * signum((RotMatrix(2,1)-RotMatrix(1,2))) * sqrt(RotMatrix(3,3)-RotMatrix(1,1)-RotMatrix(2,2)+1)];

 
    % display results [Eta (scalar) and Esp (vector)]
    fprintf(" Eta: %0.2f \n Esp: [", eta);
    fprintf(" %0.2g " , esp);
    fprintf("] \n");

end

%modified signum function
function result = signum (value)
    result = sign(value);
    if (value == 0)
        result = 1;
    end
end