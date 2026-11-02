from setuptools import setup

package_name = 'square_tracer'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Harshit',
    maintainer_email='harshitbanga26@gmail.com',
    description='A ROS 2 node that makes turtlesim trace a square',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'square_tracer = square_tracer.square_tracer:main',
        ],
    },
)

