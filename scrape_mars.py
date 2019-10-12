
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import time
from selenium import webdriver

def init_browser():
     executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
     return Browser('chrome', **executable_path, headless=False)


def scrape():

     browser = init_browser()
     # this dictionary will hold everything we pull from all the sites
     scraped_data = {}


     # NASA Mars News
     # 
     # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

     # site 1 - NASA News
     
     news_url = "https://mars.nasa.gov/news/" 
     browser.visit(news_url)
     html = browser.html
     soup = bs(html, "html.parser")

     #NASA article
     time.sleep(2)
     article = soup.find("div", class_='list_text')
     news_title = article.find("div", class_="content_title").text
     news_p = article.find("div", class_="article_teaser_body").text
     print(news_title)
     print(news_p)

     # JPL Mars Space Images - Featured Image
     # 
     # Visit the url for JPL Featured Space Image here.
     # 
     # Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
     # 
     # Make sure to find the image url to the full size .jpg image.
     # 
     # Make sure to save a complete url string for this image.


     # site 2 - NASA Image
     time.sleep(3)
     image_url="https://www.jpl.nasa.gov"
     search_url="/spaceimages/?search=&category=Mars"
     # use splinter to connect to the url and navigate, then use bs4 to repeat what you did in site 1
     browser.visit(image_url+search_url)
     html = browser.html
     soup = bs(html, "html.parser")
    


     path=soup.find("div", class_="carousel_items")
     relative_image_path = path.find("article", class_="carousel_item")["style"].split("'")[1]
     relative_image_path
     featured_image_url = image_url + relative_image_path
     featured_image_url


     # Mars Weather
     # 
     # Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. 
     # Save the tweet text for the weather report as a variable called mars_weather.

     # site 3 - Twitter Weather 
     tweet_url="https://twitter.com/marswxreport?lang=en"
     # grab the latest tweet and be careful its a weather tweet
     browser.visit(tweet_url)
     html = browser.html
     soup = bs(html, "html.parser")
     time.sleep(2)

     # Example:
     # mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'

     tweets = soup.find("div", class_='js-tweet-text-container')
     mars_weather = tweets.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

     print(mars_weather)


     # Mars Facts
     # 
     # Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
     # 
     # Use Pandas to convert the data to a HTML table string.
     # site 4 - 
     facts_url = 'https://space-facts.com/mars/'
     browser.visit(facts_url)
     html = browser.html
     soup = bs(html, "html.parser")
     time.sleep(2)


     # use pandas to parse the table
     facts=[]
     facts_df = pd.read_html(facts_url)[0]
     facts_df

     # facts_df.to_html('mars_facts.html')
     facts_string=facts_df.to_html(index=False, justify="center")

     # Mars Hemispheres
     # 
     # 
     # Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
     # 
     # You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
     # 
     # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
     # 
     # Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


     # site 5 
     hemisphere_image_urls = []
     # use bs4 to scrape the title and url and add to dictionary


     astro_url = 'https://astrogeology.usgs.gov'


     #Cerberus
     cerberus_url = '/search/map/Mars/Viking/cerberus_enhanced'
     browser.visit(astro_url+cerberus_url)
     html = browser.html
     soup = bs(html, "html.parser")
     time.sleep(2)

     hemi = soup.find("div", class_='wide-image-wrapper')
     hemi_path= hemi.find(class_='wide-image')["src"]
     image_url = astro_url + hemi_path
     print(image_url)
     soup.find(class_="")
     title=soup.find("h2", class_="title").text
     print(title)

     cerberus_data = {'title': title, 'img_url': image_url}
     cerberus_data


     # site 5 
     hemisphere_image_urls = []
     # use bs4 to scrape the title and url and add to dictionary

     url = 'https://astrogeology.usgs.gov/'
     astro_url='search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


     # #Cerberus

     browser.visit(url+astro_url)
     html = browser.html
     soup = bs(html, "html.parser")
     time.sleep(2)

     link = soup.find_all("div", class_='item')[0]
     url_link= link.find("a", class_='itemLink product-item')["href"]


     browser.visit(url+url_link)
     html = browser.html
     soup = bs(html, "html.parser")
     time.sleep(2)

     hemi = soup.find("div", class_='wide-image-wrapper')
     hemi_path= hemi.find(class_='wide-image')["src"]
     cerberus_url = url + hemi_path
     print(image_url)
     soup.find(class_="")
     cerberus_title=soup.find("h2", class_="title").text
     print(title)

     

     #Schiaparelli

     url = 'https://astrogeology.usgs.gov/'
     astro_url='search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

     browser.visit(url+astro_url)
     html = browser.html
     soup = bs(html, "html.parser")
     time.sleep(2)

     link = soup.find_all("div", class_='item')[1]
     link
     url_link= link.find("a", class_='itemLink product-item')["href"]
     # url_link

     browser.visit(url+url_link)
     html = browser.html
     soup = bs(html, "html.parser")
     time.sleep(2)

     hemi = soup.find("div", class_='wide-image-wrapper')
     hemi_path= hemi.find(class_='wide-image')["src"]
     schiaparelli_url = url + hemi_path
     print(image_url)
     soup.find(class_="")
     schiaparelli_title=soup.find("h2", class_="title").text
     print(title)




     #Syrtis Major
     url = 'https://astrogeology.usgs.gov/'
     astro_url='search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

     browser.visit(url+astro_url)
     html = browser.html
     soup = bs(html, "html.parser")
     time.sleep(2)

     link = soup.find_all("div", class_='item')[2]
     link
     url_link= link.find("a", class_='itemLink product-item')["href"]
     # url_link

     browser.visit(url+url_link)
     html = browser.html
     soup = bs(html, "html.parser")
     time.sleep(2)

     hemi = soup.find("div", class_='wide-image-wrapper')
     hemi_path= hemi.find(class_='wide-image')["src"]
     syrtis_major_url = url + hemi_path
     print(image_url)
     soup.find(class_="")
     syrtis_major_title=soup.find("h2", class_="title").text
     print(title)

     
     #Valles Marineris
     url = 'https://astrogeology.usgs.gov/'
     astro_url='search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

     browser.visit(url+astro_url)
     html = browser.html
     soup = bs(html, "html.parser")
     time.sleep(2)

     link = soup.find_all("div", class_='item')[3]
     link
     url_link= link.find("a", class_='itemLink product-item')["href"]
     # url_link

     browser.visit(url+url_link)
     html = browser.html
     soup = bs(html, "html.parser")
     time.sleep(2)

     hemi = soup.find("div", class_='wide-image-wrapper')
     hemi_path= hemi.find(class_='wide-image')["src"]
     valles_marineris_url=url + hemi_path
     
     soup.find(class_="")
     valles_marineris_title=soup.find("h2", class_="title").text
   


     #Store all data in dictionary
     mars_data = {
          "news_title": news_title,
          "news_paragraph": news_p,
          "featured_image": featured_image_url,
          "mars_weather": mars_weather,
          "facts_string": facts_string,
          "cerberus_title":  cerberus_title,
          "cerberus_url": cerberus_url,
          "schiaparelli_title": schiaparelli_title,
          "schiaparelli_url": schiaparelli_url,
          "syrtis_major_title": syrtis_major_title,
          "syrtis_major_url": syrtis_major_url,
          "valles_marineris_title": valles_marineris_title,
          "valles_marineris_url": valles_marineris_url
          }


     # Close the browser after scraping
     #
     browser.quit()

     return mars_data




