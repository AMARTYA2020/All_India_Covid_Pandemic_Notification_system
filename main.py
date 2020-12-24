from plyer import notification
import requests
from bs4 import BeautifulSoup //parsing skeleton page into meaning full JSON format

def notifyMe(title_message,display_message):
    notification.notify(
       title = title_message,
       message = display_message,
        app_icon = r"C:\Users\AMARTYA PANDEY\PycharmProjects\All_India_Covid_Pandemic_Notification_system\Corona.ico",
        timeout = 10

    )

def receive_data(url):
    req = requests.get(url)
    return req.text


if __name__ == "__main__":
    notifyMe("Amartya_Pandey","Virus infection growth rate and recovery rate is to be checked every moment")
    skeleton_data = receive_data("https://www.mohfw.gov.in")



   # print(skeleton_data)  # Random data is displayed but we have to display in an effective manner of covid cases
                          # in each cities with info of active cases and dischareged cases.

lets_praise = BeautifulSoup(skeleton_data,'html.parser')
print(lets_praise.prettify())

#for link in lets_praise.find_all('a'):  """ ALL anchor tag containing links gets printed """
#   print(link.get('href'))

#for table in lets_praise.find_all('table'):  """ FAIR ENOUGH !! Now by using table we can see covid cases in each city more precisely"""
#   print(table)

x = ""
"""
for tr in lets_praise.find_all('tbody')[1].find_all('tr'):
    print(tr.get_text()) 
"""

for tr in lets_praise.find_all('tbody')[1].find_all('tr'):
    x = x+tr.get_text()
print(x.split("\n"))


