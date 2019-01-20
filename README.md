<h2> Packet Parsing </h2>

The information of the passenger pick-up and drop-off locations transmitted over Wi-Fi communication.

The total packet length is 11 bytes. The first two bytes contain the start bits at 0xFFFF. The
next 1-byte expresses the position type. This byte is 0 for the passenger pick-up point and
1 for the passenger drop-off point. The x-coordinate and the y-coordinate are 4-byte littleendian
signed int numbers containing the coordinates of the passenger pick-up/drop off
points on the map relative to the first starting position of the robot in centimeters. 

See the following image:

![alt text](https://raw.githubusercontent.com/Isydmr/tcp_paket_server/master/tcp-ip.jpg)

Source: https://www.teknofestistanbul.org/Content/files/Teknoloji/Robotaksi_english_2018_09_05.pdf
