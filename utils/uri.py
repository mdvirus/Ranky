from re import findall
#To prevent cloudflare captcha issues
import cloudscraper


def uri(link):
    if link == "":
        return "0"
    else:
        #Instantiate a scraper
        scraper = cloudscraper.create_scraper()
        return findall(r'<span>Solved:</span>\s*(.*?)\s*</li>', scraper.get(link).text)[0]
