import requests
from bs4 import BeautifulSoup
from tkinter import *

url = 'https://issue.zum.com/'
response = requests.get(url)
tk = Tk()

rank = []

# Title
tk.title("Trends")

# Label
label = Label(tk, text = "Trends", font = ("맑은 고딕", 20, 'bold'))
label.pack(side = TOP)

# Text
text = Text(tk,  font = ("맑은 고딕", 13))

if response.status_code == 200:
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    ul = soup.find("ul", {"id":"issueKeywordList"})
    num = ul.findAll("span", {"class":"num"})
    word = ul.findAll("span", {"class":"word"})
    for i in range(10):
        rank.append(word[i].text)

for i in range(10):
    text.insert(INSERT, f"{i+1}위 : {rank[i]}\n")
text.pack()

# GUI Resize
tk.geometry('400x300')
tk.resizable(False, False)

tk.mainloop() #pack tkinter
#ZUM Trends