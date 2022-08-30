import napalm
import sys
import os

import argparse
from napalm import get_network_driver
from getpass import getpass
import json
from netmiko import Netmiko
from pprint import pprint as pp
import json


parser = argparse.ArgumentParser(prog= 'rahat.py', usage='%(prog)s device os username',description="login credentials & device type")
parser.add_argument('--device', help="hostname or IP",type=str,default=None  )
parser.add_argument('--device_type', help="device type", type=str, default=None)
parser.add_argument('--username', help="login name", type=str, default=None)

args = parser.parse_args()

host = args.device
driver = args.device_type
user = args.username

device_password = getpass(" SSH key password: ")
priv = getpass(" priviledge password: ")

optional_args = {'secret': priv}
device_driver = get_network_driver(driver)

commands2 = ['show ipv6 route']
commands1 = ['show ip route']
commands3 = ['show route table inet.0']
commands4 = ['show route table inet6.0']
 

with device_driver(hostname=host, username=user, password= device_password, optional_args=optional_args) as dev:
    dev.open()
    if driver == 'ios' :
        cmd1 = dev.cli(commands1)
        cmd2 = dev.cli(commands2)
    elif driver == 'junos' :
        cmd1 = dev.cli(commands3)
        cmd2 = dev.cli(commands4)
        
    
   
#    info = dev. get_facts()
#    info2 = dev.get_network_instances()
#    info4= dev.get_bgp_config()
#    info5= dev.get_bgp_neighbors()
#    info6= dev.get_bgp_neighbors_detail()
#    info_json = json.dumps(info, sort_keys=True, indent=4)
#    info2_json = json.dumps(info2, sort_keys=True, indent=4)
    info3_json = json.dumps(cmd1, sort_keys=True, indent=4)
    info4_json = json.dumps(cmd2, sort_keys=True, indent=4)
#    info5_json = json5.dumbs(cmd, sort_keys=True, indent=4)
#    info6_json = json6.dumbs(cmd, sort_keys=True, indent=4)
    


#print(info_json)  

#print('bgp config' + '#######################################################')
#print(info4) 

#print('bgp neighbou' + '#######################################################')
#print(info5) 

#print('bgp neighbou details' + '#######################################################')
#print(info6)
#print(info)
#pp(type(cmd))
print(info3_json)
print("#############################################################################")
print(info4_json)
