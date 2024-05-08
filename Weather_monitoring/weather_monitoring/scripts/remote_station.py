#!/usr/bin/env python3
#################################### Start Of Libraries ####################################
import rospy
from weather_monitoring.msg import SensorReading
from weather_monitoring.srv import *
#################################### End Of Libraries ####################################

#################################### Strat Of Functions ####################################
def remote_station():

    rospy.init_node('remote_station_node')

    rospy.Service('Monitoring_Service', monitoring, callback)
    rospy.spin()

def callback(data):
    if not data.tempState:
            rospy.loginfo("Temperature Value: %s °C", data.temperature)
    else:
        rospy.logwarn("Temperature Sensor reading is out of range! Value: %s °C", data.temperature)

    if not data.preState:
            rospy.loginfo("Pressure Value: %0.2f atm", data.pressure)
    else:
        rospy.logwarn("Pressure Sensor reading is out of range! Value: %0.2f atm", data.pressure)

    if not data.humState:
            rospy.loginfo("Humidity Value: %0.2f", data.humidity)
            print("--------------------------------------------------")
    else:
        rospy.logwarn("Humidity Sensor reading is out of range! Value: %0.2f", data.humidity)
        print("--------------------------------------------------")

    response = monitoringResponse()
    rospy.sleep(2)
    response.efficiency = (1- ((data.tempState + data.preState + data.humState) / 3)) * 100
    response.result_message = "All Is Recieved"
    return response
#################################### End Of Functions ####################################

#################################### Start Of Main ####################################
if __name__ == '__main__':
    try:
        remote_station()
    except rospy.ROSInterruptException:
        pass
#################################### End Of Main ####################################