# -*- coding: utf-8 -*-
"""tokenization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gRZ2CYomZt28VIUHEkQM75ya0y4JG42h
"""

#from util import *

# Add your import statements here
from nltk.tokenize import TreebankWordTokenizer
import string


class Tokenization():

    def naive(self, text):
        """
        Tokenization using a Naive Approach

        Parameters
        ----------
        arg1 : list
            A list of strings where each string is a single sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
        """
        print("using NAIVE")
        tokenizedText = []
        #Fill in code here
        for i in range(0,len(text)):
            st=text[i]
            arr=[]
            st+=" "
            s=""
            for j in range(0,len(st)):
                #print(st)
                if st[j]==' ':
                    if s!="":
                      arr.append(s)
                    s=""
                elif st[j] in string.punctuation:
                    if s!="":
                      arr.append(s)
                    s=""
                    s+=st[j]
                    arr.append(s)
                    s=""
                else:
                  s+=st[j]
            tokenizedText.append(arr)	  
        
        return tokenizedText



    def pennTreeBank(self, text):
        """
        Tokenization using the Penn Tree Bank Tokenizer

        Parameters
        ----------
        arg1 : list
            A list of strings where each string is a single sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
        """

        tokenizedText = []

        #Fill in code here
        for i in range(0,len(text)):
            sentence=text[i]
            arr=TreebankWordTokenizer().tokenize(sentence)
            tokenizedText.append(arr)
         
        return tokenizedText
#print("tokenization done")