def repeat_inside(line):
    """
        first the longest repeating substring
    """
    print("************")
    cache = {}
    MAX_WINDOW = ""
    MAX_WINDOW_AMOUNT = 0
    length = len(line)

    for i in range(len(line)-1, 0, -1):
        window_length = length // i
        for j in range(0, window_length):
            window = line[j:window_length]
            if cache.get(window):
                continue
            # else
            print(f"\nwindow: {window}")
            print(f"cache: {cache}")
            amount = line.count(window)
            for k in range(amount, 1, -1):
                temp_substring = window * k
                if line.count(temp_substring):
                    print(f"temp_substring: {temp_substring} {line.count(temp_substring)}")
                    amount = temp_substring.count(window)
                    break

            if amount > 1:
                cache[window] = amount
                if len(amount * window) > len(MAX_WINDOW_AMOUNT * MAX_WINDOW):
                    MAX_WINDOW_AMOUNT = amount
                    MAX_WINDOW = window

    print(MAX_WINDOW * MAX_WINDOW_AMOUNT)
    return MAX_WINDOW * MAX_WINDOW_AMOUNT


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')
