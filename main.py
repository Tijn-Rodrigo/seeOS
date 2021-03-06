# File: seeos.py
# created: Sat 4 june 

# Import Libary's
import os
import time
from sys import platform
import platform

try:
	from termcolor import colored
except ImportError:
	print("seeOS (v1.0) ran into an error.")
	print("module termcolor not found.")
	print("")
	print("Input/commands are case sensitive.")
	import_err = input("Want to install termcolor? Type 'YES'to install, 'NO' to cancel: ")
	
	if import_err == ("YES"):
		os.system("clear")
		print("[+] Installing Termcolor...")
		os.system("pip3 install termcolor")
		print("")
		print
		
	elif import_err == ("NO"):
		os.system("clear")
		print("[+] Installation canceled!")
		print("")
		print("remember that seeOS requires python 3, pip3 and module(termcolor)")
		time.sleep(2)
		quit()

def banner():
	print("""
                   ____  _____
   ________  ___  / __ \/ ___/
  / ___/ _ \/ _ \/ / / /\__ \ v1.0
 (__  )  __/  __/ /_/ /___/ / 
/____/\___/\___/\____//____/  

seeOS let you see your PC information such as CPU, Device name, architecture and OS.

	""")

def main():
	print("""
                   ____  _____
   ________  ___  / __ \/ ___/
  / ___/ _ \/ _ \/ / / /\__ \ v1.0
 (__  )  __/  __/ /_/ /___/ / 
/____/\___/\___/\____//____/ 
 """)
	print(colored("Your Device information: ", 'yellow'))
	print("=========================================")
	print("")
	print("OS: "+ platform.system())   
	print("CPU: " + platform.processor())
	print(platform.architecture())
	print("Device Name: " + platform.machine()) 
	print("")
	print("=========================================")
	
def runtime():
	banner()
	print(colored("Loading System info...", 'green'))
	time.sleep(5)
	os.system("clear")
	main()
	
runtime()
