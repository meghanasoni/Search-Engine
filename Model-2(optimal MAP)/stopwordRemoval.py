# -*- coding: utf-8 -*-
"""stopwordRemoval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UKqjrgmzw88xCoQYU1MjVECVFlYiAuAq
"""

#from util import *

# Add your import statements here

from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


class StopwordRemoval():

    def fromList(self, text):
        """
        Sentence Segmentation using the Punkt Tokenizer

        Parameters
        ----------
        arg1 : list
            A list of lists where each sub-list is a sequence of tokens
            representing a sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
            representing a sentence with stopwords removed
        """

        stopwordRemovedText = []
        stop_words = set(stopwords.words('english'))

        #Fill in code here
        for i in range(0,len(text)):
          arr=[]
          curr=text[i]
          for j in range(0,len(curr)):
            if curr[j] not in stop_words:
              arr.append(curr[j])
          stopwordRemovedText.append(arr)
          

        return stopwordRemovedText
#print("stopword removal done")