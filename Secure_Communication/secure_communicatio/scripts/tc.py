#!/usr/bin/env python3
import rospy
from secure_communicatio.srv import *

def custom_xor(data, key):
    encrypted_data = []

    for char in data:
        # Step 1: Character Representation
        char_value = ord(char)

        # Step 2: XOR Operation
        encrypted_value = char_value ^ key

        # Step 3: Resulting Encrypted Value
        encrypted_data.append(encrypted_value)

    # Step 4: Concatenation
    ciphertext = ''.join([chr(value) for value in encrypted_data])

    return ciphertext

def clien_one(data, key):
    rospy.init_node('client_node')
    rospy.wait_for_service('Secret_Data')
    
    try:
        encrypt_service = rospy.ServiceProxy('Secret_Data', encrypt)
        request = encryptRequest()
        request.encrypted = custom_xor(data, key)
        request.key = key

        response = encrypt_service(request)

        print("Received decrypted data:", response.decrypted)

    except rospy.ServiceException as e:
        print(f"Service call failed: {e}")


if __name__ == "__main__":
    data = input("Enter the data to be sent: ")
    key = int(input("Enter the encryption key: "))
    clien_one(data, key)
