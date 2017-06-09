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
    time.sleep(5)


    print "Starting the second request"
    print "\nRequesting for Resource 2"
    second_request_begin = time.time()
    # Starting second request
    current_mid = current_mid+1
    req2 = Request()
    req2._usecache = use_cache
    req2.code = defines.Codes.GET.number
    path = "/basic2"
    req2.uri_path = path
    req2.type = defines.Types["CON"]
    req2._mid = current_mid
    req2.destination = server_address
    req2.proxy_uri = "coap://"+server_text+":5683/basic2"
    received_message = client.send_request(req2)
    second_request_end = time.time()

    time.sleep(5)

    print "Starting the third request"
    print "\nRequesting for Resource 3"
    third_request_begin = time.time()
    # Starting third request
    current_mid = current_mid + 1
    req3 = Request()
    req3._usecache = use_cache
    req3.code = defines.Codes.GET.number
    path = "/basic3"
    req3.uri_path = path
    req3.type = defines.Types["CON"]
    req3._mid = current_mid
    req3.destination = server_address
    req3.proxy_uri = "coap://"+server_text+":5683/basic3"
    received_message = client.send_request(req3)
    third_request_end = time.time()
    time.sleep(5)



    print "Starting the fourth request"
    print "\nRequesting for Resource 1 again"
    fourth_request_begin = time.time()
    # Starting first request
    path = "/basic1"
    current_mid = current_mid+1
    req4 = Request()
    req4._usecache = use_cache
    req4.code = defines.Codes.GET.number
    req4.uri_path = path
    req4.type = defines.Types["CON"]
    req4._mid = current_mid
    req4.destination = server_address
    req4.proxy_uri = "coap://" + server_text + ":5683/basic1"
    received_message = client.send_request(req4)
    fourth_request_end = time.time()
    time.sleep(5)


    print "Starting the fifth request"
    print "\nRequesting for Resource 2 again"
    fifth_request_begin = time.time()
    # Starting second request
    current_mid = current_mid+1
    req5 = Request()
    req5._usecache = use_cache
    req5.code = defines.Codes.GET.number
    path = "/basic2"
    req5.uri_path = path
    req5.type = defines.Types["CON"]
    req5._mid = current_mid
    req5.destination = server_address
    req5.proxy_uri = "coap://"+server_text+":5683/basic2"
    received_message = client.send_request(req5)
    fifth_request_end = time.time()
    time.sleep(5)

    print "Starting the sixth request"
    print "\nRequesting for Resource 3 again"
    # Starting third request
    sixth_request_begin = time.time()
    current_mid = current_mid + 1
    req6 = Request()
    req6._usecache = use_cache
    req6.code = defines.Codes.GET.number
    path = "/basic3"
    req6.uri_path = path
    req6.type = defines.Types["CON"]
    req6._mid = current_mid
    req6.destination = server_address
    req6.proxy_uri = "coap://"+server_text+":5683/basic3"
    received_message = client.send_request(req6)
    sixth_request_end = time.time()
    time.sleep(5)


    print "Starting the seventh request"
    print "\nRequesting for Resource 4"
    seventh_request_begin = time.time()
    # Starting first request
    path = "/basic4"
    current_mid = current_mid+1
    req7 = Request()
    req7._usecache = use_cache
    req7.code = defines.Codes.GET.number
    req7.uri_path = path
    req7.type = defines.Types["CON"]
    req7._mid = current_mid
    req7.destination = server_address
    req7.proxy_uri = "coap://" + server_text + ":5683/basic4"
    received_message = client.send_request(req7)
    seventh_request_end = time.time()
    time.sleep(5)


    print "Starting the eighth request"
    print "\nRequesting for Resource 5"
    eighth_request_begin = time.time()
    # Starting second request
    current_mid = current_mid+1
    req8 = Request()
    req8._usecache = use_cache
    req8.code = defines.Codes.GET.number
    path = "/basic5"
    req8.uri_path = path
    req8.type = defines.Types["CON"]
    req8._mid = current_mid
    req8.destination = server_address
    req8.proxy_uri = "coap://"+server_text+":5683/basic5"
    received_message = client.send_request(req8)
    eighth_request_end = time.time()
    time.sleep(5)

    print "Starting the ninth request"
    print "\nRequesting for Resource 6"
    ninth_request_begin = time.time()
    # Starting third request
    current_mid = current_mid + 1
    req9 = Request()
    req9._usecache = use_cache
    req9.code = defines.Codes.GET.number
    path = "/basic6"
    req9.uri_path = path
    req9.type = defines.Types["CON"]
    req9._mid = current_mid
    req9.destination = server_address
    req9.proxy_uri = "coap://"+server_text+":5683/basic6"
    received_message = client.send_request(req9)
    ninth_request_end = time.time()
    time.sleep(5)

    print "Starting the tenth request"
    print "\nRequesting for Resource 4 again"
    tenth_request_begin = time.time()
    # Starting third request
    current_mid = current_mid + 1
    req10 = Request()
    req10._usecache = use_cache
    req10.code = defines.Codes.GET.number
    path = "/basic4"
    req10.uri_path = path
    req10.type = defines.Types["CON"]
    req10._mid = current_mid
    req10.destination = server_address
    req10.proxy_uri = "coap://" + server_text + ":5683/basic4"
    received_message = client.send_request(req10)
    tenth_request_end = time.time()
    time.sleep(5)

    print "Starting the eleven request"
    print "\nRequesting for Resource 7"
    eleventh_request_begin = time.time()
    # Starting third request
    current_mid = current_mid + 1
    req11 = Request()
    req11._usecache = use_cache
    req11.code = defines.Codes.GET.number
    path = "/basic7"
    req11.uri_path = path
    req11.type = defines.Types["CON"]
    req11._mid = current_mid
    req11.destination = server_address
    req11.proxy_uri = "coap://" + server_text + ":5683/basic7"
    received_message = client.send_request(req11)
    eleventh_request_end = time.time()
    print "Tearing down application"
    # Tearing down application
    print "DONE !"
    print "-------------------"
    print "Printing Analytics"
    print "--------------------"
    print "Build Time : " + str(setup_time_end-setup_time_begin)
    print "First request : "+str(first_request_end-first_request_begin)
    print "Second request : " + str(second_request_end - second_request_begin)
    print "Third request : " + str(third_request_end - third_request_begin)
    print "Fourth request : " + str(fourth_request_end - fourth_request_begin)
    print "Fifth request : " + str(fifth_request_end - fifth_request_begin)
    print "Sixth request : " + str(sixth_request_end - sixth_request_begin)
    print "Seventh request : " + str(seventh_request_end - seventh_request_begin)
    print "Eighth request : " + str(eighth_request_end - eighth_request_begin)
    print "Ninth request : " + str(ninth_request_end - ninth_request_begin)
    print "Tenth request : " + str(tenth_request_end - tenth_request_begin)
    print "Eleventh request : " + str(eleventh_request_end - eleventh_request_begin)
    print "--------------------------"
    print "TOTAL TIME TAKEN : " + str((first_request_end-first_request_begin)+
(second_request_end - second_request_begin)+
(third_request_end - third_request_begin)+
(fourth_request_end - fourth_request_begin)+
(fifth_request_end - fifth_request_begin)+
(sixth_request_end - sixth_request_begin)+
(seventh_request_end - seventh_request_begin)+
(eighth_request_end - eighth_request_begin)+
(ninth_request_end - ninth_request_begin)+
(tenth_request_end - tenth_request_begin)+
(eleventh_request_end - eleventh_request_begin))
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
