def hamming2(i1, i2):
    s1 = str(bin(i1)[2:])
    s2 = str(bin(i2)[2:])
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

print(hamming2(1, 4))