"""
This code will connect to a Cisco IOS router (replace the IP address and credentials with your own), send the "show run" command, and print the output to the console. You can modify this code as needed to perform other tasks or connect to different types of network devices.
"""

import netmiko

# Define router details
router = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password'
}

# Connect to the router
net_connect = netmiko.ConnectHandler(**router)

# Send command to the router
output = net_connect.send_command('show run')

# Print output
print(output)

# Disconnect from the router
net_connect.disconnect()