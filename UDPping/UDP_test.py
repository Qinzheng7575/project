import argparse
import socket
import datetime
import time
import struct
import multiprocessing
Pitch_angle_s = ""  # 俯仰角
Yaw_angle_s = ""  # 偏航角
Roll_angle_s = ""  # 翻滚角
Node_x_s = ""
Node_y_s = ""
Node_z_s = ""
Node_x_speed_s = ""
Node_y_speed_s = ""
Node_z_speed_s = ""
Node1_id = ""

Pitch2_angle_s = ""  # 俯仰角
Yaw2_angle_s = ""  # 偏航角
Roll2_angle_s = ""  # 翻滚角
Node2_x_s = ""
Node2_y_s = ""
Node2_z_s = ""
Node2_x_speed_s = ""
Node2_y_speed_s = ""
Node2_z_speed_s = ""
Node2_id = ""

Pitch3_angle_s = ""  # 俯仰角
Yaw3_angle_s = ""  # 偏航角
Roll3_angle_s = ""  # 翻滚角
Node3_x_s = ""
Node3_y_s = ""
Node3_z_s = ""
Node3_x_speed_s = ""
Node3_y_speed_s = ""
Node3_z_speed_s = ""
Node3_id = ""

s_info={}
now_node=""

Node_txt = []
ttf_abs = 'C:\Windows\Fonts\STSONG.TTF'


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))
    # print('listening {}'.format(sock.getsockname()))

    while True:
        data, address = sock.recvfrom(1024)
        # print(data)
        node_data(data)

        # ehco='already received'.encode('ascii')
        # sock.sendto(ehco, address)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = b'\x01\x01\x01\x0f\xae\x87?k=\x8a?L\xb8\x9e?\x01\x00P\\G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x00\x00H\xc2\x02\x00P\\G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x00\x00H\xc2\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    text2=b'\x00\x00\x01\x00\x00\x00'\
        b'\x00\x00\x00\x00\x00\x00\x00\x00'\
        b'\x00\x01\x01\x00\x00\x00\x00\x00'\
        b'\x7a\x44\x00\x00\xfa\x44\x00\xc0'\
        b'\x5a\x47\x00\x00\xc8\x42\x00\x00'\
        b'\xc8\x42\x00\x00\x48\x43\x02\x00'\
        b'\x00\x00\xf3\xff\xf9\x44\xf4\xff'\
        b'\xf9\x44\x00\xc0\x5a\x47\x00\x00'\
        b'\xc8\x42\x00\x00\xc8\x42\x00\x00'\
        b'\x48\x43\x03\x00\x00\x00\xfc\xff'\
        b'\x79\x44\xfb\x7f\x3b\x45\x00\xc0'\
        b'\x5a\x47\x00\x00\xc8\x42\x00\x00'\
        b'\xc8\x42\x00\x00\x48\x43\x01\x00'\
        b'\x00\x00\x00\x00\x7a\x44\x00\x00'\
        b'\xfa\x44\x00\xc0\x5a\x47\x00\x00'\
        b'\xc8\x42\x00\x00\xc8\x42\x00\x00'\
        b'\x48\x43\xff\xff\xff\xff\x00\x00'\
        b'\x00\x00\x00\x00\x00\x00\x00\x00'\
        b'\x00\x00\x00\x00\x00\x00\x00\x00'\
        b'\x00\x00\x00\x00\x00\x00\xff\xff'\
        b'\xff\xff\x00\x00\x00\x00\x00\x00'\
        b'\x00\x00\x00\x00\x00\x00\x00\x00'\
        b'\x00\x00\x00\x00\x00\x00\x00\x00'\
        b'\x00\x00'


    # udp_data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10\x11\x12\x13\x14\x15'\
    #     b'\x16\x17\x18\x19\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x30\x31'\
    #     b'\x32\x33\x34\x35\x36\x37\x38\x39'
    for i in range(5):
        sock.sendto(text2, ('127.0.0.1', port))
    # data, address = sock.recvfrom(1024)
    # text1 = data.decode('ascii')
    # print('the server {}replied {!r}'.format(address, text1))

    # time.sleep(4)
    # sock.sendto(udp_data, ('127.0.0.1', port))


