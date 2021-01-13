
#--------------------------------------------
# import subprocess
# import sys
# import threading
# from threading import Thread
# import time
# import logging

# flag=0
# stdout = sys.stdout

# def server():
#     global flag
#     if flag == 1:
#         return
#     with subprocess.Popen("2-2-UDPPingerServer.py", shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
#         while True:
#             print("doing")

#             output = process.stdout.readline()

#             if output == '' and process.poll() is not None:
#                 break
#             if output:
#                 pass


#         rc = process.poll()


# def client():
#     global flag
#     PID=0
#     with subprocess.Popen(["UDPPingerClient.py", "127.0.0.1","12000"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
#         while True:
#             output = process.stdout.readline()
#             if output == '' and process.poll() is not None:
#                 break
#             if output:
#                 pass

#                 print(output.strip())


#         rc = process.poll()
#         time.sleep(2)
#         flag = 1
#         if flag ==1:
#             print("client has shut")
#             with subprocess.Popen(["netstat", "-ano|findstr","12000"], stdout=subprocess.PIPE, shell=True,universal_newlines=True) as process:
#                         while True:
#                             output = process.stdout.readline()
#                             if output == '' and process.poll() is not None:
#                                 break
#                             if output:
#                                 PID = output[-5:]
#                                 print(output[-5:])
#             with subprocess.Popen("taskkill  /F /pid "+str(PID), stdout=subprocess.PIPE, shell=True,universal_newlines=True) as process:
#                         while True:
#                             output = process.stdout.readline()
#                             if output == '' and process.poll() is not None:
#                                 break
#                             if output:
#                                 print(output.strip())

            


# if __name__ == "__main__":
#     t1 = Thread(target=server)
#     t2 = Thread(target=client)
    
#     t1.start()
#     time.sleep(3)
#     t2.start()
#     # client()

# import threading
# from threading import Lock, Thread
# import argparse, socket
# import datetime
# import time
# import struct
# import multiprocessing
# Pitch_angle_s = ""  #俯仰角
# Yaw_angle_s = ""  #偏航角
# Roll_angle_s = ""  #翻滚角
# Node_x_s = ""
# Node_y_s = ""
# Node_z_s = ""
# Node_x_speed_s = ""
# Node_y_speed_s = ""
# Node_z_speed_s = ""
# Node_txt=[]
# ttf_abs = 'C:\Windows\Fonts\STSONG.TTF'

# def server(port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     print(sock.bind(('0.0.0.0', port)))
    
#     print('listening {}'.format(sock.getsockname()))
#     # a=1
#     while True:
#         data, address = sock.recvfrom(1024)
#         print(data)
#         # if a == 1:
#         print(node_data(data))
#         # a+=1
#         ehco='already received'.encode('ascii')
#         sock.sendto(ehco, address)
#     # message = [Pitch_angle_s, Yaw_angle_s, Roll_angle_s, Node_x_s, Node_y_s, Node_z_s, Node_x_speed_s, Node_y_speed_s, Node_z_speed_s]
#     # pipe.send(message)
    
# def client(port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     # text = 'the time is{}'.format(datetime.datetime.now())
#     text=b'\x01\x01\x01\x0f\xae\x87?k=\x8a?L\xb8\x9e?\x01\x00P\\G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x00\x00H\xc2\x02\x00P\\G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x00\x00H\xc2\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'


#     for i in range(2):
#         sock.sendto(text, ('127.0.0.1', port))
#         data, address = sock.recvfrom(1024)
#         text1 = data.decode('ascii')
#         print('the server {}replied {!r}'.format(address, text1))
    
# def node_data(udp_data):
#     Pitch_angle=[]
#     for i in range(4):
#         Pitch_angle.append(udp_data[3 + i])
#         print(Pitch_angle)
#     Pitch_angle_s = struct.unpack('<f',struct.pack('4B',*Pitch_angle))[0]
#     print("Pitch_angle is {}".format(Pitch_angle_s))

#     Yaw_angle=[]
#     for i in range(4):
#         Yaw_angle.append(udp_data[7+i])
#     Yaw_angle_s=struct.unpack('<f',struct.pack('4B',*Yaw_angle))[0]
#     print("Yaw_angle  is {}".format(Yaw_angle_s))

#     Roll_angle=[]
#     for i in range(4):
#         Roll_angle.append(udp_data[11+i])
#     Roll_angle_s=struct.unpack('<f',struct.pack('4B',*Roll_angle))[0]
#     print("Roll_angle is {}".format(Roll_angle_s))


