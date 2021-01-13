#使用之前先将server和client的路径加到系统变量里
import pygame,sys
from pygame.locals import *
import time
import subprocess
import threading
from threading import Thread
import logging
import struct
import multiprocessing
from multiprocessing import Pipe as guandao
import socket


class Node:
    Node_init = pygame.image.load('D:\ForStudy\Desktop\C4挑战赛\images\Guestshell.png')
    Node_g=pygame.image.load('D:\ForStudy\Desktop\C4挑战赛\images\Guestshell_g.png')
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
            b'\x16\x17\x18\x19\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x30x\31'\
            b'\x32\x33\x34\x35\x36\x37\x38\x39'

    txt = []
    render=[]
    i=0
    line_num = 0
    # render = []
    flag = 0
    ttf_abs = 'C:\Windows\Fonts\STSONG.TTF'

    pipe_flag = 0  #pipe_flag
    Node_txt=[]
    ttf_abs = 'C:\Windows\Fonts\STSONG.TTF'



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
            time.sleep(2)
            self.flag = 1
            if self.flag ==1:
                print("client has shut")
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
                                    self.txt.append(output.strip)
        fontObj = pygame.font.Font(self.ttf_abs, 15)
        for i in range(len(self.txt)):
            # print(self.txt[i])                                    
            self.render.append(fontObj.render(str(self.txt[i]), False, (0, 0, 0)))

    def node_data(self,udp_data, node1:Node, node2:Node, node3:Node):
        fontObj = pygame.font.Font(self.ttf_abs, 15)
        
        Pitch_angle=[]
        for i in range(4):
            Pitch_angle.append(udp_data[3+i])
        node1.Pitch_angle = struct.unpack('<f',struct.pack('4b',*Pitch_angle))[0]
        print("俯仰角 is {}".format(node1.Pitch_angle))

        Yaw_angle=[]
        for i in range(4):
            Yaw_angle.append(udp_data[7+i])
        node1.Yaw_angle=struct.unpack('<f',struct.pack('4b',*Yaw_angle))[0]
        print("偏航角 is {}".format(node1.Yaw_angle))

        Roll_angle=[]
        for i in range(4):
            Roll_angle.append(udp_data[11+i])
        node1.Roll_angle=struct.unpack('<f',struct.pack('4b',*Roll_angle))[0]
        print("翻滚角 is {}".format(node1.Roll_angle))



        if str(udp_data[15]) != '255':
            
            print("节点1 ID is  {}".format(str(udp_data[15])))
            #-----------------节点坐标------------------------
            Node1_x=[]
            for i in range(4):
                Node1_x.append(udp_data[16+i])
            node1.Node_x=struct.unpack('<f',struct.pack('4b',*Node1_x))[0]
            print("节点1坐标X is {}".format(node1.Node_x))

            Node1_y=[]
            for i in range(4):
                Node1_y.append(udp_data[20+i])
            node1.Node_y = struct.unpack('<f', struct.pack('4b', *Node1_y))[0]
            print("节点1坐标Y is {}".format(node1.Node_y))

            Node1_z=[]
            for i in range(4):
                Node1_z.append(udp_data[24+i])
            node1.Node_z = struct.unpack('<f', struct.pack('4b', *Node1_z))[0]
            print("节点1坐标Z is {}".format(node1.Node_z))

            #-----------------节点速度------------------------

            Node1_x_speed=[]
            for i in range(4):
                Node1_x_speed.append(udp_data[28+i])
            node1.Node_x_speed=struct.unpack('<f',struct.pack('4b',*Node1_x_speed))[0]
            print("节点1X方向速度 is {}".format(node1.Node_x_speed))

            Node1_y_speed=[]
            for i in range(4):
                Node1_y_speed.append(udp_data[32+i])
            node1.Node_y_speed=struct.unpack('<f',struct.pack('4b',*Node1_y_speed))[0]
            print("节点1Y方向速度 is {}".format(node1.Node_y_speed))

            Node1_z_speed=[]
            for i in range(4):
                Node1_z_speed.append(udp_data[36+i])
            node1.Node_z_speed=struct.unpack('<f',struct.pack('4b',*Node1_z_speed))[0]
            print("节点1Z方向速度 is {}".format(node1.Node_z_speed))
        else:
                print("节点1 ID is  -1")

        txt = ["俯仰角" + str(node1.Pitch_angle), " 偏航角" + str(node1.Yaw_angle), "翻滚角" + str(node1.Roll_angle),
                    "x:" + str(node1.Node_x), "y:" + str(node1.Node_y), "z:" + str(node1.Node_z),
                    "x速度:" + str(node1.Node_x_speed), "y速度:" + str(node1.Node_y_speed), "z速度:" + str(node1.Node_z_speed)]

        node1.Node_txt=[]#每次接受新的信息，归零
        for i in txt:
            node1.Node_txt.append(fontObj.render(i, False, (0, 0, 0)))
        
    # def UDP_test_server(self,pipe):
    #     if self.flag == 1:
    #         return
    #     with subprocess.Popen(["UDP_test.py","server"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
    #         while True:
    #             # print("doing server")
    #             output = process.stdout.readline()
    #             # print(type(output))
    #             if output == '' and process.poll() is not None:
    #                 break
    #             if output:
    #                 print(output.strip())
    #                 # self.udp_data=
    #                 self.txt.append(output.strip())
    #         rc = process.poll()


    #     fontObj = pygame.font.Font(self.ttf_abs, 15)
    #     for i in range(len(self.txt)):
    #         # print(self.txt[i])                                    
    #         self.render.append(fontObj.render(str(self.txt[i]), False, (0, 0, 0)))
    #     print(self.render)




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
            time.sleep(2)
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



