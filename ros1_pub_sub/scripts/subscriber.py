#!/usr/bin/env python
import rospy

from std_msgs.msg import String


class Subscriber:

    def __init__(self):
        self.topic = "talker"
        self.subscriber = rospy.Subscriber(self.topic, String, self.callback)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)


def main(args=None):
    rospy.init_node('subscriber', anonymous=True)
    minimal_subscriber = Subscriber()
    rospy.spin()


if __name__ == '__main__':
    main()