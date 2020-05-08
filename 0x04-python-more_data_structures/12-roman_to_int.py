#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return 0
    else:
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
        total = 0
        for i in range(l):
            if numbers.get(rom[i], 0) == 0:
                return 0
            if i != l - 1 and (numbers[rom[i + 1]] > numbers[rom[i]]):
                total -= numbers[rom[i]]
            else:
                total += numbers[rom[i]]
        return total
