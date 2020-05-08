#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if roman_string and len(roman_string):
        numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        rom = roman_string
        l = len(rom)
        for i in range(l):
            if numbers.get(rom[i], 0) == 0:
                return 0
            if i != l - 1 and (numbers[rom[i + 1]] > numbers[rom[i]]):
                total -= numbers[rom[i]]
            else:
                total += numbers[rom[i]]
    return total
