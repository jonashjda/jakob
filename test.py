import pandas as pd
import operator
import matplotlib.pyplot as plt
import numpy as np

df_1 = pd.read_table("Trump_speeches/BattleCreekDec19_2019.txt")
df_2 = pd.read_table("Trump_speeches/BemidjiSep18_2020.txt")
df_3 = pd.read_table("Trump_speeches/CharlestonFeb28_2020.txt")
df_4 = pd.read_table("Trump_speeches/CharlotteMar2_2020.txt")
df_5 = pd.read_table("Trump_speeches/CincinnatiAug1_2019.txt")
df_6 = pd.read_table("Trump_speeches/ColoradorSpringsFeb20_2020.txt")
df_7 = pd.read_table("Trump_speeches/DallasOct17_2019.txt")
df_8 = pd.read_table("Trump_speeches/DesMoinesJan30_2020.txt")
df_9 = pd.read_table("Trump_speeches/FayettevilleSep9_2019.txt")
df_10 = pd.read_table("Trump_speeches/FayettevilleSep19_2020.txt")
df_11 = pd.read_table("Trump_speeches/FreelandSep10_2020.txt")
df_12 = pd.read_table("Trump_speeches/GreenvilleJul17_2019.txt")
df_13 = pd.read_table("Trump_speeches/HendersonSep13_2020.txt")
df_14= pd.read_table("Trump_speeches/HersheyDec10_2019.txt")


df = df_1 + df_2 + df_3 + df_4 + df_5 + df_6 + df_7 + df_8 + df_9 + df_10 + df_11 + df_12 + df_13 + df_14


def stopwords():
    return ["","a","about","above","after","again","against"]

def tokenizer(text, lower=True, stopword=True):
    if stopword:
        stopwordlist = stopwords()
        tokens = [token for token in text.lower().split(' ') if token not in stopwordlist]
    elif lower:
        tokens = text.lower().split()
    else:
        tokens = text.split()
    return tokens

def word_count(text, sort = True, stopword=True):
    counter = dict()
    for word in tokenizer(text, stopword=stopword):
        counter.setdefault(word, 0)
        counter[word] = counter[word] + 1
    if sort:
        counter = dict(sorted(counter.items(), key=operator.itemgetter(1), reverse=True))
    return counter

wc = word_count(' '.join(df))
wc_items = wc.items()
lst = list(wc_items)[:10]
print('[INFO] Top 10 most common words in Donald Trump rally speeches:')
print(lst)

def extractWords(lst):
    new_list = list()
    for i in lst:
        new_list.append(i[0])
    return new_list

def extractNums(lst):
    new_list = list()
    for i in lst:
        new_list.append(i[1])
    return new_list


x = extractWords(lst)
y = extractNums(lst)

print('[INFO] The 10 most used words:')
print(x)
print('[INFO] How many times they are used:')
print(y)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(x,y)
plt.show()
plt.close()