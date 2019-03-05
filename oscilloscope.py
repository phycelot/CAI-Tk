from tkinter import Tk,Label,Canvas,Frame,Menu,Menubutton,Button,Scale,Scrollbar,filedialog
from observer import *
from generator import *
from view import *
from controller import *
 
# if  __name__ == "__main__" : 
#     root=Tk()
#     root.option_readfile('config.txt')
#     root.title('Oscilloscope')
#     model=Generator()
#     view=Screen(root)
#     view.grid(8,8)
#     view.update(model)
#     model.attach(view)
#     ctrl=Controller(model,view)
#     view.packing()
#     root.mainloop()

class MenuBar(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self, borderwidth=2)
        button_file = Menubutton(self, text="File")
        button_file.pack(side="left")
        menu_file = Menu(button_file)
        menu_file.add_command(label='Save', underline=0,
        command=parent.save)
        menu_file.add_command(label='Quit', underline=0,
        command=parent.destroy)
        button_file.configure(menu=menu_file)
        # button_file = Menubutton(self, text="Edit")
        button_file.pack(side="left")
        button_file.configure(menu=menu_file)
      
class MainWindow(Frame):
    def __init__(self,parent=None,width=200,height=100,bg="red"):
        Frame.__init__(self)
        self.parent=parent
        self.x,self.y=0,0
        menubar = MenuBar(self)
        model=Generator()
        view=Screen(root)
        view.grid(8,8)
        view.update(model)
        model.attach(view)
        ctrl=Controller(model,view)
        menubar.pack()
        view.packing()
        
    def new(self):
        pass
    def save(self):
        formats = [('Texte','*.py'),('Portable Network Graphics','*.png')]
        filename = filedialog.asksaveasfilename(parent=self.parent,filetypes=formats,title="Sauvez l'image sous...")
        if len(filename) > 0:
          print("Sauvegarde en cours dans %s" % filename)

    def exit(self):
        self.parent.destroy()

if __name__ =="__main__":
    root = Tk()
    root.option_readfile('config.txt')
    root.title('Oscilloscope')
    mw = MainWindow(root)
#    mw.pack()
    mw.pack(expand=1,fill="both",padx=6,pady=6)
    root.mainloop()