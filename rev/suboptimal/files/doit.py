import string

# complex decoding
def complex_decoding(e):
    c = e - 4
    if c < 0x41:
        c += 0x3d
    return c

# complex2 decoding
def complex2_decoding(e):
    c = e - 4
    if c < 0x41:
        c += 0x3d
    return c

# encoded string
s = 'xk|nF{quxzwkgzgwx|quitH'

# decoded string
o = ''

# loop over each character in the encoded string
for e in s:
    # decode the character
    c = complex_decoding(complex2_decoding(ord(e)))

    # append to the decoded string
    o += chr(c)

# done
print(o)
