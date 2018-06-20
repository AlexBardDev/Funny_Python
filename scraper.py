import requests
from lxml import html

link = "https://github.com/"

#Get the web page
web_page = requests.get(link + "AlexBardDev")

#Get an HTML element
data = html.fromstring(web_page.content)

#Parse the data with xpath
name = data.xpath("//span[@class='p-nickname vcard-username d-block']")[0].text_content()
repositories = data.xpath("//a[@title='Repositories']")[0].get("href")

#Print the results
print("""Lien vers les repositories du profil {} : {}""".format(name, link + repositories))
