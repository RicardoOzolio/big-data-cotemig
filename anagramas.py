# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:08:41 2019

@author: pb002780
"""
def load_english():
    DICTIONARY_FILE="D:/Ricardo/Cotemig/big-data-cotemig/lab2/words"
    words_list=[]
    with open(DICTIONARY_FILE) as file:
        for line in file:
            words_list.append(line.strip())
    return words_list

# write a program that, given letters, finds all anagrams
def anagrammer(letters, words):
    anagrams=[]    
    #loop pesquisando o arquivo de palavras verificando se a palavra contém as mesmas letras
    for word in words:
        flag = True
        #print(flag)
        
        if len(word) == len(letters): #se os tamanhos forem diferentes, não são anagramas.
            for n in range(len(word)):
                if word[n] not in letters or word.count(word[n]) != letters.count(word[n]):
                    flag = False
                    #verificar se cada letra da string está na palavra atual 
                    #e se número de ocorrência da letra é a mesma nas duas palavras
        else:
            flag = False
        #print(flag)
        if flag:
            anagrams.append(word)
    return anagrams

anagrammer("hnopty", load_english())