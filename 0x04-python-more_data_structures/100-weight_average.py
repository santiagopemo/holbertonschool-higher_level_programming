#!/usr/bin/python3
def weight_average(my_list=[]):
    if isinstance(my_list, list) and len(my_list):
        num = dem = 0
        for mem in my_list:
            num += mem[0] * mem[1]
            dem += mem[1]
        return num / dem
    return 0
