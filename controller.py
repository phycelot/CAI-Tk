class Controller :
    def __init__(self,modelList,view):
        self.modelList=modelList
        self.modelX=modelList[0]
        self.modelY=modelList[1]
        self.view=view
        self.view.get_magnitudeX().bind("<B1-Motion>",self.update_magnitudeX)
        self.view.get_frequenceX().bind("<B1-Motion>",self.update_frequenceX)
        self.view.get_phaseX().bind("<B1-Motion>",self.update_phaseX)
        self.view.get_magnitudeY().bind("<B1-Motion>",self.update_magnitudeY)
        self.view.get_frequenceY().bind("<B1-Motion>",self.update_frequenceY)
        self.view.get_phaseY().bind("<B1-Motion>",self.update_phaseY)
        self.view.get_canvas().bind("<Configure>",self.resize)


    def update_magnitudeX(self,event):
        print("update_magnitude")
        x=int(event.widget.get())
        model=self.modelX
        model.set_magnitude(x)
        model.generate_signal()

    def update_frequenceX(self,event):
        print("update_frequence")
        x=int(event.widget.get())
        model=self.modelX
        model.set_frequence(x)
        model.generate_signal()

    def update_phaseX(self,event):
        print("update_phase")
        x=int(event.widget.get())
        model=self.modelX
        model.set_phase(x)
        model.generate_signal()

    def update_magnitudeY(self,event):
        print("update_magnitude")
        x=int(event.widget.get())
        model=self.modelY
        model.set_magnitude(x)
        model.generate_signal()

    def update_frequenceY(self,event):
        print("update_frequence")
        x=int(event.widget.get())
        model=self.modelY
        model.set_frequence(x)
        model.generate_signal()

    def update_phaseY(self,event):
        print("update_phase")
        x=int(event.widget.get())
        model=self.modelY
        model.set_phase(x)
        model.generate_signal()

    def resize(self, event):
        for e in self.modelList:
            signal=e.get_signal()
            self.view.plot_signal(signal)
            pass
        self.view.grid()
        
