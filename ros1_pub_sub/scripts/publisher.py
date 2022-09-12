#!/usr/bin/env python
import rospy

from std_msgs.msg import String


class Publisher:

    def __init__(self):
        self.topic = "talker"
        self.publisher = rospy.Publisher(self.topic, String, queue_size=10)
        timer_period = 0.5  # seconds
        self.timer = rospy.Timer(rospy.Duration(timer_period), self.timer_callback)
        self.i = 0

    def timer_callback(self, event):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        rospy.loginfo('Publishing: "%s"' % msg.data)
        self.publisher.publish(msg)
        self.i += 1


def main(args=None):
    rospy.init_node('publisher', anonymous=True)
    minimal_publisher = Publisher()
    rospy.spin()


if __name__ == '__main__':
    main()