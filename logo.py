import pyfiglet
  
name = input("Name: ")
result = pyfiglet.figlet_format(name, font = "slant")
print(result)