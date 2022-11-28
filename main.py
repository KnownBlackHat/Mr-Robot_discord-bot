if __name__=="__main__":
  while True:
    import os
    os.system('python bot.py')
    os.system("pip install -r requirements.txt ")
    os.system("clear")
else:
  import requests
  from bs4 import BeautifulSoup
  import random        


  def proxy_generator():
    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html5lib')
    proxy = f"http://{random.choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))}"
    return proxy

