<h2> Packet Parsing </h2>

This repository contains only a part of our autonomous robotaxi project for Teknofest-2018 competition. Using **tcp_paket_client.py** file, we succesfully parsed the recieved byte array.

In competition, the information of the passenger pick-up and drop-off locations transmitted over Wi-Fi communication.

The total packet length is 11 bytes. The first two bytes contain the start bits at 0xFFFF. The
next 1-byte expresses the position type. This byte is 0 for the passenger pick-up point and
1 for the passenger drop-off point. The x-coordinate and the y-coordinate are 4-byte littleendian
signed int numbers.

See the following image:

![alt text](https://raw.githubusercontent.com/Isydmr/tcp_paket_server/master/tcp-ip.jpg)

Source: https://www.teknofestistanbul.org/Content/files/Teknoloji/Robotaksi_english_2018_09_05.pdf
