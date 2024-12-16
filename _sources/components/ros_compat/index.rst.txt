ROS Compatibility Layer Documentation
===================================

Welcome to the ROS Compatibility Layer documentation. This package provides a unified
interface for writing nodes that work with both ROS1 (rospy) and ROS2 (rclpy).

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api
   examples

Installation
-----------

To install the package with ROS1 support::

    pip install ros-compat[ros1]

To install with ROS2 support::

    pip install ros-compat[ros2]

Quick Start
----------

Here's a simple example of using the compatibility layer::

    from ros_compat import ROSNode
    from std_msgs.msg import String

    class MyNode(ROSNode):
        def __init__(self):
            super().__init__('my_node')
            self.pub = self.create_publisher('topic', String)
            self.create_subscription('input', String, self.callback)

        def callback(self, msg):
            self.logger.info(f"Received: {msg.data}")

    if __name__ == '__main__':
        node = MyNode()
        node.spin()

API Reference
------------

.. automodule:: ros_compat.node
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: ros_compat.time
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: ros_compat.logging
   :members:
   :undoc-members:
   :show-inheritance:
