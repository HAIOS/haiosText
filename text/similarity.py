
#@source:geeksforgeeks & wikipedia
import math

class HammingDistance:
       def __init__():
           pass

class JaccardIndex:
        def __init__(self):
             pass

        def distance(self,a,b):
               """
                argument (set1,set2)
                return Jaccard index b/w two set
               """

               a=set(a)
               b=set(b)
               aIb = len(a.intersection(b))
               aUb = len(a)+len(b)-aIb
               x = float(aIb)/float(aUb)
               return x

class EditDistance:
        """
          distance bitween two string
        """
        def __init__(self):
            pass

        def distance(self,str1,str2,algo=2):
            if algo == 1:
               return self.algo1(str1,str2,len(str1),len(str2))
            else:
               return self.algo1(str1,str2,len(str1),len(str2))

        def algo1(self,str1, str2, m , n):
            """
            A Naive recursive Python program to fin minimum number
            operations to convert str1 to str2
            """
            # If first string is empty, the only option is to
            # insert all characters of second string into first
            if m==0:
                 return n

            # If second string is empty, the only option is to
            # remove all characters of first string
            if n==0:
                return m

            # If last characters of two strings are same, nothing
            # much to do. Ignore last characters and get count for
            # remaining strings.
            if str1[m-1]==str2[n-1]:
                return self.algo1(str1,str2,m-1,n-1)

            # If last characters are not same, consider all three
            # operations on last character of first string, recursively
            # compute minimum cost for all three operations and take
            # minimum of three values.
            return 1 + min(self.algo1(str1, str2, m, n-1),    # Insert
                           self.algo1(str1, str2, m-1, n),    # Remove
                           self.algo1(str1, str2, m-1, n-1)    # Replace
                           )

        def algo2(self,str1, str2, m, n):
            """
             A Dynamic Programming based Python program for edit
             distance problem
            """
            # Create a table to store results of subproblems
            dp = [[0 for x in range(n+1)] for x in range(m+1)]

            # Fill d[][] in bottom up manner
            for i in range(m+1):
                for j in range(n+1):

                    # If first string is empty, only option is to
                    # isnert all characters of second string
                    if i == 0:
                        dp[i][j] = j    # Min. operations = j

                    # If second string is empty, only option is to
                    # remove all characters of second string
                    elif j == 0:
                        dp[i][j] = i    # Min. operations = i

                    # If last characters are same, ignore last char
                    # and recur for remaining string
                    elif str1[i-1] == str2[j-1]:
                        dp[i][j] = dp[i-1][j-1]

                    # If last character are different, consider all
                    # possibilities and find minimum
                    else:
                        dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                           dp[i-1][j],        # Remove
                                           dp[i-1][j-1])    # Replace
            return dp[m][n]

if __name__ == '__main__':
      d = EditDistance()
      print d.distance("hitesh","aditi")
      a=[1,2,3,4,5,6,7,8]
      b=[1,11,11,11,4,3,2,5]
      j = JaccardIndex()
      print j.distance(b,a)
