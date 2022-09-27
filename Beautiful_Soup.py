import xlsxwriter as xlsxwriter
from bs4 import BeautifulSoup
import requests
import time
import csv
import datetime
import smtplib
from datetime import datetime
import arrow
import datetime as dt
import pandas as pd
import csv




# Connect to a wesbite
URL = 'https://www.amazon.in/product-reviews/B07S31CP9G/ref=acr_dp_hist_5?ie=UTF8&filterByStar=five_star&reviewerType=all_reviews#reviews-filter-bar'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
page = requests.get(URL, headers=headers)

# Extracting the content from whole page
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

reviews = soup2.find_all('div', {'data-hook': 'review'})

for review in reviews:
            title = review.find('a', {'data-hook': 'review-title'}).text.strip()
            rating = float(review.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip())
            body = review.find('span', {'data-hook': 'review-body'}).text.strip()
            dates = review.find('span', {'data-hook': 'review-date'}).text.strip()
            dates = dates.replace("Reviewed in India on", "")
            final_reviews = {'Title': title, 'rating': rating, "Description": body, 'Date': dates}


df = pd.DataFrame(data=final_reviews, index=[1])
df.to_excel("students.xlsx", index=False)
print("Dictionary converted into excel...")



