a = 12 # 1100 in binary
b = 4 # 0100 in binary

# Bitwise And if both the bits are 1 then only its going to return 1
result= a & b
print(f"Bitwise And {result}")

# Bitwise Or if one of the bits is 1 then its return 1
result= a | b 
print(f"Bitwise Or {result}")

# Bitwise Xor , its return true when both the bits are different otherwise its return false
result= a ^ b 
print(f"Bitwise Xor {result}")

# Bitwise Not return compliment of bits
a=2
result= ~a
print(f"Bitwise Not of a {result}")

# Bitwise left shift , shift the whole bits to left site 
# 8 4 2 1 
# 1 1 0 0 binary representation of 12
# now if we shift the 1100 to left side by 2 bits 
# 32 16 8 4 2 1 (16 and 32 is added to left side )
# 1  1  0 0 0 0 (now the 1100 is start from 32 and remaning 2 bits will become 0)
a=12
result= a << 2
print(f"Bitwise left shift of a {result}")

# Bitwise Right shift
a=12
result= a >> 2
print(f"Bitwise right shift of a {result}")