def node_data(udp_data):
    global Pitch_angle_s
    global Yaw_angle_s
    global Roll_angle_s

    global Node_x_s
    global Node_y_s
    global Node_z_s
    global Node_x_speed_s
    global Node_y_speed_s
    global Node_z_speed_s
    global Node1_id
    
    global Node2_x_s
    global Node2_y_s
    global Node2_z_s
    global Node2_x_speed_s
    global Node2_y_speed_s
    global Node2_z_speed_s
    global Node2_id

    global Node3_x_s
    global Node3_y_s
    global Node3_z_s
    global Node3_x_speed_s
    global Node3_y_speed_s
    global Node3_z_speed_s
    global Node3_id

    global s_info
    global now_node
    s_info.update({'node1':{}})
    s_info.update({'node2':{}})
    s_info.update({'node3':{}})
                                    
    for i in s_info:
        s_info[i].update({'id':''})        
        s_info[i].update({'x':''})
        s_info[i].update({'y':''})
        s_info[i].update({'z':''})
        s_info[i].update({'x_speed':''})
        s_info[i].update({'y_speed':''})
        s_info[i].update({'z_speed':''})


    # ------S节点1---------------------------
    if len(udp_data) > 89:
        if str(udp_data[91]) != '255':
            s_info['node1']['id']='1'
            # -----------------节点坐标------------------------
            Node_x = []
            for i in range(4):
                Node_x.append(udp_data[92+i])
            s_info['node1']['x'] = struct.unpack('<f', struct.pack('4B', *Node_x))[0]

            Node_y = []
            for i in range(4):
                Node_y.append(udp_data[96+i])
            s_info['node1']['y'] = struct.unpack('<f', struct.pack('4B', *Node_y))[0]

            Node_z = []
            for i in range(4):
                Node_z.append(udp_data[100+i])
            s_info['node1']['z'] = struct.unpack('<f', struct.pack('4B', *Node_z))[0]

            # -----------------节点速度------------------------
            c=udp_data[112]+udp_data[113]+udp_data[114]+udp_data[115]
            # print('@@@@',type(udp_data))
            # print('*********',udp_data[112],udp_data[113],udp_data[114],udp_data[115])
            # print('@@@@',udp_data[112].hex(),udp_data[113].hex(),udp_data[114].hex(),udp_data[115].hex())
            # print('********',c.hex())
            # l = [hex(int(i)) for i in c]
            # print('**************',c)
            # print(" ".join(l))





            Node_x_speed = []
            for i in range(4):
                Node_x_speed.append(udp_data[104+i])
                
            s_info['node1']['x_speed'] = struct.unpack('<f', struct.pack('4B', *Node_x_speed))[0]

            Node_y_speed = []
            for i in range(4):
                Node_y_speed.append(udp_data[108+i])
            s_info['node1']['y_speed'] = struct.unpack('<f', struct.pack('4B', *Node_y_speed))[0]

            Node_z_speed = []
            for i in range(4):
                Node_z_speed.append(udp_data[112+i])
            s_info['node1']['z_speed'] = struct.unpack('<f', struct.pack('4B', *Node_z_speed))[0]
            
        else:
            s_info['node1']['id'] = "-1"




    # ------S节点2---------------------------
    if len(udp_data) > 114:
        if str(udp_data[116]) != '255':
            s_info['node2']['id']='1'
            # -----------------节点坐标------------------------
            Node_x = []
            for i in range(4):
                Node_x.append(udp_data[117+i])
            s_info['node2']['x'] = struct.unpack('<f', struct.pack('4B', *Node_x))[0]

            Node_y = []
            for i in range(4):
                Node_y.append(udp_data[121+i])
            s_info['node2']['y'] = struct.unpack('<f', struct.pack('4B', *Node_y))[0]

            Node_z = []
            for i in range(4):
                Node_z.append(udp_data[125+i])
            s_info['node2']['z'] = struct.unpack('<f', struct.pack('4B', *Node_z))[0]

            # -----------------节点速度------------------------
            Node_x_speed = []
            for i in range(4):
                Node_x_speed.append(udp_data[129+i])
            s_info['node2']['x_speed'] = struct.unpack('<f', struct.pack('4B', *Node_x_speed))[0]

            Node_y_speed = []
            for i in range(4):
                Node_y_speed.append(udp_data[133+i])
            s_info['node2']['y_speed'] = struct.unpack('<f', struct.pack('4B', *Node_y_speed))[0]

            Node_z_speed = []
            for i in range(4):
                Node_z_speed.append(udp_data[137+i])
            s_info['node2']['z_speed'] = struct.unpack('<f', struct.pack('4B', *Node_z_speed))[0]

        else:
            s_info['node2']['id'] = "-1"



    # ------S节点3---------------------------
    if len(udp_data) > 139:
        if str(udp_data[141]) != '255':
            s_info['node3']['id']='1'
            # -----------------节点坐标------------------------
            Node_x = []
            for i in range(4):
                Node_x.append(udp_data[142+i])
            s_info['node3']['x'] = struct.unpack('<f', struct.pack('4B', *Node_x))[0]

            Node_y = []
            for i in range(4):
                Node_y.append(udp_data[146+i])
            s_info['node3']['y'] = struct.unpack('<f', struct.pack('4B', *Node_y))[0]

            Node_z = []
            for i in range(4):
                Node_z.append(udp_data[150+i])
            s_info['node3']['z'] = struct.unpack('<f', struct.pack('4B', *Node_z))[0]

            # -----------------节点速度------------------------
            Node_x_speed = []
            for i in range(4):
                Node_x_speed.append(udp_data[154+i])
            s_info['node3']['x_speed'] = struct.unpack('<f', struct.pack('4B', *Node_x_speed))[0]

            Node_y_speed = []
            for i in range(4):
                Node_y_speed.append(udp_data[158+i])
            s_info['node3']['y_speed'] = struct.unpack('<f', struct.pack('4B', *Node_y_speed))[0]

            Node_z_speed = []
            for i in range(4):
                Node_z_speed.append(udp_data[162+i])
            s_info['node3']['z_speed'] = struct.unpack('<f', struct.pack('4B', *Node_z_speed))[0]

        else:
            s_info['node3']['id'] = "-1"









    #当前选择的节点名
    now_node=str(udp_data[15])

    Pitch_angle = []
    for i in range(4):
        Pitch_angle.append(udp_data[3 + i])
        # print(Pitch_angle)
    Pitch_angle_s = struct.unpack('<f', struct.pack('4B', *Pitch_angle))[0]
    # print("Pitch_angle is {}".format(Pitch_angle_s))

    Yaw_angle = []
    for i in range(4):
        Yaw_angle.append(udp_data[7+i])
    Yaw_angle_s = struct.unpack('<f', struct.pack('4B', *Yaw_angle))[0]
    # print("Yaw_angle  is {}".format(Yaw_angle_s))

    Roll_angle = []
    for i in range(4):
        Roll_angle.append(udp_data[11+i])
    Roll_angle_s = struct.unpack('<f', struct.pack('4B', *Roll_angle))[0]
    # print("Roll_angle is {}".format(Roll_angle_s))

    # print(str(udp_data[15]))
    if str(udp_data[16]) != '255':
        Node1_id = "1"
        # print("node1 ID is  {}".format(str(udp_data[15])))

        # -----------------节点坐标------------------------
        Node1_x = []
        for i in range(4):
            Node1_x.append(udp_data[17+i])
        Node_x_s = struct.unpack('<f', struct.pack('4B', *Node1_x))[0]
        Node_x_s=round(Node_x_s,3)
        # print("Node_x is {}".format(Node_x_s))

        Node1_y = []
        for i in range(4):
            Node1_y.append(udp_data[21+i])
        Node_y_s = struct.unpack('<f', struct.pack('4B', *Node1_y))[0]
        Node_y_s=round(Node_y_s,3)
        # print("Node_y is {}".format(Node_y_s))

        Node1_z = []
        for i in range(4):
            Node1_z.append(udp_data[25+i])
        Node_z_s = struct.unpack('<f', struct.pack('4B', *Node1_z))[0]
        Node_z_s=round(Node_z_s,3)
        # print("Node_z is {}".format(Node_z_s))

        # -----------------节点速度------------------------

        Node1_x_speed = []
        for i in range(4):
            Node1_x_speed.append(udp_data[29+i])
        Node_x_speed_s = struct.unpack('<f', struct.pack('4B', *Node1_x_speed))[0]
        Node_x_speed_s=round(Node_x_speed_s,3)
        # print("Node_x_speed is {}".format(Node_x_speed_s))

        Node1_y_speed = []
        for i in range(4):
            Node1_y_speed.append(udp_data[33+i])
        Node_y_speed_s = struct.unpack('<f', struct.pack('4B', *Node1_y_speed))[0]
        Node_y_speed_s=round(Node_y_speed_s,3)
        # print("Node_y_speed is {}".format(Node_y_speed_s))

        Node1_z_speed = []
        for i in range(4):
            Node1_z_speed.append(udp_data[37+i])
        Node_z_speed_s = struct.unpack('<f', struct.pack('4B', *Node1_z_speed))[0]
        Node_z_speed_s=round(Node_z_speed_s,3)
        # print("Node_z_speed is {}".format(Node_z_speed_s))
    else:
        Node1_id = "-1"

    # ------------------------节点二---------------------
    # ------------------------节点二---------------------
    if len(udp_data) > 42:
        if str(udp_data[41]) != '255':
            Node2_id = "1"

            # -----------------节点坐标------------------------
            Node2_x = []
            for i in range(4):
                Node2_x.append(udp_data[42+i])
            Node2_x_s = struct.unpack('<f', struct.pack('4B', *Node2_x))[0]
            Node2_x_s=round(Node2_x_s,3)


            Node2_y = []
            for i in range(4):
                Node2_y.append(udp_data[46+i])
            Node2_y_s = struct.unpack('<f', struct.pack('4B', *Node2_y))[0]
            Node2_y_s=round(Node2_y_s,3)

            Node2_z = []
            for i in range(4):
                Node2_z.append(udp_data[50+i])
            Node2_z_s = struct.unpack('<f', struct.pack('4B', *Node2_z))[0]
            Node2_z_s=round(Node2_z_s,3)

            # -----------------节点sus速度------------------------
            Node2_x_speed = []
            for i in range(4):
                Node2_x_speed.append(udp_data[51+i])
            Node2_x_speed_s = struct.unpack('<f', struct.pack('4B', *Node2_x_speed))[0]
            Node2_x_speed_s=round(Node2_x_speed_s,3)

            Node2_y_speed = []
            for i in range(4):
                Node2_y_speed.append(udp_data[58+i])
            Node2_y_speed_s = struct.unpack('<f', struct.pack('4B', *Node2_y_speed))[0]
            Node2_y_speed_s=round(Node2_y_speed_s,3)

            Node2_z_speed = []
            for i in range(4):
                Node2_z_speed.append(udp_data[62+i])
            Node2_z_speed_s = struct.unpack('<f', struct.pack('4B', *Node2_z_speed))[0]
            Node2_z_speed_s=round(Node2_x_speed_s,3)

        else:
            Node2_id = "-1"

    # ------------------------节点三---------------------
    # ------------------------节点三---------------------
    if len(udp_data) > 70:
        if str(udp_data[66]) != '255':
            Node3_id = "1"

            # -----------------节点坐标------------------------
            Node3_x = []
            for i in range(4):
                Node3_x.append(udp_data[67+i])
            Node3_x_s = struct.unpack('<f', struct.pack('4B', *Node3_x))[0]

            Node3_y = []
            for i in range(4):
                Node3_y.append(udp_data[71+i])
            Node3_y_s = struct.unpack('<f', struct.pack('4B', *Node3_y))[0]

            Node3_z = []
            for i in range(4):
                Node3_z.append(udp_data[75+i])
            Node3_z_s = struct.unpack('<f', struct.pack('4B', *Node3_z))[0]

            # -----------------节点速度------------------------
            Node3_x_speed = []
            for i in range(4):
                Node3_x_speed.append(udp_data[79+i])
            Node3_x_speed_s = struct.unpack('<f', struct.pack('4B', *Node3_x_speed))[0]

            Node3_y_speed = []
            for i in range(4):
                Node3_y_speed.append(udp_data[83+i])
            Node3_y_speed_s = struct.unpack('<f', struct.pack('4B', *Node3_y_speed))[0]

            Node3_z_speed = []
            for i in range(4):
                Node3_z_speed.append(udp_data[87+i])
            Node3_z_speed_s = struct.unpack('<f', struct.pack('4B', *Node3_z_speed))[0]

        else:
            Node3_id = "-1"

    # print(Pitch_angle_s, Yaw_angle_s, Roll_angle_s, 
    # Node_x_s, Node_y_s, Node_z_s, Node_x_speed_s, Node_y_speed_s, Node_z_speed_s, Node1_id,
    # Node2_x_s, Node2_y_s, Node2_z_s, Node2_x_speed_s, Node2_y_speed_s, Node2_z_speed_s, Node2_id,
    # Node3_x_s, Node3_y_s, Node3_z_s, Node3_x_speed_s, Node3_y_speed_s, Node3_z_speed_s, Node3_id,
    # s_info['node1']['id'],'s_node1 pos:',s_info['node1']['x'],s_info['node1']['y'],s_info['node1']['z'],'s_node1 speed:',s_info['node1']['x_speed'],s_info['node1']['y_speed'],s_info['node1']['z_speed'],
    # s_info['node2']['id'],s_info['node2']['x'],s_info['node2']['y'],s_info['node2']['z'],s_info['node2']['x_speed'],s_info['node2']['y_speed'],s_info['node2']['z_speed'],
    # s_info['node3']['id'],s_info['node3']['x'],s_info['node3']['y'],s_info['node3']['z'],s_info['node3']['x_speed'],s_info['node3']['y_speed'],s_info['node3']['z_speed'])


    print(Pitch_angle_s, Yaw_angle_s, Roll_angle_s, 
    Node_x_s, Node_y_s, Node_z_s, Node_x_speed_s, Node_y_speed_s, Node_z_speed_s, Node1_id,
    Node2_x_s, Node2_y_s, Node2_z_s, Node2_x_speed_s, Node2_y_speed_s, Node2_z_speed_s, Node2_id,
    Node3_x_s, Node3_y_s, Node3_z_s, Node3_x_speed_s, Node3_y_speed_s, Node3_z_speed_s, Node3_id,
    now_node,s_info['node1']['id'],s_info['node2']['id'],s_info['node3']['id'])
    # print(Pitch_angle_s, Yaw_angle_s, Roll_angle_s, 
    # s_info['node1']['x'], s_info['node1']['y'],  s_info['node1']['z'], s_info['node1']['x_speed'], s_info['node1']['y_speed'], s_info['node1']['z_speed'], Node1_id,
    # Node2_x_s, Node2_y_s, Node2_z_s, Node2_x_speed_s, Node2_y_speed_s, Node2_z_speed_s, Node2_id,
    # Node3_x_s, Node3_y_s, Node3_z_s, Node3_x_speed_s, Node3_y_speed_s, Node3_z_speed_s, Node3_id,
    # now_node,s_info['node1']['id'],s_info['node2']['id'],s_info['node3']['id'])



if __name__ == "__main__":
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(
        description='send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int,
                        default=23000, help='UDP port (default 23000)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
