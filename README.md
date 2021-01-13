# project

需要将UDPping文件中的

2-2-UDPPingerServer.py

UDP_test.py

UDPPingerClient.py

以及iperf2放在拥有系统变量的文件夹下：

![image-20210113193941761](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210113193941761.png)

==（其中只有iperf-2.1.0-rc-win有用）==

这些在item.py中的函数中用到：

```python
def V_iperf_server(self):
     if 'Windows'in platform.platform():
        print('This platform is Windows')
        with subprocess.Popen(["iperf-2.1.0-rc-win.exe","-s","-u","--port","24600","-i","2"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:

```



items.py中的API_need类

其中字体文件的路径需要改变

```python
    ttf_abs ='C:\Windows\Fonts\simhei.ttf'
```

Node类图片路径需要改变，图片都放在了img文件夹下