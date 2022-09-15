import os
#os.system("python -m poetry add disnake")
while True:
    os.system("clear")
    print("[+] Installing Required Modules...")
    os.system("pip install -r requirements.txt &> pip.log")
    print("[=] Starting Bot...")
    os.system('python bot.py')
