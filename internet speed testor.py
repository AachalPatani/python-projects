from tkinter import *
import speedtest

def speedcheck():
    sp= speedtest.Speedtest()
    sp.get_servers()
    down= str(round(sp.download()/(10**6),3))+"Mbps"
    up=str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp=Tk()
sp.title("internet speed check")
sp.geometry("500x650")
sp.config(bg="Blue")

lab=Label(sp,text="internet speed check",font=("Time New Roman",20,"bold"),bg="Blue",fg="white")
lab.place(x=60,y=40,height=50,width=380)

lab=Label(sp,text="Download speed",font=("Time New Roman",20,"bold"))
lab.place(x=60,y=130,height=50,width=380)

lab_down=Label(sp,text="00",font=("Time New Roman",20,"bold"))
lab_down.place(x=60,y=200,height=50,width=380)

lab=Label(sp,text="upload speed ",font=("Time New Roman",20,"bold"))
lab.place(x=60,y=290,height=50,width=380)

lab_up=Label(sp,text="00",font=("Time New Roman",20,"bold"))
lab_up.place(x=60,y=360,height=50,width=380)

button=Button(sp,text="check speed",font=("Time New Roman",20,"bold"),relief=RAISED,bg="red",command=speedcheck)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()