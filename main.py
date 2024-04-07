from bs4 import BeautifulSoup
with open("website.html") as file:
    contents=file.read()
soup=BeautifulSoup(contents, "html.parser")
all_anchor_tags=soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get("href"))

heading=soup.find_all(name="h1", class_="heading")    
print(heading)