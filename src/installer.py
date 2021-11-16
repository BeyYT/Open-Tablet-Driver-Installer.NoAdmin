import urllib.request
import zipfile
import os
print("Hello! Welcome To The Tablet Driver Installer.")
input("Press Enter To Continue")
print("Downloading Driver")
urllib.request.urlretrieve("https://github.com/OpenTabletDriver/OpenTabletDriver/releases/download/v0.5.3.3/OpenTabletDriver.win-x64.zip", "OpenTabletDriver.win-x64.zip")
print("Downloading .NET 5.0 Framework")
urllib.request.urlretrieve("https://download.visualstudio.microsoft.com/download/pr/d1ca6dbf-d054-46ba-86d1-36eb2e455ba2/e950d4503116142d9c2129ed65084a15/dotnet-sdk-5.0.403-win-x64.zip", "dotnet-sdk-5.0.403-win-x64.zip")
with zipfile.ZipFile(os.getcwd() + "\\OpenTabletDriver.win-x64.zip", 'r') as zip_ref:
    print("Unzipping Tablet Driver")
    zip_ref.extractall(os.getcwd() + "\\Driver")

with zipfile.ZipFile(os.getcwd() + "\\dotnet-sdk-5.0.403-win-x64.zip", 'r') as zip_ref:
    print("Unzipping .Net 5.0 Framework")
    zip_ref.extractall(os.getcwd() + "\\.Net_5.0_Framework")
print("adding PATH entries")
os.system('setx DOTNET_ROOT "' + os.getcwd() + '\\.Net_5.0_Framework"')
os.system('setx PATH "' + os.getcwd() + '\\.Net_5.0_Framework"')
os.system('setx DOTNET_MULTILEVEL_LOOKUP 0')
print("done!")
# setx PATH "c:\my-user-specifc-bin-path-which-may-contain-spaces;"%%PATH%%
# set PATH=%USERPROFILE%\dotnet;%PATH%
# set DOTNET_MULTILEVEL_LOOKUP=0
print("Tablet Driver Path:" + os.getcwd() + "\\Driver")
print(".Net 5.0 Framework Path:" + os.getcwd() + "\\.Net_5.0_Framework")
input("Press the Enter key to exit.")