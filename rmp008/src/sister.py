import rospy
from std_msgs.msg import String

def callback_mom(msg):
    print(msg.data)

def sub():
    rospy.init_node('sister')
    rospy.Subscriber('idiot_do',String,callback_mom)
    rospy.spin()
if __name__=="__main__":
    sub()