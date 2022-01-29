import wget, zipfile, os, winshell, time, subprocess, shutil
from win32com.client import Dispatch
clear = lambda: os.system('cls')
ipnt = ""
def menu():
  global ipnt
  print('''

████████╗ █████╗ ██████╗ ██████╗ ██╗███╗   ██╗████████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║╚══██╔══╝
   ██║   ███████║██████╔╝██║  ██║██║██╔██╗ ██║   ██║   
   ██║   ██╔══██║██╔══██╗██║  ██║██║██║╚██╗██║   ██║   
   ██║   ██║  ██║██████╔╝██████╔╝██║██║ ╚████║   ██║   
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝   
'''
)
  print("Welcome to the Tablet Driver Installer (No-Admin ver)")
  print("Please Select an Option:")
  print('''
1: Install Driver
2: Uninstall Driver
3: Exit
''')

  ipt = input("Option: ")
  try:
    ipnt = int(ipt)
  except:
    print("No option Selected!")
    time.sleep(1)
    clear()
    menu()
  if ipnt == 1:
    clear()
    print("Downloading Driver")
    wget.download("https://github.com/OpenTabletDriver/OpenTabletDriver/releases/download/v0.5.3.3/OpenTabletDriver.win-x64.zip")
    clear()
    print("Downloading .NET 5.0 Framework")
    wget.download("https://download.visualstudio.microsoft.com/download/pr/d1ca6dbf-d054-46ba-86d1-36eb2e455ba2/e950d4503116142d9c2129ed65084a15/dotnet-sdk-5.0.403-win-x64.zip")
    clear()
    with zipfile.ZipFile(os.getcwd() + "\\OpenTabletDriver.win-x64.zip", 'r') as zip_ref:
        print("Unzipping Tablet Driver")
        zip_ref.extractall(os.getcwd() + "\\Driver")
    clear()
    with zipfile.ZipFile(os.getcwd() + "\\dotnet-sdk-5.0.403-win-x64.zip", 'r') as zip_ref:
        print("Unzipping .Net 5.0 Framework")
        zip_ref.extractall(os.getcwd() + "\\.Net_5.0_Framework")
    print("adding PATH entries")
    os.system('setx DOTNET_ROOT "' + os.getcwd() + '\\.Net_5.0_Framework"')
    os.system('setx PATH "' + os.getcwd() + '\\.Net_5.0_Framework"')
    os.system('setx DOTNET_MULTILEVEL_LOOKUP 0')
    clear()
    print("Complete!")
    print("Tablet Driver Path:" + os.getcwd() + "\\Driver")
    print(".Net 5.0 Framework Path:" + os.getcwd() + "\\.Net_5.0_Framework")
    os.remove(os.getcwd() + "\\dotnet-sdk-5.0.403-win-x64.zip")
    os.remove(os.getcwd() + "\\OpenTabletDriver.win-x64.zip")
    desktop = winshell.desktop()
    path = os.path.join(desktop, "Open Tablet Driver.lnk")
    target = os.getcwd() + "\\driver\\OpenTabletDriver.UX.Wpf.exe"
    wDir = os.getcwd() + "\\driver"
    icon = os.getcwd() + "\\driver\\OpenTabletDriver.UX.Wpf.exe"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()
    time.sleep(10)
    clear()
    menu()

  if ipnt == 2:
    if os.path.isdir(os.getcwd() + "\\.Net_5.0_Framework") and os.path.isdir(os.getcwd() + "\\Driver"):
      shutil.rmtree(os.getcwd() + "\\.Net_5.0_Framework", ignore_errors=False, onerror=None)
      shutil.rmtree(os.getcwd() + "\\Driver", ignore_errors=False, onerror=None)
      try:
        desktop = winshell.desktop()
        os.remove(os.path.join(desktop, "Open Tablet Driver.lnk"))
      except:
        print("could not delete the .ink shortcut. / deleted the shortcut!")
  
    else:
      print("Driver Not Installed! / Succsessfully Deleted Driver!")
      time.sleep(2)
      clear()
      menu()
  if ipnt == 3:
    exit()
  else:
    print("no option selected!")
    time.sleep(1)
    clear()
    menu()

menu()
    
