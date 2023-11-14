passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print ('Input your password')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
else:
    print('Access denied')