#     print(str(udp_data[15]),"@@@")
#     if str(udp_data[15]) != '255':
        
#         print("node1 ID is  {}".format(str(udp_data[15])))
#         #-----------------节点坐标------------------------
#         Node1_x=[]
#         for i in range(4):
#             Node1_x.append(udp_data[16+i])
#         Node_x_s=struct.unpack('<f',struct.pack('4B',*Node1_x))[0]
#         print("Node_x is {}".format(Node_x_s))

#         Node1_y=[]
#         for i in range(4):
#             Node1_y.append(udp_data[20+i])
#         Node_y_s = struct.unpack('<f', struct.pack('4B', *Node1_y))[0]
#         print("Node_y is {}".format(Node_y_s))

#         Node1_z=[]
#         for i in range(4):
#             Node1_z.append(udp_data[24+i])
#         Node_z_s = struct.unpack('<f', struct.pack('4B', *Node1_z))[0]
#         print("Node_z is {}".format(Node_z_s))

#         #-----------------节点速度------------------------

#         Node1_x_speed=[]
#         for i in range(4):
#             Node1_x_speed.append(udp_data[28+i])
#         Node_x_speed_s=struct.unpack('<f',struct.pack('4B',*Node1_x_speed))[0]
#         print("Node_x_speed is {}".format(Node_x_speed_s))

#         Node1_y_speed=[]
#         for i in range(4):
#             Node1_y_speed.append(udp_data[32+i])
#         Node_y_speed_s=struct.unpack('<f',struct.pack('4B',*Node1_y_speed))[0]
#         print("Node_y_speed is {}".format(Node_y_speed_s))

#         Node1_z_speed=[]
#         for i in range(4):
#             Node1_z_speed.append(udp_data[36+i])
#         Node_z_speed_s=struct.unpack('<f',struct.pack('4B',*Node1_z_speed))[0]
#         print("Node_z_speed is {}".format(Node_z_speed_s))
#     else:
#         pass
 
#     # txt = ["俯仰角" + str(node1.Pitch_angle), " 偏航角" + str(node1.Yaw_angle), "翻滚角" + str(node1.Roll_angle),
#     #             "x:" + str(node1.Node_x), "y:" + str(node1.Node_y), "z:" + str(node1.Node_z),
#     #             "x速度:" + str(node1.Node_x_speed), "y速度:" + str(node1.Node_y_speed), "z速度:" + str(node1.Node_z_speed)]

#     # node1.Node_txt=[]#每次接受新的信息，归零
#     # for i in txt:
#     #     node1.Node_txt.append(fontObj.render(i, False, (0, 0, 0)))


# server = Thread(target=server, args=(23000,))
# client = Thread(target=client, args=(23000,))
# server.start()
# client.start()



# s_info={}
# s_info.update({'node1':{}})
# s_info.update({'node2':{}})
# s_info.update({'node3':{}})
                                
# for i in s_info:
#     s_info[i].update({'Pitch_angle':''})
#     s_info[i].update({'Yaw_angle':''})
#     s_info[i].update({'Roll_angle':''})
#     s_info[i].update({'x':''})
#     s_info[i].update({'y':''})
#     s_info[i].update({'z':''})
#     s_info[i].update({'x_speed':''})
#     s_info[i].update({'y_spped':''})
#     s_info[i].update({'z_speed':''})
#     s_info[i].update({'id':''})

# s_info['node1']['x']='123'
# print(s_info['node1']['x'])
# a=b'\x66\x56'
# b=b'\x01\x02'

# print(a[0])
# print(e,type(e))

# 输出十六进制类型数组

# l = [hex(int(i)) for i in c]
# print(" ".join(l))
# for i in c:
#     print("%X,"%ord(i))
a='000001000000000000000000000000010100000000007a440000fa4400c05a470000c8420000c8420000484302000000f3fff944f4fff94400c05a470000c8420000c8420000484303000000fcff7944fb7f3b4500c05a470000c8420000c842000048430100000000007a440000fa4400c05a470000c8420000c84200004843ffffffff000000000000000000000000000000000000000000000000ffffffff000000000000000000000000000000000000000000000000'
a=list(a)
print(a)
b='\\x'
temp=0
for i in range(len(a)):

    a.insert(temp,b)
    temp+=3

a_b=''.join(a)
print(a_b)