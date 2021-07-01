from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

''' 
Using Selenium WebDriver avoid detecting scraper
by website by mimicking human actions
'''

driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--lang=en')  # change language to english
options.add_argument('headless')  # avoid opening browser


def scrape_nvd():
    for page in range(0,61,20):  # iterate over pages
        url = f'https://nvd.nist.gov/vuln/search/results?results_type=overview&form_type=Basic&search_type=last3months' \
              '&startIndex={page}'
        driver.get(url)
        
        rows = len(driver.find_elements_by_xpath('//*[@id="row"]/table/tbody/tr'))  # count rows
        columns = len(driver.find_elements_by_xpath('//*[@id="row"]/table/tbody/tr[1]/th'))  # count columns

        for row in range(1, rows + 1):
            for column in range(1, columns + 1):
                #  locate information by html tags using xpath | turn the WebElement into text
                title = driver.find_element_by_xpath(
                    '//*[@id="row"]/table/tbody/tr[' + str(row) + ']/th/strong/a').text
                desc = driver.find_element_by_xpath(
                    '//*[@id="row"]/table/tbody/tr[' + str(row) + ']/td[' + str(column) + ']/p').text
                date = driver.find_element_by_xpath(
                    '//*[@id="row"]/table/tbody/tr[' + str(row) + ']/td[' + str(column) + ']/span').text

                print(f'{title}, {date}')
                print(desc)
