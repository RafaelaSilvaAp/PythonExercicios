algo = input('Digite algo: ')
print('o tipo primitivo desse valor é ',type(algo))

print('Só tem espaços? ',algo.isspace())
print('é um número ? ',algo.isnumeric())
print('é alfabético ?',algo.isalpha())
print('é alfanumérico ? ',algo.isalnum())
print('está em maiúsculas ? ',algo.isupper())
print('está em minúsculas ? ',algo.islower())
print('está capitalizada ? ',algo.istitle())
