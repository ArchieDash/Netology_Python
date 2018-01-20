mass = [int(n) for n in input().split()]  # read input() splitted by space and convert to int() 
print([n ** 3 for n in mass if n %  3 == 0 and n % 4 == 0]) # stdout() cubes with condition
print({n: n ** 3 for n in mass if n %  3 == 0 and n % 4 == 0 }) # more plain stdout() for user. You can definitely see which N we took

# TODO: a brief description of the multiple condition test?
