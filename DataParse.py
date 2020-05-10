import requests
from bs4 import BeautifulSoup
from itertools import islice


vgm_url = 'https://www.mygov.in/covid-19/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'lxml')

res=soup.text.split("COVID-19 Dashboard")[1].split("COVID-19 Statewise Status")
state_list=["Maharashtra", "Gujarat", "Delhi", "Tamil Nadu", "Rajasthan", "Madhya Pradesh", "Uttar Pradesh", "Andhra Pradesh", "Punjab", "West Bengal", "Telengana", "Jammu and Kashmir", "Karnataka", "Haryana", "Bihar", "Kerala", "Odisha", "Chandigarh", "Jharkhand", "Tripura", "Uttarakhand", "Assam", "Chhattisgarh", "Himachal Pradesh", "Ladakh", "Andaman and Nicobar", "Meghalaya", "Puducherry", "Goa", "Manipur", "Arunachal Pradesh", "Mizoram", "Dadra and Nagar Haveli"]
abbrivation=["Hie","hie","Hello","hello","Hey","hie", "Hi", "hi"]
#print(res[0])
print("*************************************")
s=[x[0] for x in state_list]
def resp(state):
    state.title()
    if state in state_list:
        op = res[0].split(state)[1].split("\n\n\n")[0]
        return "Total number of cases in "+state+" : " +op+ "\n\nStay Safe\nStay Home!"
    elif state in abbrivation:
        return "Hello Welcome! Enter name of any state of India to get corona status.\n\nStay Safe!\nStay Home!"
    elif state[0] in s:
        temp = []
        for x in state_list:
            if x.startswith(state[0]):
                temp.append(x)
        return "Do you mean?\n\n"+'\n'.join(temp)
    else:
        return "No data avaialble!\nReply with Correct spelling of state as follow :\n\n Maharashtra\nGujarat\nDelhi\nTamil Nadu\nRajasthan\nMadhya Pradesh\nUttar Pradesh\nAndhra Pradesh\nPunjab\nWest Bengal\nTelengana\nJammu and Kashmir\nKarnataka\nHaryana\nBihar\nKerala\nOdisha\nChandigarh\nJharkhand\nTripura\nUttarakhand\nAssam\nChhattisgarh\nHimachal Pradesh\nLadakh\nAndaman and Nicobar\nMeghalaya\nPuducherry\nGoa\nManipur\nArunachal Pradesh\nMizoram\nDadra and Nagar Haveli\n\nStay Safe\nStay Home!"
resp("Gujarat")


