
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

page_url = "https://www.federalreserve.gov/newsevents/pressreleases.htm"
news_release = []
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.get(page_url)
driver.maximize_window()
time.sleep(1)


article_links = driver.find_elements(By.XPATH, '//*[@id="article"]//p[1]/span/a')


# Step 2: Store hrefs or elements because they become stale after navigating
links = [link.get_attribute("href") for link in article_links if link.get_attribute("href") is not None]


# Step 3: Visit each link one at a time
for link in links:
    driver.get(link)
    time.sleep(1)

    title = driver.title
    description_element = driver.find_element(By.XPATH, '//*[@id="article"]/div[3]/p')
    release_date = driver.find_element(By.XPATH, '//*[@id="article"]/div[1]/p[1]')

    news_release.append({
        'title': title,
        'Article': description_element.text,
        'date': release_date.text
    })

    # Optional short pause before next iteration
    time.sleep(0.5)



with open('News_release_FED.csv', 'w', encoding='utf-8', newline='') as csv_file:
	# initializing the writer object to insert data
	# in the CSV file
	writer = csv.writer(csv_file)

	# writing the header of the CSV file
	writer.writerow(['title', 'Article', 'date'])

	# writing each row of the CSV
	for article in news_release:
	    writer.writerow(article.values())

# terminating the operation and releasing the resources
csv_file.close()
