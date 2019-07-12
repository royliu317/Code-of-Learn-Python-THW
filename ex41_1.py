import random
from urllib.request import urlopen      # from package.module import function
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


def convert(snippet, phrase):       # convert(字典key, 字典value)
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]  #w.capitalize()：字符串首字母大写，其他字母小写
    # 如上等同于 for w in random.sample(WORDS, snippet.count("%%%"):  w.capitalize()
    print('class_names=', class_names)    
    other_names = random.sample(WORDS, snippet.count("***"))                            #  snippet.count("***")：返回"xxx"在snippet（字典key）中出现的次数
    # 如上表示从单词列表中随机选取x个单词，并以列表形式返回
    print('other_names=', other_names)    
    results = []
    param_names = []
    
    # 下面的4个for循环，第1个用来构建如上的param_names列表并用于第4个for循环，第2-4个用来构建如上的results列表（分别用于替换字典key、字典value中的各类字符）
    # 最终，组成一个新的列表results[updated 字典key, updated 字典value]
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        print('param_count=', param_count)
        param_names.append(', '.join(random.sample(WORDS, param_count)))                # 以','作为分隔符，将join中每个数据项进行分隔，并返回1个新的字符串str
        print('param_names=', param_names)

    for sentence in snippet, phrase:                # 先以sentence=snippet进行首次循环，再以sentence=phraes进行第2次循环（因为snippet与phrase是两个str）
        result = sentence[:]                        # 创建列表副本（以列表切片的方式），但在此无意义，因为sentence并非列表，而是str，所以result也还是str

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1) # 把“%%%”替换为变量word（仅替换1次）
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

    return results                          # 函数返回列表results[updated 字典key, updated 字典value]


# keep going until they hit CTRL-C
try:
    while True:                             # 无限循环
        snippets = list(PHRASES.keys())     # {}.keys():取字典所有keys值，返回迭代器，即snippets = ["class %%%(%%%):", "...", ...]
        random.shuffle(snippets)            # 打乱snippets列表内数据项的顺序

        for snippet in snippets:            # 子循环：循环(打乱了的)字典keys
            phrase = PHRASES[snippet]       # 字典value = 字典[key]，即取字典key对应的value
            print(snippet,": ", phrase)
            question, answer = convert(snippet, phrase) # convert()返回包含两个数据项的列表，第1个（updated 字典key）赋给question变量，第2个（updated 字典value）赋给answer变量
            if PHRASE_FIRST:
                question, answer = answer, question     # 两个变量的值对调（python支持多重赋值）

            print('\n\nQuestion:', question)

            input("> Please try to input the answer:")
            print(f"ANSWER: {answer}\n\n\n\n")
except EOFError:
    print("\nBye")

