from tkinter import Canvas,Scale
from observer import *

class Screen(Observer):
    def __init__(self,parent,bg="white"):
        self.canvas=Canvas(parent,bg=bg)
        print("parent",parent.cget("width"),parent.cget("height"))

        self.frequency_value = 5
        self.magnitude_value = 9

        self.magnitude=Scale(parent,length=250,orient="horizontal",
                         name="scaleMagnitude", sliderlength=20,
                         showvalue=0,from_=0,to=9,
                         tickinterval=1)

        self.frequence=Scale(parent,length=250,orient="horizontal",
                         name="scaleFrequence", sliderlength=20,
                         showvalue=0,from_=0,to=50,
                         tickinterval=10)

        self.phase=Scale(parent,length=250,orient="horizontal",
                         name="scalePhase", sliderlength=20,
                         showvalue=0,from_=0,to=10,
                         tickinterval=2)

        self.grid_slider=Scale(parent,length=250,orient="horizontal",
                         name="scaleGrid", sliderlength=20,
                         showvalue=4,from_=4,to=16,
                         tickinterval=1)

    def update(self,model):
        print("View update")
        signal=model.get_signal()
        self.plot_signal(signal)

    def get_magnitude(self):
        return self.magnitude

    def get_frequence(self):
        return self.frequence

    def get_phase(self):
        return self.phase
    def get_grid_slider(self):
        return self.grid_slider

    def plot_signal(self,signal,color="red"):
        w,h=self.canvas.winfo_width(),self.canvas.winfo_height()
        width,height=int(w),int(h)
#        print(self.canvas.find_withtag("signal"))
        if self.canvas.find_withtag("signal") :
            self.canvas.delete("signal")
        if signal and len(signal) > 1:
            plot = [(x*width, height/2.0*(y+1)) for (x, y) in signal]
            signal_id = self.canvas.create_line(plot, fill=color, smooth=1, width=3,tags="signal")
        return

    def grid(self, model):
        n = model.get_grid_resolution()
        self.grid_slider.set(n)

        #n = self.grid_resolution
        m = n

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
        self.magnitude.pack(fill = "both", expand = "yes")
        self.frequence.pack(fill = "both", expand = "yes")
        self.phase.pack(fill = "both", expand = "yes")
        self.grid_slider.pack(fill = "both", expand = "yes")

    def get_canvas(self):
        return self.canvas
