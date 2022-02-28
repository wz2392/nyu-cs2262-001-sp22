#!/usr/bin/env python
# coding: utf-8

# In[1]:


from socket import *
from flask import Flask,request
from urllib.request import urlopen
import json

app = Flask(__name__)


@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = int(request.args.get('as_port'))

    if not hostname or not fs_port or not number or not as_ip or not as_port:
        return 400
    
    user_socket = socket(AF_INET, SOCK_DGRAM)
    host_request = {'TYPE': 'A',
                    'NAME': hostname}
    message = json.dumps(host_request)
    user_socket.sendto(message.encode(), (as_ip, as_port))
   
    response_message, server_address = user_socket.recvfrom(2048)
    info = json.loads(response_message.decode())
    name =info['VALUE']
    user_socket.close()
    response ='http://{}:{}/fibonacci?number={}'.format(name,fs_port,number)
    html = urlopen(response)
    return html.read(), 200

app.run(host='0.0.0.0',
        port=8080,
        debug=True)


# In[ ]:




