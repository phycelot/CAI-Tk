class Controller :
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.view.get_magnitude().bind("<B1-Motion>",self.update_magnitude)
        self.view.get_frequence().bind("<B1-Motion>",self.update_frequence)
        self.view.get_phase().bind("<B1-Motion>",self.update_phase)
        self.view.get_canvas().bind("<Configure>",self.resize)
        self.view.get_grid().bind("<B1-Motion>",self.update_grid)


    def update_magnitude(self,event):
        print("update_magnitude")
        x=int(event.widget.get())*0.1
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
        #print("resize")
        signal=self.model.get_signal()
        self.view.plot_signal(signal)
        self.view.grid()

    def update_grid(self, event):
        print("update_grid")
        x=int(event.widget.get())
        print(x)
        #self.model.set_grid(x)
        self.view.grid(x,x)
