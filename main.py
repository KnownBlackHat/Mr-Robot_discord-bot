import os
#os.system("python -m poetry add disnake")
os.system("pip install -r requirements.txt ")
os.system("clear")

os.system('pip freeze > pip_log.txt')
os.system('python bot_generator.py Known_Black_Hat 1 "Our World Getting Hacked" false & ')
os.system('python bot_generator.py Cyber_Girl 4 "Over This Server" false & ')
os.system('python bot_generator.py Desus 2 "Join Us" false & ')
os.system('python bot.py')
