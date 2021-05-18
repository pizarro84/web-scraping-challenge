from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import pymongo




conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db
collection = db.articles



def scrape():

    from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)




    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')


    news = soup.find_all('div', class_="content_title")
    news_title=news[1].text
    news_title


    para = soup.find_all('div', class_="article_teaser_body")
    news_p=para[0].text
    news_p



    url_img = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url_img)




    html = browser.html
    soup = BeautifulSoup(html, 'lxml')



    photo = soup.find_all('', class_="showimg fancybox-thumbs")



    for i in photo:    
        pic = i['href']
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/' + pic
    featured_image_url



    table_url = "https://space-facts.com/mars/"




    tables = pd.read_html(table_url)
    tables




    df = tables[0]
    df.columns = ["Info", "Mars"]
    mars_facts = df.to_html()
    mars_facts


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    Hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(Hemispheres_url)




    browser.click_link_by_partial_text('Cerberus')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    photos = soup.find_all("a", target="_blank")

    all_img_url = []

    for photo in photos:
        if photo.text.strip() == "Sample":
            image_url = photo["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    all_img_url.append(a)

    all_img_url



    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")




    photos = soup.find_all("a", target="_blank")

    for photo in photos:
        if photo.text.strip() == "Sample":
            image_url = photo["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    all_img_url.append(a)

    all_img_url



    browser.click_link_by_partial_text('Major Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    photos = soup.find_all("a", target="_blank")

    for photo in photos:
        if photo.text.strip() == "Sample":
            image_url = photo["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    all_img_url.append(a)

    all_img_url



    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    photos = soup.find_all("a", target="_blank")

    for photo in photos:
        if photo.text.strip() == "Sample":
            image_url = photo["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    all_img_url.append(a)

    all_img_url

    Mars_dict = {
            "news_title" : news_title,
            "news_p" : news_p,
            "featured_image_url" : featured_image_url,
            "mars_facts" : mars_facts,
            "hemisphere_image_urls": all_img_url
        }
    print(Mars_dict)
    return Mars_dict

if __name__ == "__main__":
    scrape()


