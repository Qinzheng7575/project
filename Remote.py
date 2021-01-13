import struct
import multiprocessing
from multiprocessing import Pipe 
import socket
import subprocess

class remote:
    txt=[]

    Pitch_angle = ""  #俯仰角
    Yaw_angle = ""  #偏航角
    Roll_angle = ""  #翻滚角
    Node_x = ""
    Node_y = ""
    Node_z = ""
    Node_x_speed = ""
    Node_y_speed = ""
    Node_z_speed = ""
    Node1_id=""

    Node2_x = ""
    Node2_y = ""
    Node2_z = ""
    Node2_x_speed = ""
    Node2_y_speed = ""
    Node2_z_speed = ""
    Node2_id = ""

    Node3_x = ""
    Node3_y = ""
    Node3_z = ""
    Node3_x_speed = ""
    Node3_y_speed = ""
    Node3_z_speed = ""
    Node3_id = ""

    now_node=""
    s_node1=""
    s_node2=""
    s_node3=""



    Nighbour_v = {"12": 0, "13": 0, "23": 0}
    Nighbour_s = {"12": 0, "13": 0, "23": 0}

    def UDP_test_server(self,pipe):

        with subprocess.Popen(["UDP_test.py","server"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
            while True:
                # print("doing server")
                output = process.stdout.readline()
                # print(type(output))
                if output == '' and process.poll() is not None:
                    break
                if output:
                    message=output.strip()
                    # print(message)
                    pipe.send(message)
                    # self.udp_data=
                    # self.txt.append(output.strip())
            rc = process.poll()


    def pipe_begin(self):#建立pipe
        parent_conn, child_conn=Pipe()

        fa= multiprocessing.Process(target=self.UDP_test_server,  kwargs={'self':self,'pipe':child_conn})
        #https://www.cnblogs.com/wangm-0824/p/10267977.html
        fa.start()
        flag=1
        while True:
            temp = parent_conn.recv()
            temp=temp.split()

            # print('receive data is:',temp)
            if flag==1:


                self.Pitch_angle = temp[0]
                self.Yaw_angle=temp[1]
                self.Roll_angle = temp[2]
                self.Node_x = temp[3]
                self.Node_y=temp[4]
                self.Node_z = temp[5]
                self.Node_x_speed = temp[6]
                self.Node_y_speed = temp[7]
                self.Node_z_speed = temp[8]
                self.Node1_id = temp[9]

 
                self.Node2_x = temp[10]
                self.Node2_y=temp[11]
                self.Node2_z = temp[12]
                self.Node2_x_speed = temp[13]
                self.Node2_y_speed = temp[14]
                self.Node2_z_speed = temp[15]
                self.Node2_id = temp[16]

                self.Node3_x = temp[17]
                self.Node3_y=temp[18]
                self.Node3_z = temp[19]
                self.Node3_x_speed = temp[20]
                self.Node3_y_speed = temp[21]
                self.Node3_z_speed = temp[22]
                self.Node3_id = temp[23]

                self.now_node=temp[24]
                # print(self.now_node)
                self.s_node1=temp[25]
                self.s_node2=temp[26]
                self.s_node3=temp[27]
                
                # if self.Node1_id=='1' and self.Node2_id=='1':
                #     self.Nighbour["12"]=1
                # if self.Node1_id=='1' and self.Node3_id=='1':
                #     self.Nighbour["13"]=1
                # if self.Node3_id=='1' and self.Node2_id=='1':
                #     self.Nighbour["23"]=1

                #现在邻接表的选择也由S状态决定
                if self.s_node1=='1' and self.s_node2=='1':
                    self.Nighbour_v["12"]=1
                    self.Nighbour_s["12"]=1
                if self.s_node1=='1' and self.s_node3=='1':
                    self.Nighbour_v["13"]=1
                    self.Nighbour_s["13"]=1
                if self.s_node3=='1' and self.s_node2=='1':
                    self.Nighbour_v["23"]=1
                    self.Nighbour_s["23"]=1


                flag+=1
            elif flag==2:
                flag+=1
            elif flag==3:
                flag==1

 




    # def node_data_s(self,udp_data):
    #     Pitch_angle=[]
    #     for i in range(4):
    #         Pitch_angle.append(udp_data[3 + i])
    #         # print(Pitch_angle)
    #     self.Pitch_angle = struct.unpack('<f',struct.pack('4B',*Pitch_angle))[0]
    #     print("Pitch_angle is {}".format(self.Pitch_angle))

    #     Yaw_angle=[]
    #     for i in range(4):
    #         Yaw_angle.append(udp_data[7+i])
    #     self.Yaw_angle=struct.unpack('<f',struct.pack('4B',*Yaw_angle))[0]
    #     print("Yaw_angle  is {}".format(self.Yaw_angle))

    #     Roll_angle=[]
    #     for i in range(4):
    #         Roll_angle.append(udp_data[11 + i])
    #     self.Roll_angle=struct.unpack('<f',struct.pack('4B',*Roll_angle))[0]
    #     print("Roll_angle is {}".format(self.Roll_angle))


    #     # print(str(udp_data[15]))
    #     if str(udp_data[15]) != '255':
            
    #         print("node1 ID is  {}".format(str(udp_data[15])))
    #         #-----------------节点坐标------------------------
    #         Node1_x=[]
    #         for i in range(4):
    #             Node1_x.append(udp_data[16+i])
    #         self.Node_x=struct.unpack('<f',struct.pack('4B',*Node1_x))[0]
    #         print("Node_x is {}".format(self.Node_x))

    #         Node1_y=[]
    #         for i in range(4):
    #             Node1_y.append(udp_data[20+i])
    #         self.Node_y = struct.unpack('<f', struct.pack('4B', *Node1_y))[0]
    #         print("Node_y is {}".format(self.Node_y))

    #         Node1_z=[]
    #         for i in range(4):
    #             Node1_z.append(udp_data[24+i])
    #         self.Node_z = struct.unpack('<f', struct.pack('4B', *Node1_z))[0]
    #         print("Node_z is {}".format(self.Node_z))

    #         #-----------------节点速度------------------------

    #         Node1_x_speed=[]
    #         for i in range(4):
    #             Node1_x_speed.append(udp_data[28+i])
    #         self.Node_x_speed=struct.unpack('<f',struct.pack('4B',*Node1_x_speed))[0]
    #         print("Node_x_speed is {}".format(self.Node_x_speed))

    #         Node1_y_speed=[]
    #         for i in range(4):
    #             Node1_y_speed.append(udp_data[32+i])
    #         self.Node_y_speed=struct.unpack('<f',struct.pack('4B',*Node1_y_speed))[0]
    #         print("Node_y_speed is {}".format(self.Node_y_speed))

    #         Node1_z_speed=[]
    #         for i in range(4):
    #             Node1_z_speed.append(udp_data[36+i])
    #         self.Node_z_speed=struct.unpack('<f',struct.pack('4B',*Node1_z_speed))[0]
    #         print("Node_z_speed is {}".format(self.Node_z_speed))
    #     else:
    #         pass
    
    #     # txt = ["俯仰角" + str(node1.Pitch_angle), " 偏航角" + str(node1.Yaw_angle), "翻滚角" + str(node1.Roll_angle),
    #     #             "x:" + str(node1.Node_x), "y:" + str(node1.Node_y), "z:" + str(node1.Node_z),
    #     #             "x速度:" + str(node1.Node_x_speed), "y速度:" + str(node1.Node_y_speed), "z速度:" + str(node1.Node_z_speed)]

    #     # node1.Node_txt=[]#每次接受新的信息，归零
    #     # for i in txt:
    #     #     node1.Node_txt.append(fontObj.render(i, False, (0, 0, 0)))

