#!/usr/bin/env python3
#################################### Start Of Libraries ####################################
import rospy
from std_msgs.msg import Int32
#################################### End Of Libraries ####################################

#################################### Start Of Functions + Classes ####################################
class NodeSubscriber:
    def __init__(self):
        rospy.init_node('Node_2', anonymous=True)       # node name
        self.sub = rospy.Subscriber('encrypted_data', Int32, self.callback)

    def callback(self, data):
        encrypted_num = data.data
        decrypted_num = (encrypted_num - 10) ** 0.5
        rospy.loginfo("Decrypted number: %s", decrypted_num)
        self.publish_decrypted_number(decrypted_num)

    def publish_decrypted_number(self, decrypted_num):
        rospy.loginfo("Publishing decrypted number: %s\n", decrypted_num)
        pub = rospy.Publisher('decrypted_data', Int32, queue_size=10)
        pub.publish(int(decrypted_num))  # Convert to integer before publishing
#################################### End Of Functions + Classes ####################################
        
#################################### Start Of Main ####################################
if __name__ == '__main__':
    try:
        Node_2 = NodeSubscriber()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
#################################### End Of Main ####################################