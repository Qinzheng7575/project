#使用之前先将server和client的路径加到系统变量里
import pygame,sys
from pygame.locals import *
import time
import subprocess
import logging
import socket
from tkinter import * 
from tkinter import messagebox 
import platform

class Node:
    Node_init = pygame.image.load('D:\ForStudy\python练习\练习\项目\img\zhongduan.png')
    Node_init = pygame.transform.scale(Node_init, (70, 70))
    Node_g=pygame.image.load('D:\ForStudy\python练习\练习\项目\img\zhongduan_g.png')
    Node_g = pygame.transform.scale(Node_g, (70, 70))
    Node_rect = Node_init.get_rect()
    if_click=0
    x = 0
    y = 0
    Pitch_angle = ""  #俯仰角
    Yaw_angle = ""  #偏航角
    Roll_angle = ""  #翻滚角
    Node_x = ""
    Node_y = ""
    Node_z = ""
    Node_x_speed = ""
    Node_y_speed = ""
    Node_z_speed = ""
    Node_txt=[]
        


    x_mid = 0
    y_mid = 0
    def __init__(self, x_pot, y_pot):
        self.x = x_pot
        self.y = y_pot

    def get_x_mid(self):
        return self.x + self.Node_rect.width / 2
    def get_y_mid(self):
        return self.y + self.Node_rect.height / 2


