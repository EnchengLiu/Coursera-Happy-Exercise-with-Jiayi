class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        result=""
        l1=len(str1)
        l2=len(str2)
        i=0
        
        
        while i<l1 or i<l2:
            
            result+=str1[i]
            if l1%(i+1)==0 and l2%(i+1)==0:
            #Check the beginning i place of code in m 
                for j in i:
                    if result[j]!=str2[i]:
                        return ""
            #Pass and then
            #Check the result for the rest of L1 and L2
                m=i
                while m+i<l1 or m+i<l2:
                    for k in i:
                        if result[k]!=str2[k+m] and result[k]!=str1[k+m]:
                            return ""
                    
                
                    
                    m+=i
                return result
               
            else:
                i+=1
                continue
            
            
            
        return ""