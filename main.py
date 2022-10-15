import os
#os.system("python -m poetry add disnake")
os.system("pip install -r requirements.txt ")
os.system("clear")

os.system('pip freeze > pip_log.txt')
os.system('python bot1.py &> bot1.log & ')
os.system('python bot2.py &> bot2.log & ')
os.system('python bot.py')
