import os
#os.system("pip install -r requirements.txt")
while True:
    #os.system("pip install -r requirements.txt")
    os.system('python bot.py 2> Runtime.error')
    os.system("echo 'Run Failure at $(date)' >> fails;kill 1")
