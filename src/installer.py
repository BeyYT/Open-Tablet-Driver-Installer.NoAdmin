# Import Modules

import urllib.request
import zipfile
import os
import winshell
from win32com.client import Dispatch

# Say hi

print("Hello! Welcome To The Tablet Driver Installer.")
input("Press Enter To Continue")
print("Downloading Driver")

# REAL EBIG SHIZ HERE 
# also add your own tablet driver distro!

urllib.request.urlretrieve("https://github.com/OpenTabletDriver/OpenTabletDriver/releases/download/v0.5.3.3/OpenTabletDriver.win-x64.zip", "OpenTabletDriver.win-x64.zip")

print("Downloading .NET 5.0 Framework")

# If Your Distro Has NET 5.0 Framework Embedded, Comment Line 18, 22, 30-32, 36-39 and 45.

urllib.request.urlretrieve("https://download.visualstudio.microsoft.com/download/pr/d1ca6dbf-d054-46ba-86d1-36eb2e455ba2/e950d4503116142d9c2129ed65084a15/dotnet-sdk-5.0.403-win-x64.zip", "dotnet-sdk-5.0.403-win-x64.zip")

# Unzipping some stuf

with zipfile.ZipFile(os.getcwd() + "\\OpenTabletDriver.win-x64.zip", 'r') as zip_ref:
    print("Unzipping Tablet Driver")
    zip_ref.extractall(os.getcwd() + "\\Driver")

with zipfile.ZipFile(os.getcwd() + "\\dotnet-sdk-5.0.403-win-x64.zip", 'r') as zip_ref:
    print("Unzipping .Net 5.0 Framework")
    zip_ref.extractall(os.getcwd() + "\\.Net_5.0_Framework")

# Path Entries (If .NET 5.0 Framework Is Not Embedded)

print("adding PATH entries")
os.system('setx DOTNET_ROOT "' + os.getcwd() + '\\.Net_5.0_Framework"')
os.system('setx PATH "' + os.getcwd() + '\\.Net_5.0_Framework"')
os.system('setx DOTNET_MULTILEVEL_LOOKUP 0')

# Printing stuff

print("done!")
print("Tablet Driver Path:" + os.getcwd() + "\\Driver")
print(".Net 5.0 Framework Path:" + os.getcwd() + "\\.Net_5.0_Framework")
os.remove(os.getcwd() + "\\dotnet-sdk-5.0.403-win-x64.zip")
os.remove(os.getcwd() + "\\OpenTabletDriver.win-x64.zip")

#adding desktop shortcut

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
input("Press the Enter key to exit.")
