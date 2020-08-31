def non_repeat2(line: str) -> str:
    if not line:
        return line

    maxst_len: int = 1
    maxst_ix: int = 0
    curst_len: int = 1
    curst_ix: int = 0

    positions = dict()
    positions[line[0]] = 0

    for ix, char in enumerate(line[1:], 1):
        previous = positions.get(char, -1)
        if previous >= 0:
            curst_len = ix - previous
            if curst_len > maxst_len:
                maxst_len = curst_len
                maxst_ix = previous
            # else:
            #     curst_len = 1
            curst_ix = ix
        # elif maxst_ix <= previous < maxst_ix + maxst_len:
        #     curst_ix = ix
        #     curst_len = 1
        else:
            curst_len += 1
            if curst_ix == maxst_ix:
                maxst_len += 1

        positions[char] = ix

    if maxst_len < curst_len:
        maxst_len = curst_len
        maxst_ix = ix - curst_len + 1
    return line[maxst_ix:maxst_ix + maxst_len]


def non_repeat(line: str) -> str:
    if not line:
        return line

    p: int = 0
    substrings = []
    substrings.append(line[0])

    for ix, c in enumerate(line[1:], 1):
        if c in substrings[-1]:
            p = len(substrings) - 1
            substrings.append(c)
        else:
            substrings.append(substrings[-1] + c)

    maxl = 1
    ix = 0
    for i, s in enumerate(substrings):
        if len(s) > maxl:
            maxl = len(s)
            ix = i
    return substrings[ix]


if __name__ == '__main__':
    assert non_repeat('aaaaa') == 'a', 1
    assert non_repeat('abcd') == 'abcd', 2
    assert non_repeat('abcabc') == 'abc', 3
    assert non_repeat('abcabcd') == 'abcd', 4
    assert non_repeat('abcbca') == 'abc', 5

    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('fghfrtyfgh') == 'ghfrty', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
