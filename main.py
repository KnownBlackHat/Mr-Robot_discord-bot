import os
#os.system("python -m poetry add disnake")
os.system("pip install -r requirements.txt ")
os.system("clear")

os.system('pip freeze > pip_log.txt')
os.system('python bot_generator.py 1 4 "Our World Getting Hacked" & ')
os.system('python bot_generator.py 2 4 "Over This Server" & ')

os.system('python bot.py')
