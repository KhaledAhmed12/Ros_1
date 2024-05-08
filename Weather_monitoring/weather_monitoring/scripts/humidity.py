#!/usr/bin/env python3
#################################### Start Of Libraries ####################################
import rospy
from weather_monitoring.msg import SensorReading
import random
#################################### End Of Libraries ####################################

#################################### Start Of Functions ####################################
def humidity_node():
    rospy.init_node('humidity_node', anonymous=True)
    pub = rospy.Publisher('humidity_data', SensorReading, queue_size=10)

    while not rospy.is_shutdown():
        humidity_value = random.uniform(0.60, 1.05)

        error_status = humidity_value > 0.95 or humidity_value < 0.7  # Set to True if an error is detected

        rospy.loginfo("Humidity Value: %0.2f, Error Status: %s", humidity_value, str(error_status))

        data = SensorReading(value=humidity_value, error=error_status)

        pub.publish(data)

        rospy.sleep(5)
#################################### End Of Functions ####################################
        
#################################### Start Of Main ####################################
if __name__ == '__main__':
    try:
        humidity_node()
    except rospy.ROSSerializationException:
        pass
#################################### End Of Main ####################################
