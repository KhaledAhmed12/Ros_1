#!/usr/bin/env python3
import rospy
from secure_communicatio.srv import *
import time

def Public_Host():
    rospy.init_node('server_node')
    
    # Create a service named 'Secret_Data' with the 'encrypt' callback function
    rospy.Service('Secret_Data', encrypt, callback)

    print("I'm Ready...")
    rospy.spin()

def callback(data):
    print("Received encrypted data:",data.encrypted, "with key:", data.key)
    Decrypted_Data = XOR_decryption(data.encrypted, data.key)
    time.sleep(1.5)
    print("Sending back decrypted data:", Decrypted_Data)
    print("--------------------------------------------------")

    response = encryptResponse()
    response.decrypted = Decrypted_Data
    return response

def XOR_decryption(data, key):
    decryption_data = "".join([chr(ord(char) ^ key) for char in data])
    return decryption_data

if __name__ == "__main__":
    Public_Host()
