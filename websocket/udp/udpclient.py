# -*- coding:utf-8 -*-
 import socket

 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 for data in[b 'Hello', b['World']]:
     