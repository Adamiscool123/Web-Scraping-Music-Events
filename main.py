import requests
import selectorlib
from send_email import send_email
import time

URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """Scrape the page source from the url"""
    response = requests.get(url)
    text = response.text
    return text

def extract(text):
    """Extract band name or if no tour from text variable"""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(text)["tours"]
    return value

def store(extrac):
    with open("data.txt", "a") as file:
        file.write(extrac + "\n")

def read(extra):
    with open("data.txt", "r") as file:
        return file.read()

if __name__ == '__main__':
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content = read(extracted)
        if extracted != "No upcoming tours":
            if not extracted in content:
                store(extracted)
                send_email(message="Hey a new event was found!")
                print("An email was sent!")
        time.sleep(1)