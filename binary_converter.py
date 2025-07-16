# File      : binary_converter.py
# Author    : Srikanth v
# Date      : 09/07/2025

"""
This script will get an decimal integer input
and show the binary value as the outpu
"""

# Getting the input Value
decimal_value = int(input("Please Enter a integer value to convert into binary : "))

# Display the decimal value
print(f"Your input decimal value : {decimal_value}")

# Binary conversion Logic
remainder_value = decimal_value%2
count = 0                         # This will add the binary value
bin_value = 0                      # This will initialise the bin_value

while decimal_value > 0:
    remainder_value = decimal_value % 2
    bin_value = bin_value + (remainder_value * 10**count)
    count = count+1
    decimal_value = decimal_value // 2
    print("decimal_value ",decimal_value)
    print("remainder_value ",remainder_value)
    print("count ",count)
    print("binary value ",bin_value)

        
    
    
    
    
    

    


