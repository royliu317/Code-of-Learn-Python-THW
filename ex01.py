print("Hello World!") 
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.') 
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

#-------------------------------------------------------------------
print("-----------------------------------------------------------")
print() 
print(9)
print('\n' *2, end='8') # end'' is used to set how the output of print() will end. By default it is \n
print('7') 
print("\n")             # Output includes 2 newlines. One is the defalut \n，another is the \n wrote in here
print('1' *3)

print('\n' *2) 
print(1*2*3)

print("\n" *0)          # Output includes 1 newline since \n set to 0 means no newline
print(5)

print('\n', end='')     # Output includes 1 newline since end is not the default vale (one newline) in here
s="It's me again"
print(s)

print('abc', end='')    
print('def')

for i in range(0,6):
    print(i)

for i in range(0,6):
    print(i, end='') 
 
