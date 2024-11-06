print ("CONVERT APP")
print (f"{10 * '='}")

user_input = input("Masukkan bilangan biner('1010') atau bilangan decimal('15') = ")
if set(user_input) <= {'0', '1'}:
    decimal = int(user_input, 2)
    print(f"binary: {user_input.zfill(4)} -> decimal: {decimal}")
else:
    binary = bin(int(user_input))[2:].zfill(4)
    print(f"decimal: {user_input} -> binary: {binary}")