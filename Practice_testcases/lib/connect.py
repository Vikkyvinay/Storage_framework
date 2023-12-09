"""
This module is an API to connect remote linux host and get the response
Author::Vinay
Date::10-06-2023
"""
import paramiko
import time
import sys
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
json_file = r"D:\Practice_testcases\testcases\config_files\host_details.json"

with open(json_file) as file1:
    host_mapping = json.load(file1)

server_ip = host_mapping["test_setup"]["IP"]
username = host_mapping["test_setup"]["Username"]
password = host_mapping["test_setup"]["password"]


def exec_cmd(cmd):
    """
    This function is used to connect remote linux host and execute commands
    :param cmd:
    :param server_ip:
    :param username:
    :param password:
    :return: str
    """
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server_ip, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(cmd)
    out = stdout.read()
    return out.decode()
