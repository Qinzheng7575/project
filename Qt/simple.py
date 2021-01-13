import tkinter as tk
from tkinter import ttk

class window:
    


    def xFunc(self,moshi,juese,gps):
        print(moshi,juese,gps)            # #获取选中的值方法1

    def gps_select(self,if_gps):
        print('选中了gps')

    def begain_gui(self):
        window = tk.Tk()
        window.title('my window')
        # window.geometry('400x600')
        #ip地址
        L1 = tk.Label(window, text="IP地址").grid(column=1,row=0)
        e1 = tk.Entry(window, show=None).grid(column=0,row=0)

        #模式
        moshi_var=tk.StringVar()
        moshi_win=ttk.Combobox(window,textvariable=moshi_var)
        moshi_win.grid(column=0,row=1)
        moshi_win["value"]=('1','2','3')
        moshi_win.current(0)

        juese_var=tk.StringVar()
        juese_win=ttk.Combobox(window,textvariable=juese_var)
        juese_win.grid(column=0,row=2)
        juese_win["value"]=('4','5','6')
        juese_win.current(0)

        #单选框 美化：https://blog.csdn.net/ever_peng/article/details/102815139
        if_gps=tk.IntVar()
        if_gps_win=tk.Radiobutton(window,text='使能gps',value=1,variable=if_gps,command=lambda : self.gps_select(if_gps=if_gps.get()))
        if_gps_win.grid(column=0,row=3)


        b1 = tk.Button(window, text='选择', command=lambda : self.xFunc(moshi=moshi_var.get(),juese=juese_var.get(),gps=if_gps.get()))
        b1.grid(column=0,row=4)



    # e2 = tk.Entry(window, show=None)
    # e2.pack()

    # b1 = tk.Button(window, text='insert', width=15, height=2, command=lambda : insert_ip(ip=e,marsk=e2,interface=e1,next_hop=e3))
    # b1.pack()
    # bot = tk.Label(window, text='请在下方输入next_hop')
    # bot.pack()
    # e3 = tk.Entry(window, show=None)
    # e3.pack()
        window.mainloop()
    # 使用
    # sing_thread = Thread(target=begain_gui)
    # sing_thread.start()
if __name__ == "__main__":
    win=window()
    win.begain_gui()