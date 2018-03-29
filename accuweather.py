#Server script 

from urllib.request import urlopen
from selenium import webdriver

driver = webdriver.Chrome('/home/vatsalbabel/Work/Selenium/chromedriver')

#Converting the int type date format to string type date format 
int_month = [1,2,3,4,5,6,7,8,9,10,11,12]
string_month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
date = input('Enter a date - ')
month = int(input('Enter a month - '))
for i in range(0,len(int_month)):
	if(month==int_month[i]):
		full_date = date + ' ' + string_month[i]
		break

#Generating the search query for google
city_name = input('Enter a city - ')
search = city_name + ' ' + full_date + ' ' + 'accuweather.com'
google = 'https://www.google.co.in/?#q='+search

#Selenium inspect code
driver.get(google)
id = driver.find_elements_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/h3/a')
ii = id[0]
name = ii.get_attribute('href')
driver.get(name)
to_find = str(month) + "/" + date
del id
id = driver.find_elements_by_xpath('//*[@id="panel-main"]/div[2]/div/div/table/tbody/tr')
tr_count = 0;
for ii in id:
	tr_count = tr_count + 1
	td_count = 0
	list = ii.find_elements_by_xpath('.//td')
	for jj in list:
		td_count = td_count + 1
		try:
			next = jj.find_element_by_xpath('.//div/h3/time').text
			if(to_find==next):
				fi_xpath = '//*[@id="panel-main"]/div[2]/div/div/table/tbody/tr['+str(tr_count)+']/td['+str(td_count)+']/div/div[2]/div[2]'
				condition = driver.find_element_by_xpath(fi_xpath).text
				fi_xpath = '//*[@id="panel-main"]/div[2]/div/div/table/tbody/tr['+str(tr_count)+']/td['+str(td_count)+']/div/div[2]/div[1]/span[1]'
				max_temp = driver.find_element_by_xpath(fi_xpath).text
				fi_xpath = '//*[@id="panel-main"]/div[2]/div/div/table/tbody/tr['+str(tr_count)+']/td['+str(td_count)+']/div/div[2]/div[1]/span[2]'
				min_temp = driver.find_element_by_xpath(fi_xpath).text
				print(max_temp	+min_temp+"\t"+condition)
				sys.exit(0)
				break
		except:
			pass

driver.close()			


#Alteration for list type values for next
'''
	next = jj.find_elements_by_xpath('.//div/h3/time')
	if(len(next)!=0):
		next = next[0].text
	if(to_find==next):
		fi_xpath = '//*[@id="panel-main"]/div[2]/div/div/table/tbody/tr['+str(tr_count)+']/td['+str(td_count)+']/div/div[2]/div[2]'
		condition = driver.find_element_by_xpath(fi_xpath).text
		fi_xpath = '//*[@id="panel-main"]/div[2]/div/div/table/tbody/tr['+str(tr_count)+']/td['+str(td_count)+']/div/div[2]/div[1]/span[1]'
		max_temp = driver.find_element_by_xpath(fi_xpath).text
		fi_xpath = '//*[@id="panel-main"]/div[2]/div/div/table/tbody/tr['+str(tr_count)+']/td['+str(td_count)+']/div/div[2]/div[1]/span[2]'
		min_temp = driver.find_element_by_xpath(fi_xpath).text
		print(max_temp	+min_temp+"\t"+condition)
		sys.exit(0)
		break
'''


