#imports
import os
import time
import platform
from tkinter import messagebox
import webbrowser

#Lvki Colors
HEADER =    '\033[95m'
OKBLUE =    '\033[94m'
OKCYAN =    '\033[96m'
OKGREEN =   '\033[92m'
WARNING =   '\033[93m'
FAIL =      '\033[91m'
ENDC =      '\033[0m'
BOLD =      '\033[1m'
UNDERLINE = '\033[4m'
Black =     "\u001b[30m"
Red =       "\u001b[31m"
Green =     "\u001b[32m"
Yellow =    "\u001b[33m"
Blue =      "\u001b[34m"
Magenta =   "\u001b[35m"
Cyan =      "\u001b[36m"
White =     "\u001b[37m"
Reset =     "\u001b[0m"
Valid =     f"{Reset}[{OKGREEN}+{Reset}]"
inValid =   f"{Reset}[{Red}-{Reset}]"
Warn =      f"{Reset}[{WARNING}!{Reset}]"
Question =  f"{Reset}[{OKBLUE}?{Reset}]"


while True:
    os.system("cls")
    print(f"""
    {OKBLUE}
                                        ███╗   ██╗███████╗ ██████╗ ███████╗██████╗ 
                                        ████╗  ██║██╔════╝██╔════╝ ██╔════╝██╔══██╗
                                        ██╔██╗ ██║█████╗  ██║  ███╗█████╗  ██████╔╝
                                        ██║╚██╗██║██╔══╝  ██║   ██║██╔══╝  ██╔══██╗
                                        ██║ ╚████║███████╗╚██████╔╝███████╗██║  ██║
                                        ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                    discord.gg/chairs

                                        {OKBLUE}┌╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾┑{Reset}
                                        {OKBLUE}│{Reset} [1] Reset                             {OKBLUE}│{Reset}
                                        {OKBLUE}│{Reset} [2] CheckSystemFiles                  {OKBLUE}│{Reset}
                                        {OKBLUE}│{Reset} [3] RepairSystemFiles                 {OKBLUE}│{Reset}
                                        {OKBLUE}│{Reset} [4] Activate Win10pro                 {OKBLUE}│{Reset}
                                        {OKBLUE}│{Reset} [5] Activate Win10pro Enterprise      {OKBLUE}│{Reset}
                                        {OKBLUE}│{Reset} [6] Clean Temp Files                  {OKBLUE}│{Reset}
                                        {OKBLUE}│{Reset} [7] Check Windows Version             {OKBLUE}│{Reset}
                                        {OKBLUE}│{Reset} [8] Discord                           {OKBLUE}│{Reset}
                                        {OKBLUE}└╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾┘{Reset}
""")
    Input = input(f"{OKBLUE}                        Input : ")
    if Input == "1":
        os.system("cls")
        print(f"{Valid} Cleaning Pc")
        time.sleep(1)
        os.system("systemreset -cleanpc")
        os.system("pause")
    if Input == "2":
        os.system("cls")
        print(f"{Valid} Checking System Files")
        time.sleep(1)
        os.system("sfc /scannow")
        os.system("pause")
    if Input == "3":
        os.system("cls")
        print(f"{Valid} Repairing System Files")
        time.sleep(1)
        os.system("DISM.exe /Online /Cleanup-image /Restorehealth")
        os.system("pause")
    if Input == "4":
        os.system("cls")
        print(f"{Valid} Activate Windows 10 pro")
        time.sleep(1)
        os.system("slmgr /ipk")
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /skms kms.xspace.in")
        os.system("slgr /ato")
        os.system("slmgr.vbs -xpr ")
        os.system("pause")
    if Input == "5":
        os.system("cls")
        print(f"{Valid} Activate Win10pro Enterprise")
        time.sleep(1)
        os.system("slmgr.vbs /upk")
        os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        os.system("slmgr /skms zh.us.to")
        os.system("slgr /ato")
        os.system("slmgr.vbs -xpr ")
        os.system("pause")
    if Input == "6":
        os.system("cls")
        print(f"{Valid} Cleaning temp")
        time.sleep(1)
        os.system("del /q /s %Temp%")
        os.system("pause")
    if Input == "7":
        os.system("cls")
        print(f"{Valid} Checking Windows Version")
        time.sleep(1)
        print("My OS System is: " + platform.system() + " " + platform.version())
        os.system("pause")
    if Input == "8":
        os.system("cls")
        print(f"{Valid} Opening Discord")
        time.sleep(1)
        webbrowser.open("discord.gg/chairs")


        os.system("pause")

