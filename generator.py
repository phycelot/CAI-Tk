from math import pi,sin
from observer import *

class Generator(Subject):
    def __init__(self,a=1.0,f=1.0,p=0.0):
        Subject.__init__(self)
        self.signal=[]
        self.a,self.f,self.p=a,f,p
        self.generate_signal()
        self.grid_resolution = 8

    def generate_signal(self):
        del self.signal[0:]
        samples=1000
        for t in range(0,samples,5):
            samples=float(samples)
            e=self.a*sin((2*pi*self.f*(t*1.0/samples))-self.p)
            self.signal.append((t*1.0/samples,e))
        self.notify()

    def set_magnitude(self,a):
        self.a=a
        print("set_magnitude "+str(a))
        self.generate_signal()

    def get_grid_resolution(self):
        return self.grid_resolution

    def set_grid_resolution(self, value):
        self.grid_resolution = value

    def get_magnitude(self):
        return self.a

    def set_frequence(self,f):
        self.f=f
        self.generate_signal()

    def get_frequence(self):
        return self.f

    def set_phase(self,p):
        self.p=p
        self.generate_signal()

    def get_phase(self):
        return self.p

    def get_signal(self):
        return self.signal
