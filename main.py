
import requests,subprocess,os
import tkinter as tk
from tkinter import messagebox

def download_and_install():
    url = "https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2023/08/windows10.0-kb5029244-x64_fb8cdde229cf17755c2c890a12e0e8f252dd38c0.msu"
    download_dir = "C:\\FACEIT_PATCHER"
    
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        os.chdir(download_dir)
    else:
        os.chdir(download_dir)
    
    msu_filename = "windows10.0-kb5029244-x64_fb8cdde229cf17755c2c890a12e0e8f252dd38c0.msu"
    msu_path = os.path.join(download_dir, msu_filename)
    
    response = requests.get(url)
    with open(msu_path, 'wb') as msu_file:
        msu_file.write(response.content)
    
    install_command = f"wusa.exe {msu_filename}"
    os.system(install_command)



root = tk.Tk()
root.title("TINY FACEIT PATCHER by FPSHEAVEN.com")
root.resizable(False, False)
root.geometry("500x80")

download_button = tk.Button(root, text="Download and Install KB5029006", command=download_and_install)
download_button.pack(padx=10, pady=10)
label1 = tk.Label(text="Please wait for the download to finish. It might take a while.")
label2=tk.Label(text="The app will FREEZE during download. Be patient")
label2.pack(side="bottom")
label1.pack(side="bottom")

# ksekina t malakia
root.mainloop()
