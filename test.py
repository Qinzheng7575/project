# file = open("D:\ForStudy\python练习\练习\项目\Test.txt", "rt", encoding="utf-8") 
# File = file.readlines()
# txt=[]

# for line in File:
#     line=line.strip('\n')
#     # print(line)
#     txt.append(line)
# file.close()
# print(txt)


# import sys
# stdout = sys.stdout
# with open('D:\ForStudy\python练习\练习\项目\out.txt', 'w+') as file:
#     sys.stdout = file
#     print('lalalla')
# sys.stdout = stdout
# print("嘿嘿嘿")

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
#     with subprocess.Popen(["iperf3.exe", "-s"], stdout=subprocess.PIPE, universal_newlines=True) as process:
#         while True:
#             print("doing")
#             # print(flag)
#             output = process.stdout.readline()

#             if output == '' and process.poll() is not None:
#                 break
#             if output:
#                 # with open('D:\ForStudy\python练习\练习\项目\out.txt', 'w+') as file:
#                 #     sys.stdout = file             
#                 #     print(output.strip())

#                 # sys.stdout = stdout
#                 a=output.strip()
#                 print(a)
#                 # print("length is :",len(a))
#                 if len(a) > 70:
#                     print("time to close")
#                     return 0


#         rc = process.poll()


# def client():
#     global flag
#     with subprocess.Popen(["iperf3.exe", "-c","127.0.0.1"], stdout=subprocess.PIPE, universal_newlines=True) as process:
#         while True:
#             output = process.stdout.readline()
#             if output == '' and process.poll() is not None:
#                 break
#             if output:
#                 pass
#                 # sys.stdout = stdout
#                 # print(output.strip())


#         rc = process.poll()
#         time.sleep(2)
#         flag = 1
#         if flag ==1:
#             print("client has shut")
#             with subprocess.Popen("taskkill /IM iperf3.exe /F", stdout=subprocess.PIPE, shell=True,universal_newlines=True) as process:
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


#----------------------------------------------------
#----------------------------------------------------
# import threading
# import time
# from threading import Thread

# flag=0
# def loop():
#     global flag
#     i = 0
#     while True:
#         print(i)
#         i += 1
#         if i > 10:
#             flag=1
#             return
#         time.sleep(0.5)

# def loop2():
#     global flag

#     while True:
#         if flag == 1:
#             print("time to close")
#             time.sleep(2)
#             return
#         pass
# if __name__ == "__main__":
#     t1 = Thread(target=loop)
#     t2 = Thread(target=loop2)
#     t1.start()
#     t2.start()


