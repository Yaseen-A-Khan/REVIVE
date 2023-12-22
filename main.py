# from bs4 import BeautifulSoup
# import requests

# html_text = requests.get('https://www.google.com/search?q=nearest+hospitals+to+me&oq=nearest+hos&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIGCAEQRRg5MgcIAhAAGIAEMgoIAxAAGLEDGIAEMgwIBBAAGBQYhwIYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBggHEEUYPKgCALACAA&sourceid=chrome&ie=UTF-8').text
# soup = BeautifulSoup(html_text,'html.parser')
# # print(soup.prettify())

# # print(html)

# quotes= soup.find_all('div',class_='main')

# # test = soup.find_all('div',id="Odp5De")
# print(quotes)
# # for i in main:
# #     tester=i.find('span')
# #     print(tester)
# #     print()
# #     print()

# # heading_object=soup.find_all( 'h3' )

# # print(heading_object)
# # for i in heading_object:
    
#     # print(i.getText())
# # jobs = soup.findall('a')
# # main = soup.find_all('span')
# # for i in main:
# #     tester = i.find_all('div')
# #     print(tester)
# # main = soup.find('div',id='cnt')
# # main = soup.find_all('div',class_="GyAeWb")

# # main = main.find('div',class_="yXg2De")
# # main = main.find('div')
# # (class_='main')'
# # print(main)from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from geopy.geocoders import Nominatim
import time

def get_hospitals_near_me():
    # Set up Selenium WebDriver with your browser driver
    driver = webdriver.Chrome(executable_path='./chromedriver')  # Update with the path to your driver

    try:
        # Open Google Maps
        driver.get("https://www.google.com/maps")

        # Get current location using GeoPy
        geolocator = Nominatim(user_agent="hospital_locator")
        location = geolocator.geocode("Your Location")  # Replace with your actual location
        latitude, longitude = location.latitude, location.longitude

        # Search for hospitals near your location
        search_box = driver.find_element("name", "q")
        search_box.send_keys("hospitals near me")
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load
        time.sleep(5)

        # Extract and print the names of the hospitals
        hospitals = driver.find_elements_by_css_selector(".section-result-title")
        for hospital in hospitals:
            print(hospital.text)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    get_hospitals_near_me()





