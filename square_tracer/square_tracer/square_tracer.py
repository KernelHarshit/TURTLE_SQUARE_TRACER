
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class SquareTracer(Node):

    def __init__(self):
        super().__init__('square_tracer')

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.movements = ['forward', 'turn'] * 4
        self.index = 0
        self.counter = 0.0

        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )

        self.get_logger().info('Square tracer started')

    def timer_callback(self):

        if self.index >= len(self.movements):

            msg = Twist()
            self.publisher.publish(msg)

            self.timer.cancel()
            self.get_logger().info('Square completed')
            return

        msg = Twist()

        if self.movements[self.index] == 'forward':

            msg.linear.x = 2.0
            duration = 2.0

        else:

            msg.angular.z = 1.57
            duration = 1.0

        self.publisher.publish(msg)

        self.counter += 0.1

        if self.counter >= duration:

            self.counter = 0.0
            self.index += 1


def main(args=None):

    rclpy.init(args=args)

    square_tracer = SquareTracer()

    rclpy.spin(square_tracer)

    square_tracer.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

