kotely = "(<v>)"
print(kotely)
owcaUser = input('Podaj ile kotelow chcesz wygenerowac')
print(owcaUser)
try:
    owcaUser = int(owcaUser)
except ValueError as owcaError:
    owcaUser = 1
    print('program potrzebuje liczby a nie ciagu znaku')

print (kotely * owcaUser)
    





