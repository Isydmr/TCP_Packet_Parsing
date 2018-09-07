

import socket


TCP_IP = '192.168.1.24'
TCP_PORT = 5010
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

#gonderilecek_paket2 = (bytearray([0xFF, 0xFF, 0x00, 0xE8, 0x03, 0x00, 0x00, 0xE8, 0x03, 0x00, 0x00]))
gonderilecek_paket2 = bytearray(b'\0x03\0x00\0x00\0xE8\0x03\0x00\0x00\0xFF\0xFF\0x00\0xE8\0x03\0x00\0x00\0xE8\0x03\0x00\0x00\0xFF\0xFF\0x00\0xE8\0x03')
#ACABA GONDERILECEK PAKET FORMATI HANGI TIPTE OLACAK.? usttekı mı alltakı mı
print(gonderilecek_paket2)
conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    #data = conn.recv(BUFFER_SIZE)
    # if not data: break
    #print ("received data:", data)
    conn.send(gonderilecek_paket2)  # echo
    print(gonderilecek_paket2)

conn.close()
