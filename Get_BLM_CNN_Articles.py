from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import time
from selenium import webdriver
import pandas as pd

# Create a chrome driver to search CNN's website and get articles related to the search
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=chrome_options)

# Dictionary for getting articles from CNN
# The URL gets 100 articles at a time, this was the max that one page on CNN would load
cnn_dict = {
    "url": "https://www.cnn.com/search?size=100&q=black%20lives%20matter&category=us&type=article&from=",
    "domain_url": "https://www.cnn.com",
    "class": {"class": "cnn-search__results-list"}
}

all_articles = [] # Stores all results from the CNN searches

# At the time of creating this there were 10 pages of search results from CNN's website relating to Black Lives Matter in the US
# Multiplying j by 100 will search for 100 new articles each time it is called
# Sleep must be called to slow the requests down in order to pull all the necessary data
for j in range(0, 10, 1):
  url_request = driver.get(cnn_dict["url"]+str(j*100))
  time.sleep(2)

  html = driver.page_source
  page_soup = soup(html, "html.parser")
  domain_url = cnn_dict["domain_url"]
  site_class = cnn_dict["class"]
  text_sections = page_soup.find("div", site_class).find_all("a")
  all_articles.append(text_sections)


# Article Urls stores all urls found in the search, in order to store them later
# The following for loop gets the results of the previous search
# i is incremented by 2 to avoid duplicate results since CNN's wesite has 2 links stored under href
# https: is added in order to create a valid link
article_urls = []
for j in all_articles:
  for i in range(0, len(j), 2):
          t = "https:" + j[i].get("href")
          article_urls.append(t)


used_article_urls = []  # Stores the articled URLS that have "BLM" or "Black Lives Matter" in the headline
headlines = []          # Stores the headlines of articles that have "BLM" or "Black Lives Matter"
article_text = []       # Stores the content of the articled that have "BLM" or "Black Lives Matter" in the headline
training_text = []      # Stores the text from the articles that DO NOT have "BLM" or "Black Lives Matter" in the headline

# The following function iterates through the URLS that were scraped in the search on CNN and returns it back to the caller
def text_f_html(read_html, html_func, parse_section):
    page_soup = soup(read_html, "html.parser")
    for i in article_urls:
         text_sections = page_soup.find_all(html_func, {"class": parse_section})
         joined_texts = ""
         for j in text_sections:
            joined_texts = joined_texts + " " + j.text
         return joined_texts

# The following loops through the article URL's collected in search and pulls the html text from each
# Each headline from the url is searched for the text "Black Lives Matter" or "BLM"
  # If the headline contains "BLM":
    # All instances of "BLM" in the header are changed to "Black Lives Matter"
    # The headline is stored to be the prefix of the GPT2 trained model
    # The text is store for data observation and analysis
  # If the headline does not contain "BLM" or "Black Lives Matter":
    # The text of the article will be used to train the GPT2 software
for i in article_urls:
    uClient = uReq(i)
    read_html = uClient.read()

    headline = text_f_html(read_html,"h1","pg-headline")
    temp_headline = headline.lower()

    if "black lives matter" in temp_headline or "blm" in temp_headline:
      headline = headline.replace("BLM", "Black Lives Matter")
      headlines.append(headline)
      article_text.append(text_f_html(read_html, "div","zn-body__paragraph"))
      used_article_urls.append(i)
    else:
      training_text.append(text_f_html(read_html, "div","zn-body__paragraph"))

# The following creates a text file of articles whos headline did NOT contain "BLM" or "Black Lives Matter"
file = open("/content/BLM_CNN_GPT2_training.txt", "w")
for i in training_text:
  file.write(i)
  file.write("\n")
file.close()

# Dictionary to create .csv file with all articles who contain "BLM" or "Black Lives Matter"
retrievedArticles = {
    'Article_Urls': used_article_urls,
    'Headlines' : headlines,
    'Article_Text' : article_text
}

#Data frame to export the articles as a .csv
df = pd.DataFrame(retrievedArticles, columns=['Article_Urls','Headlines','Article_Text'])
df.index.name = 'Index'
df.to_csv(r'/content/BLM_CNN_articles.csv', index = True, header = True)

print(df)

