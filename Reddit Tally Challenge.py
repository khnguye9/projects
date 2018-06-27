scores = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
score_input = "EbAAdbBEaBaaBBdAccbeebaec" #4 a's, 4 b's, 3 c's, 2 d's, 3 e's
points = "abcde"

def tally_score(s1:str, s2:str): # takes in 2 strings, the challenged input and the string to know if you score a point
    for x in s1: #checks every value in the challenge string
        if x in scores: # checks if lower case letters are in the challenged string
            scores[x] += 1 # adds 1 to the corresponding letter in the dictionary
        elif x not in scores: #if the value is not a lower case letter
            scores[x.lower()] -= 1 # subtracts 1
    sorted_score = sorted(scores.items(), key = lambda x: x[1], reverse =True) #sorts the dictionary by its values
    print(sorted_score) #prints out the sorted dictionary
tally_score(score_input, points) # calls the function
