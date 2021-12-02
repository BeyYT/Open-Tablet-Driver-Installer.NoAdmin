# Import Modules

import urllib.request, zipfile, os, winshell
from win32com.client import Dispatch

# Say hi

print("Hello! Welcome To The Tablet Driver Installer.")
print("Copyright BeyYT 2021. All Rights Reserved, OpenTabletDriver Is A Part Of The OpenTabletDriver Group.")
input("Press Enter To Continue")
print("Downloading Driver")

# REAL EBIG SHIZ HERE 
# also add your own tablet driver distro!

urllib.request.urlretrieve("https://github.com/OpenTabletDriver/OpenTabletDriver/releases/download/v0.5.3.3/OpenTabletDriver.win-x64.zip", "OpenTabletDriver.win-x64.zip")

print("Downloading .NET 5.0 Framework")

# If Your Distro Has NET 5.0 Framework Embedded, Comment Line 22, 30-33, 37-42 and 46.

urllib.request.urlretrieve("https://download.visualstudio.microsoft.com/download/pr/d1ca6dbf-d054-46ba-86d1-36eb2e455ba2/e950d4503116142d9c2129ed65084a15/dotnet-sdk-5.0.403-win-x64.zip", "dotnet-sdk-5.0.403-win-x64.zip")

# Unzipping some stuf

with zipfile.ZipFile(os.getcwd() + "\\OpenTabletDriver.win-x64.zip", 'r') as zip_ref:
    print("Unzipping Tablet Driver")
    zip_ref.extractall(os.getcwd() + "\\Driver")

with zipfile.ZipFile(os.getcwd() + "\\dotnet-sdk-5.0.403-win-x64.zip", 'r') as zip_ref:
    print("Unzipping .Net 5.0 Framework")
    zip_ref.extractall(os.getcwd() + "\\.Net_5.0_Framework")

# Path Entries (If .NET 5.0 Framework Is Not Embedded)
# Usually Requires Local PATH To Be Enabled By SYSADMIN
print("adding PATH entries")

os.system('setx DOTNET_ROOT "' + os.getcwd() + '\\.Net_5.0_Framework"')
#Get Current Path Entries
curpath = os.getenv(['PATH'])
os.system('setx PATH "' + curpath + ';' + os.getcwd() + '\\.Net_5.0_Framework"')
os.system('setx DOTNET_MULTILEVEL_LOOKUP 0')

# Printing stuff

print("done!")
print("Tablet Driver Path:" + os.getcwd() + "\\Driver")
print(".Net 5.0 Framework Path:" + os.getcwd() + "\\.Net_5.0_Framework")

# deleting Useless ZIP Files

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

# Hey!
# In Case It Stops Working Or Dosent Work, Please Send Me A DM on Discord
# Bey#0513

