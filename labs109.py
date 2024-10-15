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
    prev_row = colours

    while len(prev_row) > 1:
        curr_row = []
        for i in range(len(prev_row) - 1):
            if prev_row[i] == prev_row[i + 1]:
                curr_row.append(prev_row[i])
            else:
                # Determine the missing color
                if 'r' not in (prev_row[i], prev_row[i + 1]):
                    curr_row.append('r')
                elif 'b' not in (prev_row[i], prev_row[i + 1]):
                    curr_row.append('b')
                else:
                    curr_row.append('y')
        prev_row = curr_row  # Move to the next row

    return prev_row[0]

def count_dominators(items):
    count = 0
    #assume some arbitary large negative number
    max_so_far = float('-inf') #can also use some really big negative number like -1e9

    #reverse the list
    items = items[::-1]
    # Traverse the list from right to left
    for item in items:
        if item > max_so_far:
            count += 1
            max_so_far = item  # Update the max so far

    return count

def extract_increasing(digits):
    ans = []
    prev = -1
    current = 0
    for d in digits:
        current= 10 * current + int(d)
        if current > prev:
            ans.append(current)
            prev = current
            current = 0
    return ans

def words_with_letters(words, letters):
    # return the list words that contan letters as a subsequence
    ans = []
    for word in words:
        i = 0
        for letter in letters:
            # you can do it without .find(), but its gonna be slower since
            # .find() is implemented in C
            i = word.find(letter, i)
            if i == -1:
                break
            i += 1
        else:
            ans.append(word)
    return ans

def taxi_zum_zum(moves):
    #facing north initialy
    location = [0,0]
    possibilies = [(0,1), (1,0), (0,-1), (-1,0)]
    index = 0
    for move in moves:
        if move == 'L':
            index -=1
            continue
        elif move == 'R':
            index +=1
            continue
        else:
            direction = possibilies[index%4]
            location[0] += direction[0]
            location[1] +=  direction[1]
    return tuple(location)

