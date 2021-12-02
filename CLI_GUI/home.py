import Installer
import Uninstaller
# AAAAAAAA
print("installer thingy")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("Options:")
print("1: Install / Update Tablet Driver")
print("2: Uninstall Tablet Driver")
option = int(input("Select Option: "))
if option == 1:
  print("Select Options:")
  print("1: Background Install")
  print("No Option: Regular Install")
  input2 = int(input("Select Option: "))
  if input2 == 1:
    Installer.backinstall()
  else:
    Installer.install()
