import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer

class InformationRetrieval:
    def __init__(self):
        self.index = None
        self.docIDs = None
        self.vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        self.svd = TruncatedSVD(n_components=400)

    def buildIndex(self, docs, docIDs):
        """
        Builds the document index in terms of the document
        IDs and stores it in the 'index' class variable

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is
            a document and each sub-sub-list is a sentence of the document
        arg2 : list
            A list of integers denoting IDs of the documents
        Returns
        -------
        None
        """
       
        self.docIDs = docIDs
        doc_strings = [' '.join([' '.join(sent) for sent in doc]) for doc in docs]
        X = self.vectorizer.fit_transform(doc_strings)
        X_reduced = self.svd.fit_transform(X)
        self.index = X_reduced

    def rank(self, queries):
        """
        Rank the documents according to relevance for each query

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is a query and
            each sub-sub-list is a sentence of the query

        Returns
        -------
        list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        """
        query_strings = [' '.join([' '.join(sent) for sent in query]) for query in queries]
        Y = self.vectorizer.transform(query_strings)
        Y_reduced = self.svd.transform(Y)
        scores = np.dot(Y_reduced, self.index.T)
        rankings = np.argsort(scores, axis=1)[:, ::-1]
        results = [[self.docIDs[j] for j in ranking] for ranking in rankings]
        return results
