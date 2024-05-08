#!/usr/bin/env python3
#################################### Start Of Libraries ####################################
import rospy
from weather_monitoring.msg import SensorReading
import random
#################################### End Of Libraries ####################################

#################################### Start Of Functions ####################################
def pressure_node():
    rospy.init_node('pressure_node', anonymous=True)
    pub = rospy.Publisher('pressure_data', SensorReading, queue_size=10)

    while not rospy.is_shutdown():
        pressure_value = random.uniform(0.85, 1.3)

        error_status = pressure_value > 1.2 or pressure_value < 0.95  # Set to True if an error is detected

        rospy.loginfo("Pressure Value: %0.2f, Error Status: %s", pressure_value, str(error_status))

        data = SensorReading(value=pressure_value, error=error_status)

        pub.publish(data)

        rospy.sleep(5)
#################################### End Of Functions ####################################
        
#################################### Start Of Main ####################################
if __name__ == '__main__':
    try:
        pressure_node()
    except rospy.ROSSerializationException:
        pass
#################################### End Of Main ####################################
