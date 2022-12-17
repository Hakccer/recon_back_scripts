import subprocess
import os
from base64 import b64encode


def removal(ele):
    return ele[0:len(ele) - 2]


def detecter(listing):
    alive_ones = []
    for ele in listing:
        my_ele_list = str(ele).split(" ")
        if my_ele_list[1] == "[\x1b[32mSUCCESS\x1b[0m":
            alive_ones.append(my_ele_list[0])
    return alive_ones


def get_sub_domains(domain):
    key_1 = str(b64encode(os.urandom(20)).decode('utf-8'))
    key_2 = str(b64encode(os.urandom(20)).decode('utf-8'))

    subprocess.run(f'subfinder -d {domain} -o {key_1}.txt', shell=True)
    subprocess.run(f'httpx -list {key_1}.txt -silent -probe -o {key_2}.txt', shell=True)
    file = open(f'{key_2}.txt')
    sd = list(map(removal, file.readlines()))
    alives = detecter(sd)
    for k in alives:
        print(k)
    file = open('cole.txt', 'w')
    file.writelines(alives)
    file.close()


get_sub_domains('hotstar.com')
