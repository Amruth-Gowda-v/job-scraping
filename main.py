from bs4 import BeautifulSoup
import requests
import csv

response = requests.get(
    "https://realpython.github.io/fake-jobs/"
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

jobs = soup.find_all(
    "div",
    class_="card-content"
)

job_list = []

for job in jobs:

    title = job.find("h2").text.strip()

    company = job.find("h3").text.strip()

    job_list.append([title, company])

with open(
    "jobs.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow(["Job Title", "Company"])

    writer.writerows(job_list)

print("CSV created successfully!")




   
