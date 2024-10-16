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

def give_change(amount, coins):
    ans = []
    for coin in coins:
        if coin <= amount:
            n = amount//coin
            ans+=[coin]*n
            amount-= coin*n
    return ans

def safe_squares_rooks(n,rooks):
    board = [[0]*n]*n
    if not rooks:
        return n*n
    for rook in rooks:
        board[rook[0]]=[1]*n
        for i in range(n):
            board[i][rook[1]] = 1
    return sum([board[i].count(0) for i in range(n)])

def words_with_given_shape(words, shape):
    # shape: if word[i] comes later than words[i+1] then shape[i] = -1
    # shape: if word[i] same as words[i+1] then shape[i] = 0
    # shape: if word[i] comes earlier than words[i+1] then shape[i] = 1
    ans = []
    for word in words:
        if len(word) != len(shape)+1:
            continue
        for i in range(len(shape)):
            if (shape[i] == 1 and word[i] >= word[i+1]) or (shape[i] == -1 and word[i] <= word[i+1]) or (shape[i] == 0 and word[i] != word[i+1]):
                break
        else:
            ans.append(word)
    return ans

def is_left_handed(pips):
    # all possible correct answers when only looking at the 1,2,3 side
    pos = [(1,2,3), (2,3,1), (3,1,2)]
    switches = 0
    check = pips
    if pips[0] not in [1,2,3]:
        check[0] = (7-pips[0])
        switches+=1
    if pips[1] not in [1,2,3]:
        check[1] =(7-pips[1])
        switches+=1
    if pips[2] not in [1,2,3]:
        check[2] = (7-pips[2])
        switches+=1
    check = tuple(check)
    if switches % 2 == 1:
        return check not in pos
    return check in pos




def winning_card(cards, trump=None):

    # all this is that it converts the number in words to number in integers
    rank_order = {
        'ace': 14, 'king': 13, 'queen': 12, 'jack': 11,
        'ten': 10, 'nine': 9, 'eight': 8, 'seven': 7,
        'six': 6, 'five': 5, 'four': 4, 'three': 3, 'two': 2
    }


    leading_suit = cards[0][1]
    trump_cards = [card for card in cards if card[1] == trump]
    if trump_cards:
        return max(trump_cards, key=lambda x: rank_order[x[0]])
    leading_suit_cards = [card for card in cards if card[1] == leading_suit]
    return max(leading_suit_cards, key=lambda x: rank_order[x[0]])

def knight_jump(knight, start, end):
    d = {}
    k = len(knight)
    for i in range(k):
        if knight[i] not in d:
            d[knight[i]] = 1
        else:
            d[knight[i]]+=1
    for i in range(k):
        diff = abs(start[i]-end[i])
        if diff in d and d[diff] != 0:
            d[diff] -= 1
        else:
            return False
    return True



def seven_zero(n):
    # def seven_zero_generator():
    #     d = 1
    #     while True:
    #         for k in range(1, d + 1):
    #             number = int('7' * k + '0' * (d - k))
    #             yield number
    #         d += 1
    # for num in seven_zero_generator():
    #     if num % n == 0:
    #         return num
    d = 1
    output = 7
    while output % n != 0:
        output = int('7'*d)
        if n % 2 == 0 or n % 5 == 0:
            for k in range(1, d+1):
                output = int('7'*k + '0'*(d-k))
                if output % n == 0:
                    return output
        d+=1
    return output

def can_balance(items):
    for i in range(len(items)):
        left = items[:i]
        right = items[i+1:]
        left_torques = [(i-j)*x for j,x in enumerate(left)]
        right_torques = [(j+1)*x for j,x in enumerate(right)]
        if sum(left_torques) == sum(right_torques):
            return i
    return -1

def josephus(n, k):
    people = list(range(1,n+1))
    ans = []
    index = 0
    while people:
        index = (index+k-1)%len(people)
        ans.append(people.pop(index))
    return ans

def group_and_skip(n, out, ins):
    ans = []
    while n != 0:
        left_over = n%out
        ans.append(left_over)
        n-= left_over
        n = n // out * ins
    return ans

def pyramid_blocks(n, m, h):
    return n*m*h + (n+m)*((h*(h-1))//2) + (h*(h-1)*(2*h-1))//6

def count_growlers(animals):
    val = {'dog':1, 'god':1, 'cat':-1, 'tac':-1}
    growls = 0
    for i in range(len(animals)):
        watching = []
        if animals[i] == 'cat' or animals[i] == 'dog':
            watching = animals[:i]
        else:
            watching = animals[i+1:]
        if sum([val[animal] for animal in watching]) > 0:
            growls+=1
        
    return growls

def bulgarian_solitaire(piles, k):
    target = sorted(list(range(1,k+1)))
    moves = 0
    while target != sorted(piles):
        new_pile = len(piles)
        piles = [pile-1 for pile in piles if pile > 1]
        piles.append(new_pile)
        moves+=1
    return moves
    
def scylla_or_charybdis(moves, n):
    # Ill put a simpler solution when I find one
    def execute_moves(k):
        position = 0
        steps = 0
        for i in range(k - 1, len(moves), k):
            steps += 1
            if moves[i] == '+':
                position += 1
            else:
                position -= 1
            if abs(position) == n:
                return steps
        return float('inf')

    min_steps = float('inf')
    best_k = -1

    for k in range(1, len(moves) + 1):
        steps = execute_moves(k)
        if steps < min_steps:
            min_steps = steps
            best_k = k
        elif steps == min_steps and k < best_k:
            best_k = k

    return best_k if best_k != -1 else -1
