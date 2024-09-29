from bs4 import BeautifulSoup as bs
import requests

path = "rates.txt"


def get():
    page = requests.get(
        "https://www.x-rates.com/table/?from=USD&amount=1")

    content = bs(page.content, features="html.parser")
    content = str(content.find_all(class_="ratesTable"))

    contentList = []

    for each in content.splitlines():
        if "rtRates" in each:
            contentList.append(each)

    print(len(contentList))

    newContentList = []
    for i in range(0, 124):
        if i % 2 == 0:  # The lines which we want to keep.
            newContentList.append(contentList[i])

    with open(path, "r") as f:
        if bool(f.read()) == True:
            with open(path, "w") as f:
                pass
    with open(path, "a") as f:
        for each in str(newContentList).splitlines():
            f.write(each)

    excRates = []
    for each in range(0, 3):  # USD to Euros, Pounds, Rupees
        rate = str(newContentList[each][81:90])
        if "<" in rate:
            rate = rate.replace("<", "")
        excRates.append(rate)
        # print(rate)

    return excRates
