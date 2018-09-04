import requests
import cfscrape     #https://github.com/Anorov/cloudflare-scrape

def get_content(url="", ANTISPAM=False):
    if not ANTISPAM:
        res = requests.get(url)
        content = res.text
        status = res.status_code
    else:
        scraper = cfscrape.create_scraper(delay=5) #for cloudflare use this one
        res = scraper.get(url)
        content = res.text
        #content = res.content.decode("utf-8")
        status = res.status_code
    return content, status
    
    
if __name__ == "__main__":
    url = input("put url here and press enter:\n")
    content, status = get_content(url)
    print("status: {}\ncontent: {}".format(status, content))