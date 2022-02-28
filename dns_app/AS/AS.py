#!/usr/bin/env python
# coding: utf-8

# In[1]:


from socket import *
import json

server_port = 53533

as_socket = socket(AF_INET, SOCK_DGRAM)
as_socket.bind(('', server_port))
reg_mappings = {}
print('Ready to listen')

while True:
    message, client_address = as_socket.recvfrom(2048)
    decoded_message = message.decode()
    print('Recieve the message: ' + decoded_message)
    
    if 'VALUE' in decoded_message:
        print('Registrating......')
        info = json.loads(decoded_message)
        name = info['NAME']
        value = info['VALUE']
        reg_mapping[name] = value
        print('Finish Registration')
        as_socket.sendto("Success 201".encode(), client_address)
    else: 
        print('DNS Queue Request')
        info = json.loads(decoded_message)
        name = info['NAME']
        if name in reg_mappings:
            response = "TYPE=A\nNAME={}\nVALUE={}\nTTL=10".format(name, reg_mappings[name])
            as_socket.sendto(response.encode(), client_address)
    


# In[ ]:




