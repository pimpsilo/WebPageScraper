from bs4 import BeautifulSoup
import requests
import csv


# prompt user for URL
url = input("Enter a URL: ")

# send a GET request to the URL and get the response
response = requests.get(url)

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# find all <a> tags on the page
links = soup.find_all("a")

# create a list to hold the link and description data
data = []

# loop through each link and extract the link and description
for link in links:
    href = link.get("href")
    text = link.get_text()
    data.append([text, href])

# write the data to a CSV file
with open("links.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Description", "Link"])
    writer.writerows(data)
