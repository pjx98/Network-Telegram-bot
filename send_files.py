import requests
import Constants as keys
import time

def send_one_photo(file):
    token = keys.API_KEY
    photo_file = {'photo':open(file, 'rb')}
    
    url = "https://api.telegram.org/bot"
    args = "sendPhoto"
    chat_id = "-635737435"

    # start timer
    start = time.time()
    
    # Send image from bot to grp
    resp = requests.post(f"{url}{token}/{args}?chat_id={chat_id}", files=photo_file)
    
    #End timer
    end = time.time()
    time_taken = end - start
    #resp = requests.post("https://api.telegram.org/bot2090233106:AAFHri1_edUW8qWHOdwPEIOjhogseh8226s/sendPhoto?chat_id=-2090233106", files=files)
    print(resp.status_code, resp.reason, time_taken)
    
def send_one_file(file):
    token = keys.API_KEY
    doc_file = {'document':open(file, 'rb')}
    
    url = "https://api.telegram.org/bot"
    args = "sendDocument"
    chat_id = "-635737435"

    # start timer
    start = time.time()
    
    # Send image from bot to grp
    resp = requests.post(f"{url}{token}/{args}?chat_id={chat_id}", files=doc_file)
    
    #End timer
    end = time.time()
    time_taken = end - start
    #resp = requests.post("https://api.telegram.org/bot2090233106:AAFHri1_edUW8qWHOdwPEIOjhogseh8226s/sendPhoto?chat_id=-2090233106", files=files)
    print(resp.status_code, resp.reason, time_taken)


# n: number of times to invoke the sending file function
def send_photo(n,file):
    
    
    start = time.time()

    for i in range(n):
        send_one_photo(file)

    end = time.time()
    time_taken = end - start
    
    print(end-start)
    
def send_file(n,file):
    
    
    start = time.time()

    for i in range(n):
        send_one_file(file)

    end = time.time()
    time_taken = end - start
    
    print(end-start)
    
#file = "./35_KB_photo.jpg"
file = "./45MB.pdf"


send_file(5,file)
#send_photo(1,file)