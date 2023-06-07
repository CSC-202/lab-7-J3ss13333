# huffman.py
## author - nick s.
### get huffman to work first here, then make it into a function for the analysis

# the input, what we want to encode
msg: str = '''Transmission third world war third round a decade of the weapon of sound above ground no shelter if you\'re lookin\' for shade I lick shots at the brutal charade as the polls close like a casket on truth devoured a silent play in the shadow of power a spectacle monopolized the camera\'s eyes on choice disguised was it cast for the mass who burn and toil? Or for the vultures who thirst for blood and oil? yes a spectacle monopolized They hold the reins and stole your eyes Or the fistagons
The bullets and bombs
Who stuff the banks
Who staff the party ranks
More for Gore or the son of a drug lord
None of the above fuck it cut the cord
Lights out
Guerrilla Radio, turn that shit up
Lights out
Guerrilla Radio, turn that shit up
Lights out
Guerrilla Radio, turn that shit up
Lights out
Guerrilla Radio
Contact I highjacked the frequencies
Blockin\' the beltway
Move on D.C.
Way past the days of Bombin\' M.C.\'s
Sound off Mumia gwan be free
Who gottem yo check the federal file
All you pen devils know the trial was vile
An army of pigs try to silence my style
Off \'em all out that box
It\'s my radio dial
Lights out
Guerrilla Radio, turn that shit up
Lights out
Guerrilla Radio, turn that shit up
Lights out
Guerrilla Radio, turn that shit up
Lights out
Guerrilla Radio, turn that shit up
It has to start somewhere, it has to start sometime
What better place than here, what better time than now?
All hell can\'t stop us now
All hell can\'t stop us now
All hell can\'t stop us now
All hell can\'t stop us now
All hell can\'t stop us now All hell can\'t stop us now'''

# the output, should be all 0's and 1s
result: str = str()

# for counting the letter frequencies
freq: dict = dict() # key  -> a letter
                    # item -> num of occurences

# for holding the nodes of the huffman tree
nodes: list = list() 

# for storing the code for each letter
coding: dict = dict()   # key  -> a letter
                        # item -> a binary encoding


# STEP 0 
## defining our data structures
class Node: # NOT given to students
    frequency: int
    letter: str
    left: any
    right: any

    def __init__(self, letter, frequency, left=None, right=None):
        self.left = left
        self.right = right
        self.letter = letter
        self.frequency = frequency
        

    def __str__(self):
        return "Letter: " + str(self.letter) + ", Frequency: " + str(self.frequency) + ", Left: (" + str(self.left) + "), Right: (" + str(self.right) + ")"

## defining operations
### recursively traverses the huffman tree to record the codes
def retrieve_codes(v: Node, path: str=''):
    global coding
    if v.letter != None: 
        coding[v.letter] = path
    else:
        retrieve_codes(v.left, path+"0")
        retrieve_codes(v.right, path+"1")

# STEP 1
## counting the frequencies 
msg = msg.lower()
for letter in msg:
    if letter not in freq.keys():
        freq[letter] = 1
    else:
        freq[letter] += 1


# STEP 2
## initialize the nodes
nodes = list()
for (letter, freq) in freq.items():
    nodes.append(Node(letter, freq))


# STEP 3 
## combine each nodes until there's only one item in the nodes list
while len(nodes) > 1:
    ## sort based on weight
    nodes.sort(key=lambda x: x.frequency, reverse=True)

    ## get the first min
    min_a: Node = nodes.pop()

    ## get the second min
    min_b: Node = nodes.pop()

    ## combine the two
    combined = Node(letter=None, frequency=(min_a.frequency + min_b.frequency), left=min_b, right=min_a)

    ## put the combined nodes back in the list of nodes
    nodes.append(combined)

# STEP 4
## reconstruct the codes
huff_root = nodes[0]
retrieve_codes(huff_root)
print(coding)

result = ""
for letter in msg:
    result += coding[letter]

print(result)

# STEP 5
## analyize compression performance
n_original_bits: int = len(msg) * 8
n_encoded_bits: int = len(result)
compression_ratio: float = (1 - n_encoded_bits / n_original_bits) * 100

print(f'original: {n_original_bits:^4d} bits')
print(f'encoded : {n_encoded_bits:^4d} bits')
print(f'savings : {int(compression_ratio):^4d} % compression')