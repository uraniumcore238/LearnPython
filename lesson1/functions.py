def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return f"{one} {delimiter} {two}"

a = get_summ("Learn", "python")
b = a.upper()
print(a)
print(b)
