n = input()
m = input()

string_numbers = m.split()
int_numbers = list(map(int, string_numbers))

maxi = max(int_numbers)
print(maxi)
