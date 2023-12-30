
from tkinter import messagebox
import time
from datetime import datetime

range_tip_count = 10

counter = 0
while True:    
    now = datetime.now()
    # print("现在时间是", now.hour, now.minute)
    if(now.hour % 2 == 1 and now.minute > 54  and now.minute <= 59):        
        if( counter < range_tip_count ):
            messagebox.showinfo("提示common","现在时间是{}, 该定期在笔记里写工作总结了".format(now))
            time.sleep(30)        
            counter = counter + 1        

    # 每两个小时只能执行一次
    if(now.hour % 2 != 1 and counter >= range_tip_count):
        counter = 0
        time.sleep(60*10)





