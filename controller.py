class Controller :
    def __init__(self,modelList,view):
        self.modelList=modelList
        self.model=modelList[0]
        self.view=view
        self.view.get_magnitude().bind("<B1-Motion>",self.update_magnitude)
        self.view.get_frequence().bind("<B1-Motion>",self.update_frequence)
        self.view.get_phase().bind("<B1-Motion>",self.update_phase)
        self.view.get_canvas().bind("<Configure>",self.resize)


    def update_magnitude(self,event):
        print("update_magnitude")
        x=int(event.widget.get())
        self.model.set_magnitude(x)
        self.model.generate_signal()

    def update_frequence(self,event):
        print("update_frequence")
        x=int(event.widget.get())
        self.model.set_frequence(x)
        self.model.generate_signal()

    def update_phase(self,event):
        print("update_phase")
        x=int(event.widget.get())
        self.model.set_phase(x)
        self.model.generate_signal()

    def resize(self, event):
        for e in self.modelList:
            signal=e.get_signal()
            self.view.plot_signal(signal)
            pass
        self.view.grid()
        
