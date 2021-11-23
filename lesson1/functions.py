def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return f"{one} {delimiter} {two}"

merged_string = get_summ("Learn", "python")
upper_cased_string = merged_string.upper()
print(merged_string)
print(upper_cased_string)
