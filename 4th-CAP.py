from itertools import permutations
def solve_cryptarithmetic():
    for values in permutations(range(10), 8):
        s, e, n, d, m, o, r, y = values
        if s != 0 and m != 0: 
            send = s * 1000 + e * 100 + n * 10 + d
            more = m * 1000 + o * 100 + r * 10 + e
            money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
            if send + more == money:
                return send, more, money

result = solve_cryptarithmetic()
if result:
    send, more, money = result
    print(f"SEND = {send}, MORE = {more}, MONEY ={money}")
else:
    print("No solution found.")
