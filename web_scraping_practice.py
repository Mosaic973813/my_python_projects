import requests
from bs4 import BeautifulSoup
import pandas as pd #lets you store data like a spreadsheet

url = "https://quotes.toscrape.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(response.status_code) # should be 200 if succesful

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    data = [] #creating an empty dictionary for excel

    for quote in quotes: #prints the full content of each quote block
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        #print(f"{text} - {author}")
        data.append({"Quote": text, "Author": author}) #adding the quote and author to the dictionary

#To save to an excel sheet please see below.

    df = pd.DataFrame(data)
    df.to_excel("quotes.xlsx", index=False)
    print("Saved quotes to quotes.xlsx")
else:
    print("Failed to retrieve the page.")



#print(response.text[:500]) #shows the first 500 characters

