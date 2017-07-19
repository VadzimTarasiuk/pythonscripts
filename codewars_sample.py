def sum_two_smallest_numbers(numbers):
    """
    return sorted(numbers)[0] + sorted(numbers)[1]
    Tests seems to be writen bad enough to this solve to pass.
    So I made the right one
    """
    newlist = []
    for each in numbers:
        if each > 0:
            newlist.append(each)
    return sorted(newlist)[0] + sorted(newlist)[1]
print(sum_two_smallest_numbers([24, 34, -244, 12, -4, 76, -21]))