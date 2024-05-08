#!/usr/bin/env python3
#################################### Start Of Libraries ####################################
import rospy
from weather_monitoring.msg import SensorReading
import random
#################################### End Of Libraries ####################################

#################################### Start Of Functions ####################################
def temperature_node():
    rospy.init_node('temperature_node', anonymous=True)
    pub = rospy.Publisher('temperature_data', SensorReading, queue_size=10)

    while not rospy.is_shutdown():
        temperature_value = random.randint(0, 120)

        error_status = temperature_value > 100 or temperature_value < 10  # Set to True if an error is detected

        rospy.loginfo("Temperature Value: %s, Error Status: %s", temperature_value, str(error_status))

        data = SensorReading(value=temperature_value, error=error_status)

        pub.publish(data)

        rospy.sleep(5)
#################################### End Of Functions ####################################
        
#################################### Start Of Main ####################################
if __name__ == '__main__':
    try:
        temperature_node()
    except rospy.ROSSerializationException:
        pass
#################################### End Of Main ####################################
