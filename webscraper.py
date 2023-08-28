from bs4 import BeautifulSoup
import requests

ufc_website = "https://www.ufc.com/events#events-list-upcoming"
response = requests.get(ufc_website)

soup = BeautifulSoup(response.text, "html.parser")

event_date_elements = soup.find_all(
    class_="c-card-event--result__date tz-change-data")

for element in event_date_elements:
    date = element.get("data-main-card")
    print(date)

event_headlines = soup.find_all("h3", class_="c-card-event--result__headline")
for event in event_headlines:
    fighters = event.find("a")
    print(fighters.text)
