def is_power_of(number, base):
    print("is_power_of called with number " + str(number))
    if number < base:
        print("returning True")
        return number == 1
    result = number // base
    print("returning " + str(result) + " for power of " + str(number))
    return is_power_of(result, base)


print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False