import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["https://www.amazon.co.jp/"]

while True:
    # if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
    if dt.now() != dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("Working hours...")
        with open(hosts_temp,'r+', encoding="utf-8") as file:
            content=file.read()
            print(content)
    else:
        print("Fun hours...")
    time.sleep(5)