

def number_pattern(n):
    if not isinstance(n, int):
        print("Argument must be an integer value.")
        # exit
    elif n < 1:
        print("Argument must be an integer greater than 0.")
        # exit
    else:
        result = ""
        for i in range(1, n+1):
            result += str(i) + " "
            
        return result

nm = input("Enter the number : ")
print(number_pattern(int(nm)))

## ==================================================================================================
## site edition


# def number_pattern(n):
#     if not isinstance(n, int):
#         return "Argument must be an integer value."
#         # exit
#     elif n < 1:
#         return "Argument must be an integer greater than 0."
#         # exit
#     else:
#         result = ""
#         for i in range(1, n+1):
#             if i == n:
#                 result += str(i)
#             else: 
#                 result += str(i) + " "
#         return result

# print(number_pattern(4))
