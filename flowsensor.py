# Tkinter
import tkinter as tk


class MainApplication(tk.Tk):
  def __init__(self,tasks=None):
    super().__init__()

    self.title("Pressure Sensors || DEICA Automatismos S.A. de C.V.")
    self.geometry("800x480+0+0")
    self.resizable(0, 0)

    self.back = tk.Frame(master=self, width=800, height=480, bg='white')
    self.back.pack_propagate(0)
    self.back.pack(fill=tk.BOTH, expand=1)


    #Create popupmenu
    self.menu_bar = tk.Menu(self)
    self.popup_menu = tk.Menu(self.menu_bar,tearoff=0)
    self.popup_menu.add_command(label="Home",command=self.donothing)
    self.popup_menu.add_command(label="Settings",command=self.donothing)

    self.popup_menu.add_separator()
    
    self.config(menu=self.menu_bar)

  def donothing():
    filewin = tk.TopLevel(self)
    button = tk.Button(filewin,text="Do no thing")
    button.pack()




def main():
  """Es el control de la pantalla y la configuración y arranque de la misma"""

  #Inizialisamos el tk
  root = MainApplication()
  root.mainloop()

if __name__ == "__main__":
  """Empieza a ejecutar la primera linea de codigo"""
  main()