class Api_need:
    udp_data=b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10\x11\x12\x13\x14\x15'\
            b'\x16\x17\x18\x19\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x30\x31'\
            b'\x32\x33\x34\x35\x36\x37\x38\x39'

    txt = []
    render=[]
    i=0
    line_num = 0
    flag = 0
    V_flag=0
    V_receive_txt=[]#V发送配置报文之后，应该收到 的东西，和下一个变量一起使用，目前时iperf的结果
    V_num=0#V收到配置报文回复的个数，代表配置完毕
    V_if_iperf=0#是否执行iperf了

    S_flag=0
    S_receive_txt=[]#S发送配置报文之后，应该收到 的东西，和下一个变量一起使用，目前时iperf的结果
    S_num=0#V收到配置报文回复的个数，代表配置完毕
    S_if_iperf=0#是否执行iperf了

    # ttf_abs = 'C:\Windows\Fonts\STSONG.TTF'
    ttf_abs ='C:\Windows\Fonts\simhei.ttf'

    pipe_flag = 0
    Node_txt=[]


    def readtxt(self):
        file = open("D:\ForStudy\python练习\练习\项目\Test.txt", "rt", encoding="utf-8") 
        File = file.readlines()
        for line in File:
            line=line.strip('\n')
            # print(line)
            self.txt.append(line)
        file.close()
        
        self.drawText(self)
        # a = self.test_txt[self.i]
        # self.i+=1
        # self.txt.append(a)
        # if len(self.txt) > 10:
        #     self.txt = []
        #     self.i=0
        time.sleep(0.02)#刷新时间

    def drawText(self, textHeight=15, fontColor=(0, 0, 0), backgroudColor=(255, 255, 255)):
            # print(self.txt)
            ttf_abs = 'C:\Windows\Fonts\STSONG.TTF'
            fontObj = pygame.font.Font(ttf_abs, textHeight)  # 通过字体文件获得字体对象

            for i in range(len(self.txt)):
                self.render.append(fontObj.render(self.txt[i], False, (0,0,0)))
            # for i in range(len(render)):
            #     print(i)
            #     screen.blit(render[i], (800, 30 + 30 * i))

    #进程监听：
    # def V_send(self):
    #     if self.V_flag == 1:
    #         return
    #     with subprocess.Popen("V_send.py", shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
    #         while True:
    #             output = process.stdout.readline()
    #             if output == '' and process.poll() is not None:
    #                 break
    #             if output:
    #                 pass
    #         rc = process.poll()
    #     time.sleep(1)
    #     self.kill(self,'11000')
    #     print('配置完毕')




    # def V_receive(self):
    #     print('正在监听中')
    #     V_PID=0
    #     with subprocess.Popen(["V_listen.py"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
    #         while True:
    #             output = process.stdout.readline()
    #             if output == '' and process.poll() is not None:
    #                 break
    #             if output:

    #                 # print(output.strip())
    #                 self.V_receive_txt.append(output.strip())
    #                 self.V_num+=1
    #         rc = process.poll()
    #         self.V_flag = 1
    #线程监听：

    def V_config_client_send(self):
        # port=11000
        port=25600
        text=b'\xeb\x90\x17\x06\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(text, ('127.0.0.1', port))

    def V_config_client_receive(self):

        # port=11000
        port=25600
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', port))
        data, address = sock.recvfrom(1024)
        time.sleep(2)
        self.V_num=1
        self.V_if_iperf=1

        self.V_iperf_client(self)

    def V_config_server_send(self):
        # port=11000
        port=25600
        text2=b'\xeb\x90\x17\x06\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        text3=b'\xeb\x90\x17\x06\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(text2, ('192.168.3.2', port))
        sock.sendto(text3,('192.168.3.3',port))
        print("已发送")


    def V_config_server_receive(self):

        # port=11000
        # port=25600
        # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # sock.bind(('0.0.0.0', port))
        # data, address = sock.recvfrom(1024)
        # time.sleep(2)
        self.V_num=1
        self.V_if_iperf=1
        # print(data)
        self.V_iperf_server(self)

    def V_iperf_server(self):
        fontObj = pygame.font.Font(self.ttf_abs, 17)        
        if 'Windows'in platform.platform():
            print('This platform is Windows')
            with subprocess.Popen(["iperf-2.1.0-rc-win.exe","-s","-u","--port","24600","-i","2"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
            # with subprocess.Popen(["iperf-2.1.0-rc-win.exe","-s","-u","--port","24600","-i","2"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
                while True:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        # print(output.strip())
                        self.render.append(fontObj.render(output.strip(), False, (0, 0, 0)))
                        if len(self.render)>6:
                            del self.render[0]
        # elif 'Linux'in platform.platform():
        # elif 'Mac' in platform.platform():

    def V_iperf_client(self):
        if 'Windows'in platform.platform():
            print('This platform is Windows')
            # with subprocess.Popen(["iperf-2.1.0-rc-win.exe","-c","127.0.0.1","-u","-p","24600","-b","200M","-i","2","-t","20"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
            with subprocess.Popen(["iperf-2.1.0-rc-win.exe","-c","192.168.3.3","-u","-p","24602","-b","200M","-i","2","-t","600"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
                while True:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        pass



    def S_config_client_send(self):
        # port=11000
        port=25600
        text=b'\xeb\x90\x17\x01\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(text, ('127.0.0.1', port))

    def S_config_client_receive(self):

        # port=11000
        port=25600
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', port))
        data, address = sock.recvfrom(1024)
        time.sleep(2)
        self.S_num=1
        self.S_if_iperf=1

        self.S_iperf_client(self)

    def S_config_server_send(self):
        # port=11000
        port=25600
        text=b'\xeb\x90\x17\x01\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(text, ('127.0.0.1', port))

    def S_config_server_receive(self):

        # port=11000
        port=25600
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', port))
        data, address = sock.recvfrom(1024)
        time.sleep(2)
        self.S_num=1
        self.S_if_iperf=1
        # print(data)
        self.S_iperf_server(self)

    def S_iperf_server(self):
        fontObj = pygame.font.Font(self.ttf_abs, 17)
        if 'Windows'in platform.platform():
            print('This platform is Windows')
            with subprocess.Popen(["iperf-2.1.0-rc-win.exe","-s","-u","--port","24600","-i","2"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
            # with subprocess.Popen(["iperf-2.1.0-rc-win.exe","-s","-u","--port","24600","-i","2"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:

                while True:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        # print(output.strip())
                        self.render.append(fontObj.render(output.strip(), False, (0, 0, 0)))
                        if len(self.render)>6:
                            del self.render[0]

    def S_iperf_client(self):
        if 'Windows'in platform.platform():
            print('This platform is Windows')
            with subprocess.Popen(["iperf-2.1.0-rc-win.exe","-c","192.168.3.3","-u","-p","24602","-b","200M","-i","2","-t","600"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
            # with subprocess.Popen(["iperf-2.1.0-rc-win.exe","-c","127.0.0.1","-u","-p","24600","-b","200M","-i","2","-t","20"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:

                while True:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        pass

    




    def V_tanchuang(self):
        tk=Tk()
        tk.wm_withdraw()
        messagebox.showinfo('请稍等','等待回复中')
        tk.mainloop()


    def server(self):
        if self.flag == 1:
            return
        with subprocess.Popen("2-2-UDPPingerServer.py", shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
            while True:
                # print("doing server")
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    pass
            rc = process.poll()


    def client(self,screen):
        PID=0
        with subprocess.Popen(["UDPPingerClient.py", "127.0.0.1","12000"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    pass
                    # print(output.strip())
                    self.txt.append(output.strip())
            rc = process.poll()
            time.sleep(1)
            self.flag = 1
            if self.flag ==1:

                with subprocess.Popen(["netstat", "-ano|findstr","12000"], stdout=subprocess.PIPE, shell=True,universal_newlines=True) as process:
                            while True:
                                output = process.stdout.readline()
                                if output == '' and process.poll() is not None:
                                    break
                                if output:
                                    PID = output[-6:]
                                    print(output)
                                    # print(output[-6:])
                with subprocess.Popen("taskkill  /F /pid "+str(PID), stdout=subprocess.PIPE, shell=True,universal_newlines=True) as process:
                            while True:
                                output = process.stdout.readline()
                                if output == '' and process.poll() is not None:
                                    break
                                if output:
                                    print(output.strip())
                                    # self.txt.append(output.strip)
        fontObj = pygame.font.Font(self.ttf_abs, 14)
        for i in range(len(self.txt)):
            # print(self.txt[i])
            self.render.append(fontObj.render(str(self.txt[i]), False, (0, 0, 0)))



    def UDP_test_client(self):
        PID=0
        with subprocess.Popen(["UDP_test.py", "client"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    pass
                    # print(output.strip())
                    # self.txt.append(output.strip())
            rc = process.poll()
            time.sleep(1)
            self.flag = 1
            if self.flag ==1:
                print("client has shut")
                with subprocess.Popen(["netstat", "-ano|findstr","23000"], stdout=subprocess.PIPE, shell=True,universal_newlines=True) as process:
                            while True:
                                output = process.stdout.readline()
                                if output == '' and process.poll() is not None:
                                    break
                                if output:
                                    PID = output[-6:]
                                    print(output)
                                    # print(output[-6:])
                with subprocess.Popen("taskkill  /F /pid "+str(PID), stdout=subprocess.PIPE, shell=True,universal_newlines=True) as process:
                            while True:
                                output = process.stdout.readline()
                                if output == '' and process.poll() is not None:
                                    break
                                if output:
                                    print(output.strip())
                                    self.txt.append(output.strip)
        fontObj = pygame.font.Font(self.ttf_abs, 15)
        for i in range(len(self.txt)):
            # print(self.txt[i])                                    
            self.render.append(fontObj.render(str(self.txt[i]), False, (0, 0, 0)))


    def kill(self,port):
        PID=0

        with subprocess.Popen(["netstat", "-ano|findstr",port], stdout=subprocess.PIPE, shell=True,universal_newlines=True) as process:
                    while True:
                        output = process.stdout.readline()
                        if output == '' and process.poll() is not None:
                            break
                        if output:
                            PID = output[-6:]
                            print(output)
                            # print(output[-6:])
        with subprocess.Popen("taskkill  /F /pid "+str(PID), stdout=subprocess.PIPE, shell=True,universal_newlines=True) as process:
                    while True:
                        output = process.stdout.readline()
                        if output == '' and process.poll() is not None:
                            break
                        if output:
                            print(output.strip())









class Button:
    if_click = 0
    url='D:\ForStudy\Desktop\C4挑战赛\images\\'
    def __init__(self, name,name_g):

        self.BT = pygame.image.load(self.url+name)
        self.BT_g=pygame.image.load(self.url+name_g)
        self.BT_rect=self.BT.get_rect()


def draw_Connect(Nighbour_v,Nighbour_s,screen,node1,node2,node3,BK_flag):
    if BK_flag==3:
        if Nighbour_v["12"] == 1:
            pygame.draw.line(screen, [0, 0, 0], (node1.get_x_mid()-33, node1.get_y_mid()+6), (node2.get_x_mid()+33, node2.get_y_mid()+6), 3)
        if Nighbour_v["13"] == 1:
            pygame.draw.line(screen, [0, 0, 0], (node1.get_x_mid()+33, node1.get_y_mid()+6), (node3.get_x_mid()-35, node3.get_y_mid()+6), 3)
        if Nighbour_v["23"] == 1:
            pygame.draw.line(screen, [0, 0, 0], (node2.get_x_mid()+33, node2.get_y_mid()+6), (node3.get_x_mid()-35, node3.get_y_mid()+6), 3)

        #红色
        if Nighbour_s["12"] == 1:
            pygame.draw.line(screen, [255, 0, 0], (node1.get_x_mid()-33, node1.get_y_mid()-9), (node2.get_x_mid()+33, node2.get_y_mid()-9), 3)
        if Nighbour_s["13"] == 1:
            pygame.draw.line(screen, [255, 0, 0], (node1.get_x_mid()+33, node1.get_y_mid()-9), (node3.get_x_mid()-35, node3.get_y_mid()-9), 3)
        if Nighbour_s["23"] == 1:
            pygame.draw.line(screen, [255, 0, 0], (node2.get_x_mid()+33, node2.get_y_mid()-9), (node3.get_x_mid()-35, node3.get_y_mid()-9), 3)
    
    elif BK_flag==2:
        if Nighbour_v["23"] == 1:
            pygame.draw.line(screen, [0, 0, 0], (node2.get_x_mid()+33, node2.get_y_mid()+6), (node3.get_x_mid()-35, node3.get_y_mid()+6), 3)

        #红色
        if Nighbour_s["23"] == 1:
            pygame.draw.line(screen, [255, 0, 0], (node2.get_x_mid()+33, node2.get_y_mid()-9), (node3.get_x_mid()-35, node3.get_y_mid()-9), 3)


def draw_button(screen, pic: Button, pos):
    if pic.if_click==0:
        screen.blit(pic.BT, pos)
    else: 
        screen.blit(pic.BT_g,pos)


