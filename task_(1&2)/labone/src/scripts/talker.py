#!/usr/bin/env python3

#################################### Start Of Libraries ####################################
import rospy
from std_msgs.msg import Int32
from random import randint
#################################### End Of Libraries ####################################

#################################### Start Of Functions ####################################
def Talker():
    pub = rospy.Publisher('Chatter', Int32, queue_size=10)      # topic name
    rospy.init_node('pub_node', anonymous=True)                 # node name
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # generating and encrypting random number
        random_num = randint(1, 100)
        encrypted_num = random_num ** 2 + 10

        # publishing message
        rospy.loginfo("Number: %s, Encrypted: %s" % (random_num, encrypted_num)) 
        pub.publish(encrypted_num)
        rate.sleep()
#################################### End Of Functions ####################################
        
#################################### Start Of Main ####################################
if __name__ == '__main__':
    try:
        Talker()
    except rospy.ROSInterruptException:
        pass
#################################### End Of Main ####################################