#---------------------------------------------------------
    def UDP_test_server(self,pipe):
        if self.flag == 1:
            return
        with subprocess.Popen(["UDP_test.py","server"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
            while True:
                # print("doing server")
                output = process.stdout.readline()
                # print(type(output))
                if output == '' and process.poll() is not None:
                    break
                if output:
                    message=output.strip()
                    print(message)
                    pipe.send(message)
                    # self.udp_data=
                    # self.txt.append(output.strip())
            rc = process.poll()


    def pipe_begin(self):#建立pipe
        pipe = guandao()

        fa = multiprocessing.Process(target=self.UDP_test_server,  kwargs={'pipe':pipe[0]})
        shou = multiprocessing.Process(target=self.pipe_recv, kwargs={'pipe':pipe[1]})

        fa.start()
        #shou.start()

        fa.join()
        shou.terminate()



    def pipe_recv(self,pipe):
        while True:
            temp = pipe.recv()
            print('Process recv%s' % temp)  



    def node_data_s(self,udp_data):
        Pitch_angle=[]
        for i in range(4):
            Pitch_angle.append(udp_data[3 + i])
            # print(Pitch_angle)
        self.Pitch_angle = struct.unpack('<f',struct.pack('4B',*Pitch_angle))[0]
        print("Pitch_angle is {}".format(self.Pitch_angle))

        Yaw_angle=[]
        for i in range(4):
            Yaw_angle.append(udp_data[7+i])
        self.Yaw_angle=struct.unpack('<f',struct.pack('4B',*Yaw_angle))[0]
        print("Yaw_angle  is {}".format(self.Yaw_angle))

        Roll_angle=[]
        for i in range(4):
            Roll_angle.append(udp_data[11+i])
        self.Roll_angle=struct.unpack('<f',struct.pack('4B',*Roll_angle))[0]
        print("Roll_angle is {}".format(self.Roll_angle))


        # print(str(udp_data[15]))
        if str(udp_data[15]) != '255':
            
            print("node1 ID is  {}".format(str(udp_data[15])))
            #-----------------节点坐标------------------------
            Node1_x=[]
            for i in range(4):
                Node1_x.append(udp_data[16+i])
            self.Node_x=struct.unpack('<f',struct.pack('4B',*Node1_x))[0]
            print("Node_x is {}".format(self.Node_x))

            Node1_y=[]
            for i in range(4):
                Node1_y.append(udp_data[20+i])
            self.Node_y = struct.unpack('<f', struct.pack('4B', *Node1_y))[0]
            print("Node_y is {}".format(self.Node_y))

            Node1_z=[]
            for i in range(4):
                Node1_z.append(udp_data[24+i])
            self.Node_z = struct.unpack('<f', struct.pack('4B', *Node1_z))[0]
            print("Node_z is {}".format(self.Node_z))

            #-----------------节点速度------------------------

            Node1_x_speed=[]
            for i in range(4):
                Node1_x_speed.append(udp_data[28+i])
            self.Node_x_speed=struct.unpack('<f',struct.pack('4B',*Node1_x_speed))[0]
            print("Node_x_speed is {}".format(self.Node_x_speed))

            Node1_y_speed=[]
            for i in range(4):
                Node1_y_speed.append(udp_data[32+i])
            self.Node_y_speed=struct.unpack('<f',struct.pack('4B',*Node1_y_speed))[0]
            print("Node_y_speed is {}".format(self.Node_y_speed))

            Node1_z_speed=[]
            for i in range(4):
                Node1_z_speed.append(udp_data[36+i])
            self.Node_z_speed=struct.unpack('<f',struct.pack('4B',*Node1_z_speed))[0]
            print("Node_z_speed is {}".format(self.Node_z_speed))
        else:
            pass
    
        # txt = ["俯仰角" + str(node1.Pitch_angle), " 偏航角" + str(node1.Yaw_angle), "翻滚角" + str(node1.Roll_angle),
        #             "x:" + str(node1.Node_x), "y:" + str(node1.Node_y), "z:" + str(node1.Node_z),
        #             "x速度:" + str(node1.Node_x_speed), "y速度:" + str(node1.Node_y_speed), "z速度:" + str(node1.Node_z_speed)]

        # node1.Node_txt=[]#每次接受新的信息，归零
        # for i in txt:
        #     node1.Node_txt.append(fontObj.render(i, False, (0, 0, 0)))






class Button:
    if_click = 0
    url='D:\ForStudy\Desktop\C4挑战赛\images\\'
    def __init__(self, name,name_g):

        self.BT = pygame.image.load(self.url+name)
        self.BT_g=pygame.image.load(self.url+name_g)
        self.BT_rect=self.BT.get_rect()


def draw_Connect(Nighbour,screen,node1,node2,node3):
    if Nighbour["12"] == 1:
        pygame.draw.line(screen, [0, 0, 0], (node1.get_x_mid(), node1.get_y_mid()), (node2.get_x_mid(), node2.get_y_mid()), 3)
    if Nighbour["13"] == 1:
        pygame.draw.line(screen, [0, 0, 0], (node1.get_x_mid(), node1.get_y_mid()), (node3.get_x_mid(), node3.get_y_mid()), 3)
    if Nighbour["23"] == 1:
        pygame.draw.line(screen, [0, 0, 0], (node2.get_x_mid(), node2.get_y_mid()), (node3.get_x_mid(), node3.get_y_mid()), 3)

def draw_button(screen, pic: Button, pos):
    if pic.if_click==0:
        screen.blit(pic.BT, pos)
    else: 
        screen.blit(pic.BT_g,pos)


# if __name__ == "__main__":

#      api = Api_need()
    
#      api.pipe_begin()
    

#     server = Thread(target=api.server_s, args=(api,23000,))
#     client = Thread(target=api.client_s, args=(api,23000,))
#     server.start()
#     client.start()
#     client.join()
    # print(api.Pitch_angle,"***")


    # class xx:
    #     def __init__():
    #         self.    

    #     def  run(self,):