from typing import Tuple, List
import time
from itertools import product

rules = "RULES: 5-10 words\n" \
        "Upper letters, lower letters and numbers\n" \
        "NO Special symbols"

def brute_force(password: str) -> bool:
    upper = "ABCDEFGHIJKLMNOPRSTQUWXYZ"
    lower = "abcdefghijklmnoprstquwxyz"
    nums = "0123456789"

    tab = lower + nums + upper

    for passwd in product(tab, repeat=len(password)):
        if "".join(passwd) == password:
            print("".join(passwd))
            return True

    return True

if __name__ == '__main__':
    print(rules)
    password = str(input())
    start = time.clock()
    brute_force(password)
    end = time.clock()
    print("Time: {:.10f}".format(end - start))