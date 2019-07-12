from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read() 

out_file = open(to_file, 'w').write(indata) 

#fwhen ileObject.write() runs，write() function will not transfer the type of fileObject，so below commands will always keep out_file as file object type:
#out_file.write(indata)
#out_file = open(to_file, 'w')
#print(type(out_file))
#out_file.write(indata) 
#print(type(out_file)) 