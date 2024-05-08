#!/usr/bin/env python3
recieved_temp = 0
temp_error = False
recieved_pre = 0.0
pre_error = False
recieved_hum = 0.0
hum_error = False
#################################### Start Of Libraries ####################################
import rospy
from weather_monitoring.msg import SensorReading
from weather_monitoring.srv import *
#################################### End Of Libraries ####################################

#################################### Start Of Functions ####################################
def aggregator():
    rospy.init_node('aggregator_node', anonymous=True) 

    rospy.Subscriber('temperature_data', SensorReading, temp_callback) 
    rospy.Subscriber('pressure_data', SensorReading, pre_callback)
    rospy.Subscriber('humidity_data', SensorReading, hum_callback)   

    rospy.wait_for_service('Monitoring_Service')

    while not rospy.is_shutdown():
        try:
            proxy = rospy.ServiceProxy('Monitoring_Service', monitoring)
            request = monitoringRequest()

            request.temperature = recieved_temp
            request.tempState = temp_error
            request.pressure = recieved_pre
            request.preState = pre_error
            request.humidity = recieved_hum
            request.humState = hum_error

            response = proxy(request)

            print("Remote Station Says:", response.result_message, "with system efficiency:", response.efficiency)
            print("--------------------------------------------------")
        except rospy.ServiceException as e:
            print("Service call failed: %s" % e)

        rospy.sleep(3)

def temp_callback(data):
    global recieved_temp
    global temp_error
    recieved_temp = int(data.value)
    temp_error = data.error
    # print("Received Temperature: %.0f and the error is: %s" % (recieved_temp, temp_error))


def pre_callback(data):
    global recieved_pre
    global pre_error
    recieved_pre = data.value
    pre_error = data.error
    # print("Received Pressure: %.2f and the error is: %s" % (recieved_pre, pre_error))

def hum_callback(data):
    global recieved_hum
    global hum_error
    recieved_hum = data.value
    hum_error = data.error
    # print("Received Humidity: %.2f and the error is: %s" % (recieved_hum, hum_error))
    # print("--------------------------------------------------")
#################################### End Of Functions ####################################

#################################### Start Of Main ####################################
if __name__ == '__main__':
    try:
        aggregator()
    except rospy.ROSInterruptException:
        pass
#################################### End Of Main ####################################
