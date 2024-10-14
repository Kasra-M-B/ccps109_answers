def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

def is_ascending(items):
    for i in range(1,len(items)):
        if items[i-1] >= items[i]:
            return False
    return True

def riffle(items, out=True):
    # farso shuffle
    n = len(items)
    first_half = items[:n//2]
    second_half = items[n//2:]
    result = []
    for i in range(n//2):
        if out:
            result.append(first_half[i])
            result.append(second_half[i])
        else:
            result.append(second_half[i])
            result.append(first_half[i])
    return result

def only_odd_digits(n):
    for c in str(n):
        if c not in "13579":
            return False
    return True

def is_cyclops(n):
    if n < 0:
        return False
    if n == 0:
        return True
    # without converting to a string, using base 10
    digit_count = 0
    num = n
    while num > 0:
        digit_count += 1
        num //= 10
    if digit_count % 2 == 0:
        return False
    middle_index = digit_count // 2
    for i in range(digit_count):
        digit = n % 10
        if i == middle_index:
            if digit != 0:
                return False
        else:
            if digit == 0:
                return False
        n //= 10
    return True

def domino_cycle(tiles):
    if not tiles:
        return True
    for i in range(1, len(tiles)):
        if tiles[i-1][1] != tiles[i][0]:
            return False
    return tiles[-1][1] == tiles[0][0]

def colour_trio(colours):
    pass