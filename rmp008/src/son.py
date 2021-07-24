import rospy
from rospy.topics import Publisher
from std_msgs.msg import String

def callback_mom(msg):
    print(msg.data)

def pub():
    
    msg_passer=rospy.Publisher('idiot_do',String,queue_size=10)
    msg="HOPE YOUR HEARD WHAT MOM TOLD"
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        msg_passer.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()

if __name__=="__main__":
    rospy.init_node('son')
    rospy.Subscriber('clean',String,callback_mom)
    try:
        pub()
    except rospy.ROSInterruptException:
        print("SHUTDOWN")
    rospy.spin()
