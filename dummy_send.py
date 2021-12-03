import requests
import Constants as keys
import time

def send_text():
    token = keys.API_KEY_2
    text= "/start @networkTrack_bot"
    
    url = "https://api.telegram.org/bot"
    args = "sendMessage"
    chat_id = "-635737435"

    # start timer
    start = time.time()
    
    # Send image from bot to grp
    resp = requests.post(f"{url}{token}/{args}?chat_id={chat_id}&text={text}")
    
    #End timer
    end = time.time()
    time_taken = end - start
    #resp = requests.post("https://api.telegram.org/bot2090233106:AAFHri1_edUW8qWHOdwPEIOjhogseh8226s/sendPhoto?chat_id=-2090233106", files=files)
    print(resp.status_code, resp.reason, time_taken)
    
send_text()