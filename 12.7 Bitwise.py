"""
&   	AND	Sets each bit to 1 if both bits are 1
|	    OR	Sets each bit to 1 if one of two bits is 1
^	    XOR	Sets each bit to 1 if only one of two bits is 1
~	    NOT	Inverts all the bits
<<  	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	    Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""

## Important Note:
"""
x << n → multiplies x by 2ⁿ

x >> n → divides x by 2ⁿ (floor division)

"""
print(5 & 3)    # 1  ->  0101 & 0011 = 0001
print(5 | 3)    # 7  ->  0101 | 0011 = 0111
print(5 ^ 3)    # 6  ->  0101 ^ 0011 = 0110
print(~5)       # -6 ->  ~0101   = 1010 (two's complement representation)
print(5 << 1)   # 10 ->  0101 << 1 = 1010
print(5 >> 1)   # 2  ->  0101 >> 1 = 0010