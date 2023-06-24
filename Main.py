import os
try:import httpx
except:os.system('pip install httpx > /dev/null')
try:import requests
except:os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
  os.system('chmod 777 pro.cpython-311.so;./pro.cpython-311.so')
else:
  exit(' Sorry Device Not Support ')
