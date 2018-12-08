import tkinter as tk
from tkinter import filedialog 

class MyFirstGUI:
    def __init__(self, master):
        # Instance variables
        self.master = master
        self.folder_to_process = ''

        master.title("A simple GUI")
        master.geometry("500x200")

        self.label = tk.Label(master, text="Select folder containing DBF files")
        self.label.grid(row=0,column=2,columnspan=4)

        self.choose_button = tk.Button(master, text="Choose Folder", command=self.h_choose_folder)
        self.choose_button.grid(row=1,column=0)

        self.choose_button = tk.Button(master, text="Start", command=self.h_start)
        self.choose_button.grid(row=1,column=2)

        self.close_button = tk.Button(master, text="Quit", command=master.quit)
        self.close_button.grid(row=1,column=4)
    # Event Handlers 
    def h_choose_folder(self):
        print("Greetings!")
        temp_folder = filedialog.askdirectory()
        if temp_folder:
            self.folder_to_process = temp_folder
        print(self.folder_to_process)


    def h_start(self):
        if not self.folder_to_process:
            print("No folder selected!")
        else:
            print(self.folder_to_process)


def main(): 
    root = tk.Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()