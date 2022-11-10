#!/usr/bin/env python
# coding: utf-8

# In[6]:


f = open("test.txt", "r")
text=f.read()
# print(text)
f.close()
f=open("testfile.txt", "w+")
text2=''
if ' ' in text:
    text2 = text.replace('.' , '.'+'\n')
    print(text2)
    f.write(text2)
f.close()


# Q.1 How should you segment sentences with semi-colon? As a single sentence or as two sentences? Should it depend on context?

# Use a semicolon between closely related independent clauses which are not joined by a coordinating conjunction. This rule means that semicolons are used between two complete sentences which are not already linked by words like and, but, or, nor, for, so, yet.Whether to use a period or semicolon depends completely on context.

# Q2. Should sentences with ellipsis... be treated as a single sentence or as several sentences?

# We can consider as  several sentences as it joins two statement i.e before and after the ellipsis

# Q3.If there is an exclamation after the first word in the sentence should it be a separate sentence? How about if there is a comma?

# No, it cannot be considered as seperate sentence since it is continuation of single statment. Also, even if it is comma it doesnt make any difference since the sentence continues.

# Q4.Can you think of some hard tasks for the segmenter?

# a. the study of sentence structure
# b. the study of the context of the statement
# c. the study of linguistic meaning

# In[35]:


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
f = open("text1.txt", "r")
text=f.read()
# print(text)
f.close()
f=open("text3.txt", "w+")
text2=''
for i in text:
    if i in punctuations:
        text2= text.replace(i,'\n')
        print(text2)
        
# from nltk.tokenize import WordPunctTokenizer
# text = open("text1.txt", "r")
# print("\nOriginal string:")
# print(text)
# result = WordPunctTokenizer().tokenize(text)
# print("\nSplit all punctuation into separate tokens:")
# print(result)


# Why should we split punctuation from the token it goes with ?

# Punctuation is treated as a token separate from word tokens and number tokens.

# Should abbreviations with space in them be written as a single token or two tokens ?

# Yes, they will be considered as single token. Numerals like 134 000  will also be consdidered as single token

# If you have a case suffix following punctuation, how should it be tokenised ?

# It will be tokenized as two separate tokens.

# It can be tokenized as single token as we will not understand until we know the context of the statement

# In[ ]:




