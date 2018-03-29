from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

count = 0
main_url = 'https://www.techgig.com/job_search.php?page=1&rewritestr=Fresher'
driver = webdriver.Chrome('C:/Chrome Driver/chromedriver.exe')
driver.get(main_url)

id = driver.find_elements_by_xpath("//div[@class='normal-padding']/div[@class='append-question-detail-ajax']/div[@class='container']/div[@class='jobs-section']/div[@class='page-footer clearfix']/div[@class='pagination']/li")

fileh = 'CBH.csv'
f = open(fileh, 'w')

headers = "No., Name of Company, Last Date, Review, Skills,Title(As on website), Link\n"

f.write(headers)
f.write("\n")

number = int(len(id))
number1 = 0
count_number = 1
while(count_number != number):
	a = int(number1)
	a = str(a)
	b = int(count_number)
	b = str(b)
	main_url = main_url.replace(a,b)
	number1 = count_number
	driver.get(main_url)
	
	id = driver.find_elements_by_xpath("//div[@class='normal-padding']/div[@class='append-question-detail-ajax']/div[@class='container']/div[@class='jobs-section']/div[@class='row']/div[@class='col-md-4 col-sm-6']/div[@class='job-box']/div[@class='job-content']/h6/a")

	for ii in id:
		try:
			count += 1
			url = ii.get_attribute('href')
			page = urlopen(url)
			pagetext = page.read()
			page.close()
			soup = BeautifulSoup(pagetext, "html.parser")
			
			#Getting Link
			link = url.strip()
			
			#Getting Name
			name1 = soup.findAll('div',{'class':'two-column-layout'})
			name1 = name1[0]
			name = name1.div.div.div.div.article.div.div.p.span.text.strip()
			
			#Getting Expires On
			exp = soup.findAll('footer',{'class':'clearfix'})
			exp = exp[0]
			expire = exp.p.span.text.strip()
			expire = expire.replace('Expiring on - ','')	
			
			#Getting Title(as on website)
			htmlt = soup.findAll('html')
			htmlt = htmlt[0]
			title = htmlt.head.title.text.strip()
			title = title.replace('-',' ')
			
			#Getting info
			inst = soup.findAll('div',{'style':'display:none'})
			inst = inst[0]
			info = inst.div.p.text.strip()
			if(info.find('you need to attempt one skill assessment test')==32):
				info = 'You need to attempt one skill assessment test.'
			
			#Getting Skills
			ski = soup.findAll('div',{'class':'tags'})[0]
			skills = ski.text.strip()
			if(skills.find('C C++ Java')==-1):
                                skills = 'C C++ Java Software-Testing HTML Fresher'
			f.write(str(count)+","+name+","+expire.replace(',','')+","+info+","+skills+","+title+","+link+"\n")	
			print(str(count)+" -> SCRAPED")
		except:
			print(str(count)+" -> SCRAPING ERROR")
			break
	
	count_number = count_number + 1
f.close()
driver.close()

