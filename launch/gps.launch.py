import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Assuming you have a config directory within your package with necessary configuration files
    config_dir = os.path.join(get_package_share_directory('articubot_one'), 'config')

    return LaunchDescription([
        # GPS Publisher Node
        Node(
            package='gps_publisher',  # Replace with your GPS package name
            executable='gps_pub_node',  # Replace with the executable provided by your GPS package
            output='screen',
        ),
        # NavSat Transform Node (part of robot_localization)
        Node(
            package='robot_localization',
            executable='navsat_transform_node',
            name='navsat_transform_node',
            output='screen',
            parameters=[os.path.join(config_dir, 'navsat_transform_params.yaml')],
            remappings=[('gps/fix', 'gps_topic'), ('odom', 'odom_topic')],
        ),
        # Additional nodes for localization, mapping, etc.
    ])

