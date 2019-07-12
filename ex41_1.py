import random
from urllib.request import urlopen                      # from package.module import function
import sys
import urllib

WORD_URL = "http://learncodethehardway.org/words.txt"   
WORDS = []

PHRASES = {
    "class %%%(%%%):"                                : "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)"  : "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)"       : "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()"                                    : "Set *** to an instance of class %%%.",
    "***.***(@@@)"                                   : "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'"                                : "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True     
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding='utf-8'))   # [].append() --> WORDS[account, achieve, actor, ...]


def convert(snippet, phrase):                           # convert(dict key, dict alue)
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]  
    # Above equals to: for w in random.sample(WORDS, snippet.count("%%%"):  w.capitalize()
    print('class_names=', class_names)    
    other_names = random.sample(WORDS, snippet.count("***"))                           
    print('other_names=', other_names)    
    results = []
    param_names = []
    
    # A new list: results[updated dict key, updated dict value]
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        print('param_count=', param_count)
        param_names.append(', '.join(random.sample(WORDS, param_count)))               
        print('param_names=', param_names)

    for sentence in snippet, phrase:          
        result = sentence[:]                  

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1) 
            print('result1=', result)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
            print('result2=', result)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
            print('result3=', result)

        results.append(result)
        print('results=', results)          

    return results                                      # Return results[updated dict key, updated dict value]


# keep going until they hit CTRL-C
try:
    while True:                                         # endless loop
        snippets = list(PHRASES.keys())     
        random.shuffle(snippets)            

        for snippet in snippets:            
            phrase = PHRASES[snippet]       
            print(snippet,": ", phrase)
            question, answer = convert(snippet, phrase) 
            if PHRASE_FIRST:
                question, answer = answer, question     

            print('\n\nQuestion:', question)

            input("> Please try to input the answer:")
            print(f"ANSWER: {answer}\n\n\n\n")
except EOFError:
    print("\nBye")

