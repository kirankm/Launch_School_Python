'''
PEDAC
Input String
Output 
Class called DNA
DNA has an instance variable for storing it's strand
    - No issue with empty strings
DNA has an instance method called hamming_distance
hamming_distance
    - Should compare up to length of the shorter string
    - Return an int value representing elementwise difference
'''

class DNA:
    def __init__(self, strand):
        self.strand = strand

    def hamming_distance(self, other_strand):
        mismatches = 0
        for i in range(0, min(len(self.strand), len(other_strand))):
            mismatches += (self.strand[i] != other_strand[i])
        return mismatches
