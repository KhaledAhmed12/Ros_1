#!/usr/bin/env python3

#################################### Start Of Libraries ####################################
import rospy
from std_msgs.msg import Int32
import math
#################################### End Of Libraries ####################################

#################################### Start Of Functions ####################################
def listener():
    rospy.Subscriber('Chatter', Int32, callback)        # call back is like to ISR in embedded 
    rospy.init_node('subscriber_node', anonymous=True)  # node name
    rospy.spin()                                        # it's important to keep listening not only one time

def callback(data):
    # Recieving and dencrypting the number
    encrypted_num = data.data
    decrypted_num = int(math.sqrt(encrypted_num - 10))
    rospy.loginfo("I Received: %s, Decrypted: %s" % (encrypted_num, decrypted_num))
#################################### End Of Functions ####################################

#################################### Start Of Main ####################################
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
#################################### End Of Main ####################################