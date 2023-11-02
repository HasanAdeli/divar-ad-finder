from time import sleep
from finder import AdFinder


url = 'https://divar.ir/s/tehran/rent-residential'
finder = AdFinder(url)
crawling = True
while crawling:
    ads = finder.run()
    for ad in ads:
        print(ads)

    sleep(30)
    print('*' * 200)
