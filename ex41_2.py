import random

print(random.random())               
print(random.randint(1, 10))         
print(random.uniform(1.1, 5.4))      
print(random.randrange(1, 100, 50))  
print(random.choice('tomorrow'))     
print(random.sample(range(100), 10)) 

a = [1,3,5,6,7]               
print(random.shuffle(a))             


# help('urllib')			        Help on package urllib
# help('urllib.request')		    Help on module urllib.request in urllib
# help('urllib.request.urlopen')	Help on function urlopen in urllib.request