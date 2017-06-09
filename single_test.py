import random
from coapclient import HelperClient
from coapthon import defines
from coapthon.messages.request import Request
import time
from Tkinter import *

def callback():
    try:
        index = listbox.curselection()[0]
        # get the line's text
        server_text = str(listbox.get(index))
        if(server_text==""):
            print "ERROR : Empty selection"
            return
    except:
        print "ERROR !"
        return AttributeError
    proxy_texter = str(label_proxy.cget("text"))
    text_test = path_text.get("1.0",END)
    path_texter = str(text_test)
    print "Selected : " + str(server_text)
    print "chosen path : "+str(path_texter)
    server_text = "198.199.92.83"
    proxy_texter = "104.236.174.175"
    # Setting up the application
    setup_time_begin = time.time()
    server_address = (str(proxy_texter), 5684)
    current_mid = random.randint(1, 1000)
    client = HelperClient(server_address)
    setup_time_end = time.time()

    print "Starting the first request"
    print "\nRequesting for Resource 1"
    first_request_begin = time.time()
    # Starting first request
    path = "/basic1"
    req = Request()
    req._usecache = use_cache
    req.code = defines.Codes.GET.number
    req.uri_path = path
    req.type = defines.Types["CON"]
    req._mid = current_mid
    req.destination = server_address
    req.proxy_uri = "coap://"+str(server_text)+":5683/basic1"
    received_message = client.send_request(req)
    first_request_end = time.time()
    time.sleep(21)


    print "Starting the second request"
    print "\nRequesting for Resource 1 again"
    second_request_begin = time.time()
    # Starting second request
    current_mid = current_mid+1
    req2 = Request()
    req2._usecache = use_cache
    req2.code = defines.Codes.GET.number
    path = "/basic1"
    req2.uri_path = path
    req2.type = defines.Types["CON"]
    req2._mid = current_mid
    req2.destination = server_address
    req2.proxy_uri = "coap://"+server_text+":5683/basic1"
    received_message = client.send_request(req2)
    second_request_end = time.time()

    time.sleep(5)

    print "Tearing down application"
    # Tearing down application
    print "DONE !"
    print "-------------------"
    print "Printing Analytics"
    print "--------------------"
    print "Build Time : " + str(setup_time_end-setup_time_begin)
    print "First request : "+str(first_request_end-first_request_begin)
    print "Second request : " + str(second_request_end - second_request_begin)
    print "--------------------------"
    print "TOTAL TIME TAKEN : " + str((second_request_end-second_request_begin)+(first_request_end-first_request_begin))
    print "--------------------------"

root = Tk()
root.title("CS237 : Caching DEMO")
root.geometry("500x500")
Label(root, text="CS237 : Group 25",font = "Verdana 10 bold").grid(row=0,column=1)
Label(root, text="Implementation of Caching in SCALE",font = "Verdana 10 bold").grid(row=1,column=1)
Label(root, text="Authors : Priyanka Ravi, \nSwaroopa Kadam, \nThejdeep Gudivada").grid(row=2,column=1)
Label(root, text="Please choose server : ").grid(row=3)
Label(root, text="Proxy : ").grid(row=4)
label_proxy = Label(root, text="104.236.174.175")
label_proxy.grid(row=4,column=1)
Label(root, text="Choose Path : ").grid(row=5)

path_text = Text(root,height=1, width=15)
path_text.grid(row=6,column=1)
use_cache = IntVar()
Label(root, text="Use Cache ? ").grid(row=7,column=0)
c = Checkbutton(root, text="", variable=use_cache)
c.grid(row=7,column=1)
b = Button(root, text="Send request", command=callback)
b.grid(row=8,column=1)
listbox = Listbox(root)
listbox.grid(row=3,column=1)
for item in ["104.131.165.12", "198.199.92.83"]:
    listbox.insert(END, item)


def final_run():
    print "Starting application"

    root.mainloop()

def main():
    final_run()

if __name__ == '__main__':
    main()
