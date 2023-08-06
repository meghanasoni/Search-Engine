

# Add your import statements here
import math

class Evaluation():

    def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The precision value as a number between 0 and 1
        """

        precision = -1

        val=0
        for i in range(0,k):
          doc=query_doc_IDs_ordered[i]
          doc=str(doc)
          if doc in true_doc_IDs:
            
            val+=1
    
        precision = val/k


        #Fill in code here

        return precision


    def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean precision value as a number between 0 and 1
        """

        meanPrecision = 0
        
        for i in range(0,len(query_ids)):
            vec=[]
            for j in range(0,len(qrels)):
                val1= qrels[j]["query_num"]
                val2 =query_ids[i]
                val1=str(val1)
                val2=str(val2)
                if val1==val2:
                    t=qrels[j]['id']
                    vec.append(t)
            
            pr=self.queryPrecision(doc_IDs_ordered[i],query_ids[i],vec,k)
            meanPrecision+=pr
        
        meanPrecision= (meanPrecision/len(query_ids))

        #Fill in code here
        return meanPrecision

    
    def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The recall value as a number between 0 and 1
        """

        recall = 0

        #Fill in code here

        val=0
        for i in range(0,k):
           doc=query_doc_IDs_ordered[i]
           doc=str(doc)
           if doc in true_doc_IDs:
              val+=1
        
        recall= val/len(true_doc_IDs)

        return recall


    def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean recall value as a number between 0 and 1
        """

        meanRecall = 0

        #Fill in code here

        for i in range(0,len(query_ids)):
            vec=[]
            for j in range(0,len(qrels)):
                val1= qrels[j]["query_num"]
                val2 =query_ids[i]
                val1=str(val1)
                val2=str(val2)
                if val1==val2:
                    t=qrels[j]['id']
                    vec.append(t)

            pr=self.queryRecall(doc_IDs_ordered[i],query_ids[i],vec,k)
            meanRecall+=pr

        meanRecall=(meanRecall/len(query_ids))

        return meanRecall


    def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The fscore value as a number between 0 and 1
        """

        fscore = 0

        #Fill in code here
        pr=  self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        re = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        if pr==0 or re==0:
            fscore=0
        else:
           fscore = (2*pr*re)/(pr+re)

        return fscore


    def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value
        
        Returns
        -------
        float
            The mean fscore value as a number between 0 and 1
        """

        meanFscore = 0
        for i in range(0,len(query_ids)):
            vec=[]
            for j in range(0,len(qrels)):
                val1= qrels[j]["query_num"]
                val2 =query_ids[i]
                val1=str(val1)
                val2=str(val2)
                if val1==val2:
                    t=qrels[j]['id']
                    vec.append(t)

            pr=self.queryFscore(doc_IDs_ordered[i],query_ids[i],vec,k)
            meanFscore+=pr

        meanFscore=(meanFscore/len(query_ids))

        #Fill in code here
        return meanFscore
    

    def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of nDCG of the Information Retrieval System
        at given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The nDCG value as a number between 0 and 1
        """
        
        vals=list(true_doc_IDs.values())

        for i in range(0,k):
            vals.append(0)
        
        sorted_numbers = sorted(vals, reverse=True)

        DCG=0
        IDCG=0
        nDCG = 0

        for i in range(0,k):
            t=str(query_doc_IDs_ordered[i])
            if t in true_doc_IDs:
               tem=int(true_doc_IDs[t])
               val = tem*(1/math.log2(i+2))
               DCG+=val
            else:
               tem=0
               val = tem*(1/math.log2(i+2))
               DCG+=val

            IDCG+= (int((sorted_numbers[i]))*(1/math.log2(i+2)))



        #Fill in code here
        nDCG=(DCG)/(IDCG)

        return nDCG


    def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of nDCG of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean nDCG value as a number between 0 and 1
        """
        

        meanNDCG = 0


        
        for i in range(0,len(query_ids)):
            mp={}
            
            for j in range (0,len(qrels)):
                val1= qrels[j]["query_num"]
                val2 =query_ids[i]
                val1=str(val1)
                val2=str(val2)
                if val1==val2:
                    
                    temp=qrels[j]
                    
                    mp[temp["id"]]=5-temp["position"]
            

            pr=self.queryNDCG(doc_IDs_ordered[i],query_ids[i],mp,k)
            meanNDCG+=pr

        meanNDCG=(meanNDCG/len(query_ids))

       
        #Fill in code here

        return meanNDCG


    def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of average precision of the Information Retrieval System
        at a given value of k for a single query (the average of precision@i
        values for i such that the ith document is truly relevant)

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The average precision value as a number between 0 and 1
        """

        avgPrecision = 0
        sum=0
        val=0

        for i in range(0,k):
            t=str(query_doc_IDs_ordered[i])
            if t in true_doc_IDs:
               pr=self.queryPrecision(query_doc_IDs_ordered,query_id,true_doc_IDs,i+1)
               sum+=pr
               val+=1
        if val==0:
            avgPrecision=0
        else:
            avgPrecision=sum/val
        #Fill in code here

        return avgPrecision


    def meanAveragePrecision(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of MAP of the Information Retrieval System
        at given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The MAP value as a number between 0 and 1
        """

        meanAveragePrecision = 0
        

        
        for i in range(0,len(query_ids)):
            vec=[]
            for j in range(0,len(qrels)):
                val1= qrels[j]["query_num"]
                val2 =query_ids[i]
                val1=str(val1)
                val2=str(val2)
                if val1==val2:
                    t=qrels[j]['id']
                    vec.append(t)

            pr=self.queryAveragePrecision(doc_IDs_ordered[i],query_ids[i],vec,k)
            meanAveragePrecision+=pr

        meanAveragePrecision=(meanAveragePrecision/len(query_ids))

        #Fill in code here

        return meanAveragePrecision

