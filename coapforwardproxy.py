#!/usr/bin/env python

import getopt
import sys
from coapthon.forward_proxy.coap import CoAP
import threading
import daemon

__author__ = 'Giacomo Tanganelli'


class CoAPForwardProxy(CoAP):
    def __init__(self, host, port, use_daemon=0, use_cache=0, dim_len=2,method_arg=0,multicast=False):
        print "PORT : "+str(port)
        if(use_cache):
            print "Using Cache"
            print "Using dimension : "+str(dim_len)
            CoAP.__init__(self, (host, port), cache=True,dim_len=dim_len,method_arg=method_arg,multicast=multicast)
        else:
            CoAP.__init__(self, (host, port), cache=False, multicast=multicast)

        print "CoAP Proxy start on " + host + ":" + str(port)
        try:
            if(use_daemon):
                print "Starting Daemon too"
                threading.Thread(target=daemon.cleanup, args=(self._cacheLayer.cache.cache.cache,)).start()
        except KeyboardInterrupt:
            print "Bye"


def usage():  # pragma: no cover
    print "coapforwardproxy.py -i <ip address> -p <port> -d <use_daemon> -c <use_cache> -l <cache_dim> -m <method>"
    print "Cache Replication Methods = 0:LRU, 1:LFU, 2:RR, 3:LIFO,4:FIFO,5:MFU,6:SLRU"


def main(argv):  # pragma: no cover
    ip = "0.0.0.0"
    port = 5684
    use_daemon = 0
    use_cache = 0
    try:
        opts, args = getopt.getopt(argv, "hi:p:d:c:l:m:", ["ip=", "port=","daemon=", "cache=","len=","method="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--ip"):
            ip = arg
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-d","--daemon"):
            use_daemon = int(arg)
        elif opt in ("-c", "--cache"):
            use_cache = int(arg)
        elif opt in ("-l", "--length"):
            dim_len = int(arg)
        elif opt in ("-m", "--method"):
            method_arg = int(arg)
    server = CoAPForwardProxy(ip, port,use_daemon,use_cache,dim_len,method_arg)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print "Server Shutdown"
        server.close()
        print "Exiting..."


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])