"""
=	              x = 5	            x = 5	
+=	              x += 3        	x = x + 3	
-=	              x -= 3        	x = x - 3	
*=	              x *= 3        	x = x * 3	
/=	              x /= 3    	    x = x / 3	
%=	              x %= 3    	    x = x % 3	
//=	              x //= 3   	    x = x // 3	
**=	              x **= 3   	    x = x ** 3	
&=	              x &= 3    	    x = x & 3	
|=	              x |= 3	        x = x | 3	
^=	              x ^= 3	        x = x ^ 3	
>>=	              x >>= 3	        x = x >> 3	
<<=	              x <<= 3	        x = x << 3	
:=	              print(x := 3)   	x = 3 print(x)

"""

## AND operation
x = 10
x = x & 3
print("Binary of 10:",format(10, 'b'))
print("Binary of 3:",format(3, 'b'))
print("10 & 3:",format(x, 'b'))

## OR operation
x = 10
x = x | 3
print("Binary of 10:",format(10, 'b'))
print("Binary of 3:",format(3, 'b'))
print("10 | 3:",format(x, 'b'))

## Left shift
x = 10
print("Binary of 10:",format(10, 'b'))
x = x << 3
print("After three left shift:",format(x, 'b'))  # -> 1010 ---> 1010000
print()

## Right shift
x = 23
print("Binary of 23:",format(x, 'b'))
x = x >> 3
print("After three right shift:",format(x, 'b'))  # -> 10111 ---> 00010
print()

## 
x = 10
print(x:=20)
print(x)
print()

## Walrus operator -> (:=)
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3: # Here two statement,, 1. count = len(numbers) 2. if count > 3:
    print(f"List has {count} elements")