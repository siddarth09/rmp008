import rospy
from rospy.timer import Rate
from std_msgs.msg import String

def pub():
    rospy.init_node('mom')
    word=String()
    pub=rospy.Publisher('clean',String,queue_size=10)
    rate=rospy.Rate(1)
    mom_msgs=['siddarth','clean_your_room','or i will kill you ']
    while not rospy.is_shutdown():
        for i in range(len(mom_msgs)):
            word.data=mom_msgs[i]
            pub.publish(word)
            rospy.loginfo(word.data)
        rate.sleep()

if __name__=="__main__":
    try:
        pub()
    except rospy.ROSInterruptException:
        print("SHUTDOWN")

