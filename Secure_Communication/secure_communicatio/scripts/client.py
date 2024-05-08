#!/usr/bin/env python3
import rospy
from secure_communicatio.srv import *
import random
import string
import time

def client_one():
    rospy.init_node('client_node')
    rospy.wait_for_service('Secret_Data')

    try:
        proxy = rospy.ServiceProxy('Secret_Data', encrypt)
        request = encryptRequest()

        original_data = generate_random_data(10)  # Change 10 to the desired length of your data
        key = generate_random_key()

        request.encrypted = XOR_encryption(original_data, key)
        request.key = key

        response = proxy(request)

        print("\nOriginal data sent:", original_data)
        print("Randomly generated key:", key)
        print("--------------------------------------------------")
        time.sleep(1.5)
        print("Received decrypted data:", response.decrypted,"\n")

    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def generate_random_data(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_random_key():
    return random.randint(0, 255)  # Assuming your key is an integer between 0 and 255

def XOR_encryption(original_data, key):
    encrypted_data = [ord(char) ^ key for char in original_data]
    return ''.join([chr(value) for value in encrypted_data])

if __name__ == "__main__":
    client_one()
