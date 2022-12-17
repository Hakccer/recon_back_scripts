import subprocess
import time
import os
from base64 import b64encode

def port_scanner(data, list=False):
    try:
        if list:
            try:
                file = open(list)
                file.close()
                subprocess.run(f'naabu -list {list}', shell=True)
            except Exception as e:
                print(f"No File exist with name {list} and file should be in the .TXT format")
            return 0
        f_name = str(b64encode(os.urandom(20)).decode('utf-8'))
        print(f_name)
        subprocess.run(f'naabu -host {data} -o {f_name}.txt', shell=True)
        print("Scanning Finished Successfully...")
    except Exception as e:
        print("There is an unknow error retrying in 5 seconds...")
        time.sleep(5)
        port_scanner(data, list=list)

port_scanner('facebook.com', 'cole.txt')