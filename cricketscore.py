import requests
from bs4 import BeautifulSoup
import time
# URL of the Cricbuzz match page
url = input('Match Link :')
leng=int(input('Len'))
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

timer_duration = 20



match_title = soup.find('h1', class_='cb-nav-hdr').text
print(match_title)
# Fetch the webpage
while True:
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser') # Match title
    try:
        comm=soup.find('p',class_="cb-com-ln").text
        live_score = soup.find('div', class_='cb-min-bat-rw').text  # Live score
        batters=soup.find("div", class_="cb-min-inf")
        recent=soup.find("div", class_="cb-min-rcnt").text
        key_stats=soup.find("div", class_="cb-key-lst-wrp").text
        match_status=soup.find("div", class_="cb-text-inprogress").text
        timer_duration=20
        print(live_score) 
        print() 
        for child in batters.find_all(recusive=False):
            if len(child.text.strip())<leng or child.text.strip().count(' ')>4:continue
            for child1 in child.find_all(recursive=False):
                    print(child1.text.strip(),end=' ')
            print()
        print()
        print(comm)
        print()
        print(key_stats)
        print()  
        print(recent)
        print(match_status)
    except AttributeError:
        if live_score:
            print(live_score)
        print()
        for child in batters.find_all(recusive=False):
            if len(child.text.strip())<leng or child.text.strip().count(' ')>4:continue
            for child1 in child.find_all(recursive=False):
                    print(child1.text.strip(),end=' ')
            print()
        print()
        print(comm)
        print()
        print(recent)
        print()
        print(key_stats)
        print("Match Paused!")
        timer_duration=120
        
    
    

      # 10 seconds

# Record the start time
    start_time = time.time()

# Run the loop while the timer is active
    while time.time() - start_time < timer_duration:
        time.sleep(1)  # Optional: Add delay to avoid rapid looping
    print()

# Extract score data
    