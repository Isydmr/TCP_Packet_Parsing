import socket
class tcp:
    def __init__(self):
        self.TCP_IP = '192.168.1.21'
        self.TCP_PORT = 6010
        self.BUFFER_SIZE = 1024
        self.MESSAGE = (b'send bytes')
        self.oku = True
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.TCP_IP, self.TCP_PORT))
        self.s.send(self.MESSAGE)
        self.yolcu_alma_x = None
        self.yolcu_alma_y = None
        self.yolcu_verme_x = None
        self.yolcu_verme_y = None


    def parse_bytes(self,text):
        toplam_paket = 0
        senkron_biti_1 = False
        senkron_biti_2 = False
        # split the text
        words = text.split('x')
        buffer = []
        for index,harf in enumerate(words):
            if (harf)[:2] == 'FF':
                buffer.append(harf[:2])
                if buffer[0] == 'FF' and not senkron_biti_1:
                    senkron_biti_1 = True
                    continue

            if senkron_biti_1 and not senkron_biti_2:
                if harf[:2] == 'FF':
                    # buffer.append(harf[:2])
                    senkron_biti_2 = True
                    continue

            if senkron_biti_2:
                buffer.append(harf[:2])
                if( (len(buffer)%11==0) and not len(buffer) == 0):
                    senkron_biti_1 = False
                    senkron_biti_2 = False
                    if self.get_coord_type(buffer,toplam_paket) == True:
                        self.yolcu_alma_x = self.get_x_coord(buffer,toplam_paket)
                        self.yolcu_alma_y = self.get_y_coord(buffer,toplam_paket)
                        toplam_paket += 1
                    elif self.get_coord_type(buffer,toplam_paket) == False:
                        self.yolcu_verme_x = self.get_x_coord(buffer,toplam_paket)
                        self.yolcu_verme_y = self.get_y_coord(buffer,toplam_paket)
                        toplam_paket += 1
                    else:
                        print('tip hata')
                        return buffer
                continue

    def get_coord_type(self,buffer,index):
        if index == 0:
            print("tip:"+buffer[2])

            if (buffer[2] == '00'):
                yolcu_alma = True
            else:
                yolcu_alma = False
            print (yolcu_alma)
            return yolcu_alma
        if index ==  1:
            print("tip:" + buffer[13])

            if (buffer[13] == '00'):
                yolcu_alma = True
            else:
                yolcu_alma = False
            print(yolcu_alma)
            return  yolcu_alma
        else:
            print("hata")

    def get_x_coord(self, buffer, index):
        x_coord = []
        if index == 0:
            for i in range(3, 7):
                x_coord.append(buffer[i])
        if index == 1:
            for i in range(14, 18):
                x_coord.append(buffer[i])
        x_coord = x_coord[::-1]
        x_coord_hex = "".join(x_coord)
        x_coord = int(x_coord_hex, 16)
        return x_coord

    def get_y_coord(self,buffer,index):
        y_coord = []


        if index == 0:
            for i in range(7, 11):
                y_coord.append(buffer[i])
        if index == 1:
            for i in range(18, 22):
                y_coord.append(buffer[i])
        y_coord = y_coord[::-1]
        y_coord_hex = "".join(y_coord)
        y_coord = int(y_coord_hex,16)
        return y_coord

    def getData(self):
        data = self.s.recv(tcp.BUFFER_SIZE)
        data = data.decode("utf-8")
        f = open('gelendata.txt', 'a')
        f.write(data)
        f.write('\n')
        f.close()
        self.parse_bytes(data)
        print('verme->x')
        print(tcp.yolcu_verme_x)
        print('verme->y')
        print(tcp.yolcu_verme_y)
        print('alma->x')
        print(tcp.yolcu_alma_x)
        print('alma->y')
        print(tcp.yolcu_alma_y)
        # self.s.close()
        return



#data = struct.unpack('>BL',s.recv(BUFFER_SIZE))
#tcp = tcp()
#tcp.getData()
