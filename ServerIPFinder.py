#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from socket import*

serveripaddressfinder_ico = """
#########################################################
#        SERVER IP ADDRES FINDER - GH0ST S0FTWARE       #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""
print serveripaddressfinder_ic
def ServerIPScanner():
	target = raw_input("WEP SITE ADRESI --> ")
	targetIP = gethostbyname(target)
	print "SERVER IP NUMARASI --> ", targetIP
ServerIPScanner()
