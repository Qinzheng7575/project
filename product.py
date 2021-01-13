import pygame
from pygame.locals import *
import time, os,sys
import threading
from threading import Lock, Thread
import items
import multiprocessing
from multiprocessing import Pipe as guandao
import platform
import Remote
 

if __name__ == "__main__":
    pipe = guandao()

    node1 = items.Node(750, 200)
    node2 =  items.Node(550,120)
    node3 = items.Node(980, 120)


    api = items.Api_need
    remote=Remote.remote
    # pipe = multiprocessing.Pipe()
    loding_flag=0
    V_waiting_flag=0
    BK_flag=1
    S_flag=0

    V_num=999

    pygame.init()
    screen = pygame.display.set_mode((1200, 700), 0, 32)
    pygame.display.set_caption("测试界面")
    background1 = pygame.image.load('D:\ForStudy\python练习\练习\项目\img\\background.png')
    background1 = pygame.transform.scale(background1, (1200, 700))
    Ceshi_1 = items.Button('Ceshi1.png','Ceshi1_g.png')
    Ceshi_2 =items.Button('Ceshi2.png','Ceshi2_g.png')
    Ceshi_3 =items.Button('Ceshi3.png','Ceshi3_g.png')
    Ceshi_4=items.Button('Ceshi4.png','Ceshi4_g.png')
    Ceshi_5 = items.Button('Ceshi5.png', 'Ceshi5_g.png')
    Ceshi_6=items.Button('Ceshi6.png','Ceshi6_g.png')

    #文字
    myfront  = pygame.font.Font(api.ttf_abs, 19)

    #开局就打开监听
    server = Thread(target=remote.pipe_begin, args=(remote,))
    server.start()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 接收到退出时间后退出程序
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  #点击鼠标
                # if event.button == 1:
                #     node1.y += 50
                if event.button == 3: 
                    # api.node_data(api,api.udp_data,node1,node2,node3)
                    print(remote.txt)

                if event.button == 2:#清零
                    BK_flag = 1
                    node1.if_click = 0
                    node2.if_click = 0
                    node3.if_click = 0
                    Ceshi_1.if_click = 0
                    Ceshi_2.if_click = 0
                    Ceshi_3.if_click = 0
                    Ceshi_4.if_click = 0
                    Ceshi_5.if_click = 0
                    Ceshi_6.if_click=0


                #点击事件——V段

                if (event.pos[0] > (Ceshi_1.BT_rect.left + 50) and event.pos[0] < (Ceshi_1.BT_rect.right + 50) and event.pos[1] > (Ceshi_1.BT_rect.top + 90) and event.pos[1] < (Ceshi_1.BT_rect.bottom + 90)):
                    print("click 1")
                    BK_flag=2
                    S_flag=0
                    Ceshi_1.if_click = 1
                    Ceshi_2.if_click = 0
                    Ceshi_3.if_click=0



                #************S段*******************
                if (event.pos[0] > (Ceshi_2.BT_rect.left + 50) and event.pos[0] < (Ceshi_2.BT_rect.right + 50) and event.pos[1] > (Ceshi_2.BT_rect.top + 170) and event.pos[1] < (Ceshi_2.BT_rect.bottom + 170)):
                    print("click 2")
                    BK_flag=2
                    S_flag=1
                    Ceshi_2.if_click = 1
                    Ceshi_1.if_click = 0
                    Ceshi_3.if_click=0
                if (event.pos[0] > (Ceshi_3.BT_rect.left + 50) and event.pos[0] < (Ceshi_3.BT_rect.right + 50) and event.pos[1] > (Ceshi_3.BT_rect.top + 250) and event.pos[1] < (Ceshi_3.BT_rect.bottom + 250)):
                    print("click 3")
                    BK_flag=3
                    Ceshi_3.if_click = 1
                    Ceshi_1.if_click = 0
                    Ceshi_2.if_click = 0

                #点击事件——测试服务器
                if (event.pos[0] > (Ceshi_4.BT_rect.left + 50) and event.pos[0] < (Ceshi_4.BT_rect.right + 50) and event.pos[1] > (Ceshi_4.BT_rect.top + 430) and event.pos[1] < (Ceshi_4.BT_rect.bottom + 430)):
                    print("click 4")
                    node2.if_click = 1
                    node3.if_click = 0
                    
                    Ceshi_4.if_click = 1
                    Ceshi_5.if_click = 0
                    Ceshi_6.if_click = 0
                    V_waiting_flag=1#显示等待回复
                    if S_flag==0:
                        #监听回复报文
                        V_listen=Thread(target=api.V_config_server_receive, args=(api,))
                        V_listen.start()
                        print('V is listening')
                        #发送配置报文
                        # time.sleep(1)
                        # V_send=Thread(target=api.V_config_server_send, args=(api,))
                        # V_send.start()

                    #---------------------
                    else:
                        S_listen=Thread(target=api.S_config_server_receive, args=(api,))
                        S_listen.start()
                        print('S is listening')
                        #发送配置报文
                        time.sleep(1)
                        S_send=Thread(target=api.S_config_server_send, args=(api,))
                        S_send.start()
                    

 
                #测试客户端
                if (event.pos[0] > (Ceshi_5.BT_rect.left + 50) and event.pos[0] < (Ceshi_5.BT_rect.right + 50) and event.pos[1] > (Ceshi_5.BT_rect.top + 515) and event.pos[1] < (Ceshi_5.BT_rect.bottom + 515)):
                    print("click 5")
                    node2.if_click = 0
                    node3.if_click = 1

                    Ceshi_5.if_click = 1
                    Ceshi_4.if_click = 0
                    Ceshi_6.if_click = 0

                    V_waiting_flag=1#显示等待回复
                    #监听回复报文
                    V_listen=Thread(target=api.V_config_client_receive, args=(api,))
                    V_listen.start()
                    print('listening')
                    #发送配置报文
                    time.sleep(1)
                    V_send=Thread(target=api.V_config_client_send, args=(api,))
                    V_send.start()
                    # loding_flag=1#显示测试中
                    # client = Thread(target=api.client, args=(api, screen,))
                    # client.start()


                if (event.pos[0] > (Ceshi_6.BT_rect.left + 50) and event.pos[0] < (Ceshi_6.BT_rect.right + 50) and event.pos[1] > (Ceshi_6.BT_rect.top + 600) and event.pos[1] < (Ceshi_6.BT_rect.bottom + 600)):
                    print("click 6")
                    api.kill(api,'23000')
                    # api.kill(api,'12000')
                    # api.kill(api,'11000')
                    api.kill(api,'24600')

                    BK_flag = 1
                    S_flag=0
                    node1.if_click = 0
                    node2.if_click = 0
                    node3.if_click = 0
                    Ceshi_1.if_click = 0
                    Ceshi_2.if_click = 0
                    Ceshi_3.if_click = 0
                    Ceshi_4.if_click = 0
                    Ceshi_5.if_click = 0
                    Ceshi_6.if_click=0
                    loding_flag=0
                    api.V_num=0

        #以下为显示部分——————————————
        screen.blit(background1, (0, 0))
        items.draw_button(screen, Ceshi_1, (50, 90))
        items.draw_button(screen, Ceshi_2, (50, 170))
        items.draw_button(screen, Ceshi_3, (50, 250))      
        items.draw_button(screen, Ceshi_4, (50, 460))
        items.draw_button(screen, Ceshi_5, (50, 535))
        items.draw_button(screen, Ceshi_6, (50, 610))         



        if BK_flag == 2 :

            # 打印输出
            if api.render != []:
                # print(api.render)
                loding_flag=0
                for i in range(len(api.render)):
                    screen.blit(api.render[i], (460, 470 + 23 * i))
            elif loding_flag==1:
                font_loding = pygame.font.Font(api.ttf_abs, 30)
                text_big1 = font.render("配置中", 1, (255, 10, 10))
                screen.blit(text_big1,(700,500))

            font_Vstate=pygame.font.Font(api.ttf_abs, 13)
            text_big1 = font_Vstate.render("节点状态", 1, (255, 10, 10))
            screen.blit(text_big1,(832,407))


            if api.V_num or api.S_num==0:
                pygame.draw.circle(screen,[255,0,0],[900,415],10,0)
            else:
                pygame.draw.circle(screen,[0,255,97],[900,415],10,0)
            # print(api.V_if_iperf)
            if api.V_if_iperf or api.S_if_iperf==1:
                print('该iperf了！')
                api.V_if_iperf =0
                api.S_if_iperf=0





            if len(api.render)>=3:
                V_waiting_flag=0
            elif V_waiting_flag==1:
                pygame.draw.rect(screen,[200,200,200],[570,220,250,120],0)

                font_loding = pygame.font.Font(api.ttf_abs, 30)
                text_big1 = font.render("等待回复中", 1, (0, 0, 0))
                screen.blit(text_big1,(600,250))


            #节点显示与变色
            #根据S段信息点亮
            if remote.now_node=='1':
                node1.if_click=1
            elif remote.now_node=='2':
                node2.if_click=1
            elif remote.now_node=='3':
                node3.if_click=1


            if remote.Node2_id=='1':
                if node2.if_click == 0:
                    screen.blit(node2.Node_init, (node2.x, node2.y))
                else:
                    screen.blit(node2.Node_g, (node2.x, node2.y))

            if remote.Node3_id=='1':
                if node3.if_click == 0: 
                    screen.blit(node3.Node_init, (node3.x, node3.y))
                else:
                    screen.blit(node3.Node_g, (node3.x, node3.y))

            #拓扑连线部分
            if remote.Node3_id=='1' and remote.Node2_id=='1':
                remote.Nighbour_v["23"]=1
                remote.Nighbour_s["23"]=1



            items.draw_Connect(remote.Nighbour_v,remote.Nighbour_s,screen,node1,node2,node3,BK_flag)

            #文字通用显示（V段不显示）==========================
            # texttxt2=[]
            # texttxt2.append(myfront.render("坐标(x:{},y:{},z:{})".format(remote.Node2_x,remote.Node2_y,remote.Node2_z),False,(0,0,0)))
            # texttxt2.append(myfront.render("速度(x:{},y:{},z:{})".format(remote.Node2_x_speed,remote.Node2_y_speed,remote.Node2_z_speed),False,(0,0,0)))
            # for i in range(len(texttxt2)):
            #     screen.blit(texttxt2[i], (node2.x - 50, node2.y - 42  + 20 * i))

            # texttxt3=[]
            # texttxt3.append(myfront.render("坐标(x:{},y:{},z:{})".format(remote.Node3_x,remote.Node3_y,remote.Node3_z),False,(0,0,0)))
            # texttxt3.append(myfront.render("速度(x:{},y:{},z:{})".format(remote.Node3_x_speed,remote.Node3_y_speed,remote.Node3_z_speed),False,(0,0,0)))
            # for i in range(len(texttxt3)):
            #     screen.blit(texttxt3[i],(node3.x-10,node3.y- 42 +20*i))
            #=================================================



            # texttxt=[]
            # texttxt.append(myfront.render("俯仰角{}".format(remote.Pitch_angle),False,(0,0,0)))
            # texttxt.append(myfront.render("偏航角 {}".format(remote.Yaw_angle),False,(0,0,0)))
            # texttxt.append(myfront.render("翻滚角 {}".format(remote.Roll_angle),False,(0,0,0)))
            # texttxt.append(myfront.render("坐标(x:{},y:{},z:{})".format(remote.Node_x,remote.Node_y,remote.Node_z),False,(0,0,0)))
            # texttxt.append(myfront.render("速度(x:{},y:{},z:{})".format(remote.Node_x_speed,remote.Node_y_speed,remote.Node_z_speed),False,(0,0,0)))
            # for i in range(len(texttxt)):
            #     screen.blit(texttxt[i],(node1.x-20,node1.y+70+20*i))





        if BK_flag == 3:#界面3
            right_top1 = pygame.font.Font(api.ttf_abs, 20)
            right_top_txt1 = right_top1.render("—  :V段", 1, (10, 10, 10))
            screen.blit(right_top_txt1,(1095,30))

            right_top_txt2 = right_top1.render("—  :S段", 1, (255, 10, 10))
            screen.blit(right_top_txt2,(1095,50))

            #节点显示
            # print(remote.s_node1,remote.s_node2,remote.s_node3)

            if remote.now_node=='1':
                # print(remote.now_node,type(remote.now_node))                
                node1.if_click=1
            elif remote.now_node=='2':
                node2.if_click=1
            elif remote.now_node=='3':
                node3.if_click=1



            if node1.if_click==1:
                screen.blit(node1.Node_g, (node1.x, node1.y))
            else:
                screen.blit(node1.Node_init, (node1.x, node1.y))  #中间的暂时没有变色


            if node2.if_click == 0:
                screen.blit(node2.Node_init, (node2.x, node2.y))
            else:
                screen.blit(node2.Node_g, (node2.x, node2.y))


            if node3.if_click == 0: 
                screen.blit(node3.Node_init, (node3.x, node3.y))
            else:
                screen.blit(node3.Node_g, (node3.x, node3.y))

            # print(remote.s_node1,remote.s_node2,remote.s_node3,type(remote.s_node1))
            #连线显示
            if remote.Node1_id=='1' and remote.Node2_id=='1':
                remote.Nighbour_v["12"]=1
            if remote.Node1_id=='1' and remote.Node3_id=='1':
                remote.Nighbour_v["13"]=1
            if remote.Node2_id=='1' and remote.Node3_id=='1':
                remote.Nighbour_v["23"]=1

            if remote.s_node1=='1' and remote.s_node2=='1':
                remote.Nighbour_s["12"]=1
            if remote.s_node1=='1' and remote.s_node3=='1':
                remote.Nighbour_s["13"]=1
            if remote.s_node2=='1' and remote.s_node3=='1':
                remote.Nighbour_s["23"]=1


            # print(remote.Nighbour_s)
            items.draw_Connect(remote.Nighbour_v,remote.Nighbour_s,screen,node1,node2,node3,BK_flag)


            texttxt=[]
            texttxt.append(myfront.render("俯仰角{}".format(remote.Pitch_angle),False,(0,0,0)))
            texttxt.append(myfront.render("偏航角 {}".format(remote.Yaw_angle),False,(0,0,0)))
            texttxt.append(myfront.render("翻滚角 {}".format(remote.Roll_angle),False,(0,0,0)))
            texttxt.append(myfront.render("坐标(x:{},y:{},z:{})".format(remote.Node_x,remote.Node_y,remote.Node_z),False,(0,0,0)))
            texttxt.append(myfront.render("速度(x:{},y:{},z:{})".format(remote.Node_x_speed,remote.Node_y_speed,remote.Node_z_speed),False,(0,0,0)))
            for i in range(len(texttxt)):
                screen.blit(texttxt[i],(node1.x-20,node1.y+70+20*i))

            #文字通用显示
            texttxt2=[]
            texttxt2.append(myfront.render("坐标(x:{},y:{},z:{})".format(remote.Node2_x,remote.Node2_y,remote.Node2_z),False,(0,0,0)))
            texttxt2.append(myfront.render("速度(x:{},y:{},z:{})".format(remote.Node2_x_speed,remote.Node2_y_speed,remote.Node2_z_speed),False,(0,0,0)))
            for i in range(len(texttxt2)):
                screen.blit(texttxt2[i], (node2.x - 50, node2.y - 42 + 20 * i))

            texttxt3=[]
            texttxt3.append(myfront.render("坐标(x:{},y:{},z:{})".format(remote.Node3_x,remote.Node3_y,remote.Node3_z),False,(0,0,0)))
            texttxt3.append(myfront.render("速度(x:{},y:{},z:{})".format(remote.Node3_x_speed,remote.Node3_y_speed,remote.Node3_z_speed),False,(0,0,0)))
            for i in range(len(texttxt3)):
                screen.blit(texttxt3[i],(node3.x-10,node3.y- 42 +20*i))








        font = pygame.font.Font(api.ttf_abs, 40)
        text_big1 = font.render("测试项目", 1, (10, 10, 10))
        screen.blit(text_big1,(20,20))
        text_big1 = font.render("网络拓扑", 1, (10, 10, 10))
        screen.blit(text_big1,(450,20))
        text_big1 = font.render("测试参数", 1, (10, 10, 10))
        screen.blit(text_big1,(20,400))
        text_big1 = font.render("测试结果", 1, (10, 10, 10))
        screen.blit(text_big1,(450,400))

        pygame.display.update()
        time.sleep(0.05)

        