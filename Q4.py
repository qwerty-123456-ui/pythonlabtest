# Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long. For example, generate_n_chars(5,"x") should return the string "xxxxx“ using keyword only parameters.

# def generate_n_chars(n,c):
#     return c*n

# print(generate_n_chars(5,"x"))
def generate_n_chars(c,n=0):
    z=""
    for i in range(n):
        z+=c
    return z
print(generate_n_chars(c="x",n=5))