#El Scrapo
import urllib.request
import datetime
import time
from bs4 import BeautifulSoup

currentDT = datetime.datetime.now()

# Scrape Steampowered for the statistics of PropHunt
def Scrape():
    quote_page = "http://steamcommunity.com/sharedfiles/filedetails/?id=135509255"
    page = urllib.request.urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    steam_stats_box = soup.find('table', attrs={'class': 'stats_table'})
    steam_stats = steam_stats_box.text.strip().replace("Unique Visitors", " UV | ").replace("Current Subscribers", " CS | ").replace("Current Favorites", " CF").replace("\n", "")

    # This is to make the tuple work with writing to files
    data = (datetime.datetime.now().strftime("%m/%d/%y, %I:%M %p") + " | " + steam_stats + "\n")

    # Write to text file
    with open("Steam Workshop PropHunt Data.txt","a") as file:
        file.write(data)
        #file.close()    
   
    
# Scrape every 10 minutes
while 1:
    Scrape()
    time.sleep(600)
