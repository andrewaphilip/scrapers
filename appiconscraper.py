import requests
from bs4 import BeautifulSoup
import pandas

#request html content and store to c variable
r=requests.get("https://www.apple.com/itunes/charts/free-apps/")
p=requests.get("https://www.apple.com/itunes/charts/paid-apps/")
c=r.content + p.content

#initiate BeautifulSoup's html parser
soup=BeautifulSoup(c,"html.parser")

#find all image tags in html
all=soup.find_all("img")

#make img tagged html a string for further splitting. Clean up extraneous information
txt = str((all)).replace("<img alt=","").replace('height="100"',"").replace('src=',"").replace('width="100"',"").replace("/>","").replace('"',"").replace('[',"").replace("]","")

#split string into list with title and url in the same item
x = txt.split(" , ") 

l=[] #create list variable to store dictionaries into
for item in x:
    y = item.split("  ") #further split each item in list x so that a new list is created with 0 being the app name and 1 being the url
    d={} #create the dictionary, d, to store each app and url pair into
    d["App"]=y[0] #set App as the key
    d["appUrl"]="https://apple.com"+y[1] #set appUrl as the value for the url
    l.append(d) #append the list so that we have a list of dictionaries

#use pandas to put our list of dictionaries into a .csv named appicons
df=pandas.DataFrame(l)
df.to_csv("appicons.csv")   
    
    