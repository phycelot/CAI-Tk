from tkinter import Canvas,Scale,ttk
from observer import *
import types

class Screen(Observer):
    def __init__(self,parent,bg="white"):
        self.canvas=Canvas(parent,bg=bg)
        # print("parent",parent.cget("width"),parent.cget("height"))

        self.labelX=ttk.Label(text="X")

        self.magnitudeX=Scale(parent,length=250,orient="horizontal",
                         name="scaleMagnitudeX", sliderlength=20,
                         showvalue=0,from_=0.1,to=10,
                         tickinterval=1)

        self.frequenceX=Scale(parent,length=250,orient="horizontal",
                         name="scaleFrequenceX", sliderlength=20,
                         showvalue=0,from_=0,to=5,
                         tickinterval=25)

        self.phaseX=Scale(parent,length=250,orient="horizontal",
                         name="scalePhaseX", sliderlength=20,
                         showvalue=0,from_=0,to=5,
                         tickinterval=25)

        self.separator=ttk.Separator()

        self.labelY=ttk.Label(text="Y")

        self.magnitudeY=Scale(parent,length=250,orient="horizontal",
                         name="scaleMagnitudeY", sliderlength=20,
                         showvalue=0,from_=0.1,to=10,
                         tickinterval=1)

        self.frequenceY=Scale(parent,length=250,orient="horizontal",
                         name="scaleFrequenceY", sliderlength=20,
                         showvalue=0,from_=0,to=5,
                         tickinterval=25)

        self.phaseY=Scale(parent,length=250,orient="horizontal",
                         name="scalePhaseY", sliderlength=20,
                         showvalue=0,from_=0,to=5,
                         tickinterval=25)

    def update(self,modelList):
        print("View update")
        color=["green","red","blue","orange"]
        i=0
        if isinstance(modelList,list): #isinstance(modelList,list)
            for e in modelList:
                signal=e.get_signal()
                self.plot_signal(signal,color[i])
                i=i+1
                pass
            pass
        else:
            signal=modelList.get_signal()
            self.plot_signal(signal,color[i])
            pass
        

    def get_magnitudeX(self):
        return self.magnitudeX

    def get_frequenceX(self):
        return self.frequenceX

    def get_phaseX(self):
        return self.phaseX

    def get_magnitudeY(self):
        return self.magnitudeY

    def get_frequenceY(self):
        return self.frequenceY

    def get_phaseY(self):
        return self.phaseY

    def plot_signal(self,signal,color="red"):
        w,h=self.canvas.winfo_width(),self.canvas.winfo_height()
        width,height=int(w),int(h)
        if self.canvas.find_withtag("signal") :
            self.canvas.delete("signal")
        if signal and len(signal) > 1:
            plot = [(x*width, height/2.0*(y+1)) for (x, y) in signal]
            signal_id = self.canvas.create_line(plot, fill=color, smooth=1, width=3,tags="signal")
        return

    def grid(self, n=4,m=4):
        if self.canvas.find_withtag("grid"):
            self.canvas.delete("grid")
        w,h=self.canvas.winfo_width(),self.canvas.winfo_height()
        width,height=int(w),int(h)
        print(width, height)
        if(0) : #arrow enable
            self.canvas.create_line(10,height/2,width,height/2,arrow="last")
            self.canvas.create_line(10,height-5,10,5,arrow="last")
            step=(width)/n*1.
            for t in range(1,n+2):
                x =t*step
                self.canvas.create_line(x,height/2-4,x,height/2+4)

        if(1) : #grid enable
            step=(width)/n*1.
            for t in range(1,n+2):
                x =t*step
                self.canvas.create_line(x,0,x,height,tag="grid")

            step=(height)/m*1.
            for t in range(1,m+2):
                x =t*step
                self.canvas.create_line(0,x,width,x,tag="grid")

    def packing(self) :
        self.canvas.pack(fill = "both", expand = "yes")
        self.labelX.pack(fill = "both", expand = "yes")
        self.magnitudeX.pack(fill = "both", expand = "yes")
        self.frequenceX.pack(fill = "both", expand = "yes")
        self.phaseX.pack(fill = "both", expand = "yes")
        self.separator.pack(fill = "both", expand = "yes",padx=8,pady=8)
        self.labelY.pack(fill = "both", expand = "yes")
        self.magnitudeY.pack(fill = "both", expand = "yes")
        self.frequenceY.pack(fill = "both", expand = "yes")
        self.phaseY.pack(fill = "both", expand = "yes")

    def get_canvas(self):
        return self.canvas
