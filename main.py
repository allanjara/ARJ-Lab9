"""
This is Allan Rivera Jaramillo main.py file

Working with Maria Ilieva
"""

# Allan's encode password
"""
I used Lists in order to encode the password.
1) turn it into a list of strings
2) turn them into integers in order to encode the password and manipulate numbers based on prompt
3) create an empty list to store the encoded password
4) iterate through the list and account for values > 9 to return remainder from % 10
5) iterate through the list and return string values
6) join the list and return as a string

"""


def encode(password):
    x = list(password)
    y = [eval(i) for i in x]
    z = []
    for i in range(len(y)):
        z.append(y[i] + 3)
    for i in range(len(z)):
        if z[i] > 9:
            z[i] = z[i] % 10
    z = [str(i) for i in z]
    return ''.join(z)


# Maria's Decode Password
def decode(password):
    pass

# if __name__ == '__main__':
#     while True:
#         break
