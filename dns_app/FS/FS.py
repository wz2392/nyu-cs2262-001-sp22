#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request
from socket import *
import json

app = Flask(__name__)

def get_fibonacci(n):
    if n < 0:
        return 'MUST BE POSITIVE NUM'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return get_fibonacci(n - 1) + get_fibonacci(n - 2)
    
@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')
    if not number:
        return 400
    
    else:
        fibo_num = get_fibonacci(int(number))
        return 'sequence {} fibonacci {}'.format(number, fibo_num), 200

@app.route('/register', methods=['PUT'])
def register():
    info = request.get_json() 
    hostname = info.get('hostname')
    ip = info.get('ip')
    as_ip = info.get('as_ip')
    as_port = int(info.get('as_port'))
    
    if hostname and ip and as_ip and as_port:
        
        fs_socket = socket(AF_INET, SOCK_DGRAM) 
        dns_request = {'TYPE': 'A','NAME': hostname,'VALUE': ip,'TTL': '10'}
        message = json.dumps(dns_request)
        
        fs_socket.sendto(message.encode(), (as_ip, as_port))
        response_message, server_address = fs_socket.recvfrom(2048)
       
        fs_socket.close()
        
        if response_message.decode() == 'Success 201':
            return 201
        else:
            return 500

    else:
        return 400

app.run(host='0.0.0.0',
        port=9090,
        debug=True)


# In[ ]:




