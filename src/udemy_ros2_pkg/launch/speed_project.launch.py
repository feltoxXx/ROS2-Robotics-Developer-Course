#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="udemy_ros2_pkg",
            executable="rpm_publisher.py",
            name="rpm_pub_node"
        ),
        Node(
            package="udemy_ros2_pkg",
            executable="speed_calculator.py",
            name="speed_pub_node",
            parameters=[
                {
                    "wheel_radius": 0.5
                }
            ]
        ),
        ExecuteProcess(
            cmd=['ros2','topic','list'],
            output="screen"
        )
    ])