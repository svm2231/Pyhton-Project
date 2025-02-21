import requests
from bs4 import BeautifulSoup
import time
# URL of the Cricbuzz match page
url = input()
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

timer_duration = 20



match_title = soup.find('h1', class_='cb-nav-hdr').text
print(match_title)
# Fetch the webpage
while True:
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser') # Match title
    live_score = soup.find('div', class_='cb-min-bat-rw').text  # Live score
    match_status=soup.find("div", class_="cb-text-inprogress").text
    recent=soup.find("div", class_="cb-min-rcnt").text
    batters=soup.find("div", class_="cb-min-inf")
    partneship=soup.find('div',class_="cb-min-itm-rw").text
    
    
    print(f"Live Score: {live_score}")
    for child in batters.find_all(recusive=False):
         if len(child.text.strip())<15:continue
         for child1 in child.find_all(recursive=False):
            print(child1.text.strip(),end=' ')
         print()  

       
    print(recent)
    print(match_status)

      # 10 seconds

# Record the start time
    start_time = time.time()

# Run the loop while the timer is active
    while time.time() - start_time < timer_duration:
        time.sleep(1)  # Optional: Add delay to avoid rapid looping
    print()

# Extract score data
    