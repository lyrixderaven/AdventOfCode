from inputs import NINTH

inputstring = NINTH.inputstring

total_len = 0
enct_len = 0
for str in inputstring:
    code_length = len(str[1]) + 2
    mem_length = (len(str[0]))
    enc_len = len(str[2]) + 6

    total_len += code_length - mem_length
    enct_len += enc_len - code_length

print total_len, enct_len
