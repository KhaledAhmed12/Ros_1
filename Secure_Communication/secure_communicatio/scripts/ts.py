#!/usr/bin/env python3
import rospy
from secure_communicatio.srv import *
import random

def custom_encrypt(data, key):
    encrypted_data = "".join([chr(ord(char) ^ key) for char in data])
    return encrypted_data

def encrypt_data(request):
    original_data = request.encrypted
    key = request.key

    print("Received encrypted data:", original_data, "with key:", key)

    encrypted_data = custom_encrypt(original_data, key)

    print("Sending back encrypted data:", encrypted_data)
    
    return encryptResponse(encrypted_data)

def public_host():
    rospy.init_node('server_node')
    service = rospy.Service('Secret_Data', encrypt, encrypt_data)
    print("I'm Ready...")
    rospy.spin()

if __name__ == "__main__":
    public_host()
