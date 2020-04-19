from TOOLS import ChifaScrapper
from GUI import GUI
from threading import Thread

# load the data
PATH = 'D:\\Chifa\\CHIFA_OFFICINE\\Cnas_Signed_Client'
scrapper = ChifaScrapper()
batch = scrapper.scrape(PATH)

gui = GUI()
gui.apply_theme()

# get today
import time 
today = time.strftime("%d/%m/%Y")
tt = 0
cnas = 0
casnos = 0
hc = 0
p0 = 0
p1 = 0
sales = 0.0
for item in batch:
    if item['date'] == today:
        tt += 1
        if item['center'][0] == '1':
            cnas += 1
        elif item['center'][0] == '2':
            casnos += 1
        elif item['center'][0] == '9':
            hc += 1
        post = item['bill'][-3]
        if post == '0':
            p0 += 1
        else:
            p1 += 1
        sales += float(item['mt'])

gui.set_todaytotal(tt)
gui.set_casnostotal(casnos)
gui.set_cnastotal(cnas)
gui.set_hctotal(hc)
gui.set_earnings(sales)
gui.set_post0(p0)
gui.set_post1(p1)
gui.start()