#!/usr/bin/env python3

import json

__author__ = "Rafael Correia"
__version__ = "0.0.1"
__license__ = "MIT"

class SysEx:
    def __init__(self, path):
        impl = self.__parse_file(path)
        self.id = impl['id']
        self.device_id = impl['device_id']
        self.model_id = impl['model_id']
        self.command_id = impl['command_id']
        self.addresses = impl['addresses']

    def __parse_file(self, path):
        with open(path) as file:
            data = json.load(file)
        return data

    def __calculate_checksum(self, hex):
        nums = bytes.fromhex(hex)
        checksum = 0
        for byte in nums:
            checksum += byte
        return "%02X" % (128 - checksum % 128)

    def generate_message(self, address_name, data):
        header = ''.join([self.id, self.device_id, self.model_id, self.command_id])
        body = ''.join([self.addresses[address_name]['address'], data])
        checksum = self.__calculate_checksum(body)
        return bytes.fromhex(''.join(["F0", header, body, checksum, "F7"]))