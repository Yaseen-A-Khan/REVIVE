from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.google.com/search?q=nearest+hospitals+to+me&oq=nearest+hos&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIGCAEQRRg5MgcIAhAAGIAEMgoIAxAAGLEDGIAEMgwIBBAAGBQYhwIYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBggHEEUYPKgCALACAA&sourceid=chrome&ie=UTF-8').text
soup = BeautifulSoup(html_text,'html.parser')
main= soup.prettify()
ls = soup.find_all('section',class_="lhs")
print(main)