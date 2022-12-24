#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import os
import sys

dir = os.getcwd() + "/.config/polybar/hack/scripts"
file  = "/dataDolarBs.json"
URL = "https://monitordolarvenezuela.com/"

def formatTitle(idx, title):
    if idx == 0:
        return "BCV"
    elif idx == 1:
        return "Paralelo"
    else:
        return title

if len(sys.argv) > 1 and sys.argv[1] == "show":
    with open(dir+file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for amount in data:
        print(amount["title"],amount["amount"])

elif len(sys.argv) == 1:
    print("%{F#00C400}流%{F-}")
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    divFather = soup.find(class_="row text-center")
    divChildren = divFather.find_all("div", class_="col-12 col-sm-4 col-md-2 col-lg-2")

    #0,1,5
    myJson = []
    for idx in [0,1,5]:
        tempTitle = divChildren[idx].find("h4", class_="title-prome").text
        title = formatTitle(idx, tempTitle)
        amount = divChildren[idx].find("p").text
        myJson.append(
            {
                "title":title,
                "amount":amount
            }
        )
    with open(dir+file, 'w') as file:
        json.dump(myJson, file, indent=4)