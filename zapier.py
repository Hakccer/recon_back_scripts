#!/usr/bin/env python
import subprocess
import time
from zapv2 import ZAPv2

once = False
def crawler(tar):
    global once
    target = tar
    try:
        apiKey = 'je69lkpv4tunkeiu4nkd6ph0vn'

        zap = ZAPv2(apikey=apiKey)
        print('Spidering target {}'.format(target))
        scanID = zap.spider.scan(target)
        while int(zap.spider.status(scanID)) < 100:
            print('Spider progress %: {}'.format(zap.spider.status(scanID)))
            time.sleep(1)

        print('Spider has completed!')

        our_data = '\n'.join(map(str, zap.spider.results(scanID)))
        try:
            file = open('urls.txt', 'r')
            print("File already created with this name")
            file.close()
        except Exception as e:
            file = open('urls.txt', 'a')
            file.write(our_data)
            print("Successfull (File Created and urls added in it)")
            file.close()
    except Exception as e:
        if once:
            print("Sorry we can not help see whats the problem")
            return 0
        print("Trying to run it once more time in 3 seconds...")
        time.sleep(4)
        once = True
        crawler(target)


crawler('https://public-firing-range.appspot.com')