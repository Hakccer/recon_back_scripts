import subprocess
import base64
import os
import time

def removal(ele):
    return ele[0:len(ele)-2]

once = False
def do_analysis(file_name):
    global once
    try:
        key = str(base64.b64encode(os.urandom(20)).decode('utf-8'))
        subprocess.run(f'cat {file_name} | subjs | tee {key}.txt', shell=True)
        file = open(f"{key}.txt")
        dats = list(map(removal, file.readlines()))
        for i in dats:
            subprocess.run(f'''echo "{i}" | python jsa.py''', shell=True)
    except Exception as e:
        if once:
            print("Sorry its not working")
            return
        print(e)
        print("Error Occured")
        print("Retrying in 5 seconds...")
        time.sleep(5)
        once = True
        do_analysis(file_name)

do_analysis('cole.txt')