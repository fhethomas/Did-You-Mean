import numpy as np
"""
Below code aims to create a class that on creation takes in a list of words
Can look for the most similar word to any word you have by calling find_most_similar function
this will find most similar word in your class's dictionary

The function will use the Levenshtein Distance to judge similarity of words
"""
class Dictionary:
    def __init__(self,words):
        self.words=words
    #first need to create a Levenshtein Distance function
    #this will find the distance from one word to another
    def levenshteinDistance(self,term,word):
        #creates an empty array
        d_array=np.zeros((len(term)+1,len(word)+1))
        #array items along top and side are equal to row/column number
        for i in range(0,len(term)+1):
            d_array[i,0]=i
        for j in range(0,len(word)+1):
            d_array[0,j]=j
        #try and match each letter, if they don't equal then add lowest cost
        for j in range(1,len(word)+1):
            for i in range(1,len(term)+1):
                if term[i-1]==word[j-1]:
                    substitutioncost=0
                else:
                    substitutioncost=1
                d_array[i,j]+=min(d_array[i-1,j]+1,d_array[i,j-1]+1,d_array[i-1,j-1]+substitutioncost)
        #return the max item in array
        return d_array[-1,-1]
    #apply Levenshtein distance to test term against dictionary
    def find_most_similar(self,term):
        dic={}
        for x in self.words:
            dic[x]=self.levenshteinDistance(term,x)
        min_value=min(dic.values())
        for x in sorted(list(dic.keys())):
            if dic[x]==min_value:
                print(x)
                return x
