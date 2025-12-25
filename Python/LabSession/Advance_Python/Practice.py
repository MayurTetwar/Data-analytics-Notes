def get_sum(a,b):
    return (a+b)
def get_product(a,b):
    return (a*b)
def print_name():
    return "__name__ in Practice:",__name__

print(get_product(50,10))

# How the main is work??
# Here, __name__ is __main__ for this file
# for other files __name__ is __"filename"__ (here, __Practice__)
if __name__=="__main__":
    print(get_sum(10,20))
    print(print_name())
    print("I am in Practice File...")

