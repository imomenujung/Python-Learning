# import all necessary libraries
import requests 
import pandas as pd
from bs4 import BeautifulSoup 

# define url of webpage to scrape from
url = "https://books.toscrape.com"

# send a request to get html code from the url and save the response 
response = requests.get(url, headers={"Accept": "text/html"}) 

# use BeautifulSoup to parse the text from the response 
parsed_response = BeautifulSoup(response.text, "html.parser") 

# find all book titles 
# uncomment the following line of code and FILL IN
titles = parsed_response.find_all("h3")
prices  = parsed_response.find_all("p", class_= "price_color")

# create lists to store the cleaned data
cleaned_titles = []
cleaned_prices = []

# iterate over the titles and prices, and clean the text for each
for title in titles:
    cleaned_text = ' '.join(title.a["title"].split())
    cleaned_titles.append(cleaned_text)

for price in prices:
    cleaned_price = ' '.join(price.text.split())
    cleaned_prices.append(cleaned_price)

# create a DataFrame
books_df = pd.DataFrame({
    "Title": cleaned_titles,
    "Price": cleaned_prices
})

# display the DataFrame
print(books_df)