#imports
import os
import platform
from tkinter import messagebox
import webbrowser


#begin code


#commands
commands = "!reset, !CheckSystemFiles, !RepairSystemFiles,!CleanTempFiles, !ActivatorWin10Pro !ActivatorWin10Enterprise,!help, !CheckWinVer"

#commandslist print

print("Commands : !reset ; !CheckSystemFiles ; !RepairSystemFiles ; !CleanTempFiles ; \n\n           !ActivatorWin10Pro ; !ActivatorWin10Enterprise ; !help ; !CheckWinVer")
repair_command = input("Your repair methode:")

#commands + answers
if repair_command == "!reset":
    os.system("systemreset -cleanpc")
if repair_command == "!CheckSystemFiles":
    os.system("sfc /scannow")
if repair_command == "!RepairSystemFiles":
    os.system("DISM.exe /Online /Cleanup-image /Restorehealth")
if repair_command == "!ActivatorWin10Pro":
    os.system("slmgr /ipk")
    os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
    os.system("slmgr /skms kms.xspace.in")
    os.system("slgr /ato")
    os.system("slmgr.vbs -xpr ")
if repair_command == "!ActivatorWin1ßEnterprise":
    os.system("slmgr.vbs /upk")
    os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
    os.system("slmgr /skms zh.us.to")
    os.system("slgr /ato")
    os.system("slmgr.vbs -xpr ")
if repair_command == "!CleanTempFiles":
    os.system("del /q /s %Temp%")
if repair_command == "!help":
    messagebox.showinfo("Commands Help", "Commands:" + commands)
if repair_command == "!CheckWinVer":
    print("My OS System is: " + platform.system() + " " + platform.version())

#print ending

print("Ending")



#
fertig = input("Press enter to end")


