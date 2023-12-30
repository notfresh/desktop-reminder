
from tkinter import messagebox
import time
from datetime import datetime

def show_popup():
    import tkinter as tk
    popup = tk.Tk()
    popup.title("工作日志提示")
    popup.geometry("400x300")

    # 添加文本
    label = tk.Label(popup, text="现在时间是{}, 该定期在笔记里写工作总结了".format(now))
    label.pack()

    popup.lift()
    popup.focus_force()
    popup.mainloop()


range_tip_count = 10

counter = 0
while True:    
    now = datetime.now()
    # print("现在时间是", now.hour, now.minute)
    if(now.minute > 54  and now.minute <= 59):        
        if( counter < range_tip_count ):
            show_popup()
            time.sleep(30)        
            counter = counter + 1        
    else:
        counter = 0
        time.sleep(60*2)





