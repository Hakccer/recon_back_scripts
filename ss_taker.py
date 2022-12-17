import sys
import threading
import subprocess
import os
import re

# Regex Compiler for getting link from a line
link_dectection_compiler = re.compile("(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])")


# Function For Grabbing only the link from a line
def removal(domain):
    try:
        data = link_dectection_compiler.search(domain)
        return data.group()
    except Exception as e:
        return None


# Function for take SS-ScreenShot of a single domain
def take_ss_for_single(domain):
    console_output = subprocess.run(f'gowitness single {domain}', capture_output=True, shell=True).stderr
    main_output = console_output.decode('utf-8')
    print(main_output)
    if 'This is usually a temporary error during hostname resolution and means that the local server did not receive ' \
       'a response from an authoritative server.' in main_output:
        return 2
    if 'ERR' in main_output:
        return 1
    return 0


if __name__ == '__main__':
    main_list = list(set(map(removal, open('cole.txt').readlines())))

    # In Testing

    # for i in range(len(list_by_file)):
    #     temp_list.append(list_by_file[i])
    #     if (i+1)%5 == 0:
    #         main_list.append(temp_list)
    #         temp_list = []
    #         continue
    #     if i == len(list_by_file)-1:
    #         main_list.append(temp_list)
    #         continue
    #
    # print(main_list)
    deads_list = []
    while len(main_list) > 0:
        remove_list = []
        for single_domain in main_list:
            ss_func_ouput = take_ss_for_single(single_domain)
            if ss_func_ouput == 2:
                deads_list.append(single_domain)
                remove_list.append(single_domain)
            if ss_func_ouput == 0:
                remove_list.append(single_domain)
        for single_in_error in remove_list:
            main_list.remove(single_in_error)

    print(f"There are {len(deads_list)} of domains that are dead")
    for dead in range(len(deads_list)):
        print(dead+1,deads_list[dead])
