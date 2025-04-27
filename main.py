import requests
import selectorlib
from send_email import send_email
import time
import sqlite3

connection = sqlite3.connect("data.db")

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
    """Store new data"""
    row = extrac.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()

def read(extrac):
    """Read data"""
    row  = extrac.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE Band = ? AND City = ? AND Date = ?", (band, city, date))
    rows1 = cursor.fetchall()
    return rows1

if __name__ == '__main__':
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_email(message="Hey a new event was found!")
                print("An email was sent!")
        time.sleep(1)