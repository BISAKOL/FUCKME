import os, sys 
os.system("git pull")
try:
    _import_("menu").Subscraption() 
except Exception as e: 
  exit(str(e))
