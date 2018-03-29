from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/home/vatsalbabel/Work/Selenium/chromedriver')
driver.get('https://www.hackerearth.com/challenges/')

id = driver.find_elements_by_xpath("//div[@class='challenge-container']/div[@class='upcoming challenge-list']/div[@class='challenge-card-modern']/a[@class='challenge-card-wrapper challenge-card-link']")

HackerEarth = "HackerEarth.csv"
f = open(HackerEarth, 'w')

headers = "Name of Competition, Start, Close, Link\n"

f.write(headers)
f.write("\n")

print("Crawling Status:")
print()
print("total :"+str(len(id)))

count = 0

for ii in id:
	count += 1
	try:
		url = ii.get_attribute('href')
		page = urlopen(url)
		pagetext = page.read()
		page.close()
		soup = BeautifulSoup(pagetext, "html.parser")

		#Getting links
		link = soup.link['href'].strip()

		#Getting names
		containers = soup.findAll('div',{'class':'event-container'})
		for contain in containers:
			ctag = contain.findAll('div',{'class':'event-details-container'})
		ctag = ctag[0]	
		name = ctag.h1['title'].strip()

		#Getting timings
		for contain in containers:
			ctag = contain.findAll('div',{'class':'event-timings-container scrolling-enable'})
		for time in ctag:
			tt = time.findAll('div',{'class':'event-timings '})
		#Getting opens
		for opens in tt:
			tot = opens.findAll('p',{'class':'timing no-border'})
		for open_is in tot:
			tot_is = open_is.findAll('span',{'class':'timing-text dark regular weight-700'})	
		tot_is = tot_is[0]
		open_time = tot_is.text
		#Getting close
		for p in tt:
			close = p.findAll('p',{'class':'timing'})[1]
		gem = close.find('span',{'class':'timing-text dark regular weight-700'})
		close_time = gem.text

		f.write(name+","+open_time.replace(","," ")+","+close_time.replace(","," ")+","+link+"\n")
		del name,link,containers,contain,ctag,open_time,close_time
		print(str(count)+" -> SCRAPED")
	except:
		print(str(count)+" -> SCRAPING ERROR")
		break


f.close()
driver.close()

