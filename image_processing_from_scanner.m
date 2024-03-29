% For Windows computers, the name is formatted like: "COM6"
% For Apple computers, the name is formatted like: "/dev/tty.usbmodemfa141" 
%
arduinoComPort = 'COM7';


%
% Set the baud rate
% NOTE1: The baudRate for the sending and receiving programs must be the same!
% NOTE2: Set the baudRate to 115200 for faster communication
%
baudRate = 9600;


%
% open the serial port, close it first in case it was previously open
%
out1 = instrfind('Port','COM7')
fclose(instrfind)
fopen(instrfind)
% serialPort = serial('COM7', 'BAUD', 9600);
% fopen(serialPort);
% fprintf(serialPort, '\n');



%
% initialize a timeout in case MATLAB cannot connect to the arduino
%
timeout = 0;
listx = [];
listy = [];
listz = [];


%
% main loop to read data from the Arduino, then display it
%
while timeout < 5

    %
    % check if data was received
    %
    while serialPort.BytesAvailable > 0
        %
        % reset timeout
        %
        timeout = 0;
        
        %
        % data was received, convert it into array of integers
        %
        values = eval(strcat('[',fscanf(serialPort),']'));
        print(values);
        %
        % if you want to store the integers in four variables
        %
        azimuth = values(1);
        elevation = values(2);
        sensorAve = values(3);
        
        [x, y, z] = sph2cart(azimuth,elevation,sensorAve);
        append(listx, x);
        append(listy, y);
        append(listz, z);
    end
    pause(0.5);
    timeout = timeout + 1;
end
tolerance = 500

for index = 1:length(listz)
    if listz(index) <= tolerance
        listz(index) = 1;
    end
    if listz(index) > tolerance
        listz(index) = 0;
    end
end

pointsize = 10;
scatter(listx, listy, pointsize, listz);
fclose(serialPort);
       
    
    


