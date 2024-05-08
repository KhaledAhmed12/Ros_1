#!/usr/bin/env python3
#################################### Start Of Libraries ####################################
import rospy
import random
from std_msgs.msg import Int32
#################################### End Of Libraries ####################################

#################################### Start Of Functions + Classes ####################################
class NodePublisher:
    def __init__(self):
        rospy.init_node('Node_1', anonymous=True)
        self.pub = rospy.Publisher('encrypted_data', Int32, queue_size=10)  # Change topic name to 'encrypted_number'
        self.sub = rospy.Subscriber('decrypted_data', Int32, self.callback)
        self.rate = rospy.Rate(0.5)  # adjust the rate as needed
        self.original_num = 0
        self.flag = True  # Start with the flag as True

        while not rospy.is_shutdown():
            self.publish_encrypted_number()
            self.rate.sleep()

    def publish_encrypted_number(self):
        if self.flag:
            self.original_num = random.randint(1, 100)
            encrypted_num = self.original_num ** 2 + 10
            rospy.loginfo("Publishing encrypted number: %s", encrypted_num)
            self.pub.publish(encrypted_num)
            #self.flag = False  # Set flag to False after publishing

    def callback(self, data):
        # Node 2 has sent back the decrypted number
        decrypted_num = data.data
        rospy.loginfo("Received decrypted number: %s", decrypted_num)

        if self.original_num != 0 and decrypted_num == self.original_num:
            rospy.loginfo("Decrypted number matches the original. Sending the next number....\n")
            self.flag = True
        else:
            rospy.logwarn("Decrypted number does not match the original. Setting flag to False.\n")
            self.flag = False
#################################### End Of Functions + Classes ####################################

#################################### Start Of Main ####################################
if __name__ == '__main__':
    try:
        Node_1 = NodePublisher()
    except rospy.ROSInterruptException:
        pass
#################################### End Of Main ####################################
