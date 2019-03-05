from tkinter import Tk,Label,Canvas,Frame,Menu,Menubutton,Button,Scale,Scrollbar,filedialog,messagebox
import json

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
    def __init__(self,parent=None):
        Frame.__init__(self)
        self.parent=parent
        menubar = MenuBar(self)
        parent.protocol("WM_DELETE_WINDOW", self.exit)
        model=Generator()
        view=Screen(root)
        view.grid(12,12)
        view.update(model)
        model.attach(view)
        ctrl=Controller(model,view)
        menubar.pack(expand=1,fill="x",padx=0,pady=0)
        view.packing()
        self.model=model
        model.generate_signal()

    def open(self):
        formats = [('JSON','*.json')]
        f = filedialog.askopenfilename(parent=self.parent,filetypes=formats,title="Selectionner la configuration à ouvrir")
        with open(f,"r") as f:
            data=json.load(f)
            try:
                self.model.set_phase(data["parametre"]["phase"])
                self.model.set_frequence(data["parametre"]["frequence"])
                self.model.set_magnitude(data["parametre"]["magnitude"])
                #TODO : update sliders
                pass
            except TypeError as err:
                messagebox.showerror("error","fichier de configuration mal formé\n".format(err))
                pass
            
    
    def save(self):
        formats = [('JSON','*.json')]
        f = filedialog.asksaveasfilename(parent=self.parent,filetypes=formats,title="Sauvez l'image sous...")
        if len(f) > 0:
            print("Sauvegarde en cours dans %s" % f)
            with open(f,"w") as f:
                json.dump({'parametre':{"phase":self.model.get_phase(),'frequence':self.model.get_frequence(),'magnitude':self.model.get_magnitude()},'signal':self.model.get_signal()},f)
            f.close()

    def exit(self):
        answer = messagebox.askokcancel("Question","Êtes-vous sur de vouloir quitter ?")
        if(answer) :
            self.parent.destroy()

    def credit(self):
        messagebox.showinfo("Crédit","Un grand pouvoir implique de grande résponsabilité\n\n- OLLIVIER Evan\n -> e5ollivi@enib.fr\n\n- PROUTEAU Antonin\n -> a5proute@enib.fr")
        pass

if __name__ =="__main__":
    root = Tk()
    root.option_readfile('config.txt')
    root.title('Oscilloscope')
    mw = MainWindow(root)
    mw.pack()
    mw.pack(expand=1,fill="both",padx=6,pady=6)
    root.mainloop()