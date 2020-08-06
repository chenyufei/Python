#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
# src = 'fffff7ff03ffffffffffffffffffffffbffffffffffffffb7fffffffffffffffffffffdfffbfffffffffffff0dfcfffeffffffffffeffffeffffffffffffffffffffff07'
src =  'dffffffffffffffffffffffffffffffffffffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'

def get_lose_upgrade_packet(src):
    lose_packet = []
    packet_number = 0
    for index in range(0, len(src), 2):
        for i in range(0, 2):
            value = int(src[index+1-i], 16)
            if value & 0x01 == 0x01:
                pass
            else:
                lose_packet.append(packet_number)
            packet_number = packet_number + 1

            if value & 0x02 == 0x02:
                pass
            else:
                lose_packet.append(packet_number)
            packet_number = packet_number + 1

            if value & 0x04 == 0x04:
                pass
            else:
                lose_packet.append(packet_number)
            packet_number = packet_number + 1

            if value & 0x08 == 0x08:
                pass
            else:
                lose_packet.append(packet_number)
            packet_number = packet_number + 1
    dict = {"004a7700656540013":lose_packet}
    print(dict)


def check_read_write():
    upgrade_file = 'GA60V100R003B005.bin'
    try:
        bExist = os.path.exists(upgrade_file)
        if bExist:
            fd = open(upgrade_file, "rb")
            content = fd.read()
        else:
            return
    except Exception as e:
        print("Error: fail to operator config file"+ e)
        return

    totalpacket = 0
    if content.__len__() % 208 == 0:
        totalpacket = int(content.__len__() / 208)
    else:
        totalpacket = int(content.__len__() / 208) + 1

    for upgrade_times in range(0, 4):
        index = 0
        fd.seek(0)
        while index < totalpacket:
            content = fd.read(208)
            index += 1
            time.sleep(0.3)
        time.sleep(10)



if __name__ == '__main__':
    chen={}
    dd=[]
    chen["11"] = [1,2,3,4,5,6]
    chen["22"] = [3,6,7,8,9,10]
    chen["33"] = [11,16,17,18,19,20]
    for item in chen:
        for value in chen[item]:
            if dd.count(value) == 0:
                dd.append(value)
    print(dd)
    get_lose_upgrade_packet(src)