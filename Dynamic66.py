def prob6_25(combo,size):
    
    
    finalVar = ''
    def letsMultiply(varOne,varTwo):
        finalVar=' '
        if varOne=='a' and varTwo=='a':
            finalVar='b'
        elif varOne=='a' and varTwo=='b':
            finalVar='b'
        elif varOne=='a' and varTwo=='c':
            finalVar='a'
        elif (varOne=='b' and varTwo=='a'):
            finalVar='c'
        elif varOne=='b' and varTwo=='b':
            finalVar='b'
        elif varOne=='b' and varTwo=='c':
            finalVar='a'
        elif varOne=='c' and varTwo=='a':
            finalVar='a'
        elif varOne=='c' and varTwo=='b':
            finalVar='c'
        elif varOne=='c' and varTwo=='c':
            finalVar='c'
        return finalVar
      
    Matrix = [[set() for x in range(size)] for y in range(size)]
    for i in range (0,len(combo)):
        Matrix[i][i].add(combo[i])
    for i in range (0,len(combo)-1):
        theAnswer= letsMultiply(combo[i],combo[i+1])
        print(combo[i],combo[i+1], theAnswer)
        Matrix[i][i+1].add(theAnswer)
    for i in range(0,len(combo)-2):
        theAnswerTwo= letsMultiply(Matrix[i][i+1],combo[i+2])
        print(Matrix[i][i+1],combo[i+2], theAnswer)

        Matrix[i][i+2].add(theAnswerTwo)    
    
        

    print(Matrix)









arrTwo = ['b', 'b', 'b', 'b', 'a', 'c'] 
arr = ['b', 'a', 'c', 'a']
n = len(arr) 
prob6_25(arr,n)
  

# # Only populate the entry if needed, i.e. it's empty.
#     if len(solutions[i][j]) == 0:
#         # Base case: P(i, i) = a[i]
#         if j - i == 0:
#             solutions[i][j].add(sequence[i])
#         # Base case: P(i, i + 1) = a[i] * a[i + 1]
#         elif j - i == 1:
#             solutions[i][j].add(key[sequence[i] - 1][sequence[j] - 1])
#         else:
#             # Let k represent where the sequence is divided/parenthesized.
#             for k in range(i, j):
#                 # Evaluate both sides of the parenthesization. 
#                 a = problem6_6_helper(sequence, solutions, i, k)
#                 b = problem6_6_helper(sequence, solutions, k + 1, j)

#                 # Evaluate all possible outcomes of multiplying the sets.
#                 for x in a:
#                     for y in b:
#                         solutions[i][j].add(key[x - 1][y - 1])