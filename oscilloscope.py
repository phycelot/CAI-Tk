from tkinter import Tk,Label,Canvas,Frame,Menu,Menubutton,Button,Scale,Scrollbar,filedialog,messagebox
from observer import *
from generator import *
from view import *
from controller import *

class MenuBar(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self, borderwidth=2)
        #file
        button_file = Menubutton(self, text="File")
        button_file.pack(side="left")
        menu_file = Menu(button_file)
        menu_file.add_command(label='Save', underline=0,
        command=parent.save)
        menu_file.add_command(label='Open', underline=0,
        command=parent.open)
        menu_file.add_command(label='Quit', underline=0,
        command=parent.exit)
        button_file.pack(side="left")
        button_file.configure(menu=menu_file)

        #help
        button_file1 = Menubutton(self, text="Help")
        menu_file1 = Menu(button_file1)
        menu_file1.add_command(label='Crédit', underline=0,
        command=parent.credit)
        button_file1.pack(side="left")
        button_file1.configure(menu=menu_file1)
      
class MainWindow(Frame):
    def __init__(self,parent=None,width=200,height=100,bg="red"):
        Frame.__init__(self)
        self.parent=parent
        self.x,self.y=0,0
        menubar = MenuBar(self)
        parent.protocol("WM_DELETE_WINDOW", self.exit)
        model=Generator()
        view=Screen(root)
        view.grid(8,8)
        view.update(model)
        model.attach(view)
        ctrl=Controller(model,view)
        menubar.pack(expand=1,fill="x",padx=0,pady=0)
        view.packing()
        
    def new(self):
        pass


    def open(self):
        formats = [('Texte','*.py'),('Portable Network Graphics','*.png')]
    
    def save(self):
        formats = [('Texte','*.py'),('Portable Network Graphics','*.png')]
        filename = filedialog.asksaveasfilename(parent=self.parent,filetypes=formats,title="Sauvez l'image sous...")
        if len(filename) > 0:
          print("Sauvegarde en cours dans %s" % filename)

    def exit(self):
        answer = messagebox.askokcancel("Question","Êtes-vous sur de vouloir quitter ?")
        if(answer) :
            self.parent.destroy()

    def credit(self):
        messagebox.showinfo("Crédit","Un grand pouvoir implique de grande résponsabilité")
        pass

if __name__ =="__main__":
    root = Tk()
    root.option_readfile('config.txt')
    root.title('Oscilloscope')
    mw = MainWindow(root)
    mw.pack()
    mw.pack(expand=1,fill="both",padx=6,pady=6)
    root.mainloop()