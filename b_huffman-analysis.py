# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

# DATA - lyrics
GUERILLA_RADIO = '''Transmission third world war third round a decade of the weapon of sound above ground no shelter if you\'re lookin\' for shade I lick shots at the brutal charade as the polls close like a casket on truth devoured a silent play in the shadow of power a spectacle monopolized the camera\'s eyes on choice disguised was it cast for the mass who burn and toil? Or for the vultures who thirst for blood and oil? yes a spectacle monopolized They hold the reins and stole your eyes Or the fistagons
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
CULT_OF_DIONYSUS = '''Yesterday I heard you say
Your lust for life has gone away
It got me thinking, I think I feel a similar way
And that\'s sad (that's sad)
That\'s sad
So let's make a decision, start a new religion
Yeah, we're gonna build a temple to our love
Orgiastic dances, nymphs in trances
Yeah, we\'ll be the envy of the gods above
I'm feeling devious
You\'re looking glamorous
Let\'s get mischievous
And polyamorous
Wine and women and wonderful vices
Welcome to the cult of Dionysus
We could take a Holiday in the month of May
Run free and play in fields of flowers
Pass the hours, making love is how we\'ll pray
Or start a secret society for the wild and free
Our ideology is You can do what you want
Too much is never enough
We are the Life, we are the light
We are the envy of the gods above
I\'m feeling devious
You\'re looking glamorous
Let\'s get mischievous
And polyamorous
Wine and women and wonderful vices
Welcome to the cult of Dionysus
Run, run, run away
Just take my hand and we\'ll abandon this world
We\'ll wash those tears away
You\'re young and beautiful, and I\'ll love you always
We got no time for pain
When it\'s just you and me in ecstasy
What is with the world today
The wicked games that people play
The wars, the greed they waste away
Yeah, it\'s sad (it\'s sad)
It\'s sad
So let\'s spread the word across the land
Yeah, one by one, baby hand in hand
We got a mission of hope
We got a message of love
Soon everybody, everywhere will be the envy of the gods above
I\'m feeling devious
You\'re looking glamorous
Let\'s get mischievous
And polyamorous
Wine and women and wonderful vices
Welcome to the cult of Dionysus
I'm feeling devious
You\'re looking glamorous
Let\'s get mischievous (run, run, run away)
And polyamorous
Wine and women and wonderful vices
Welcome to the cult of Dionysus'''
ITS_NOT_A_FASHION_STATEMENT_ITS_A_DEATHWISH = '''For what you did to me
And what I\'ll do to you
You get, what everyone else gets
You get a lifetime
Let\'s go
Do you remember that day when we met?
You told me this gets harder, well, it did
Been holding on forever
Promise me that when I've gone
You\'ll kill my enemies
The damage you\'ve inflicted, temporary wounds
I'm coming back from the dead
And I\'ll take you home with me
I\'m taking back the life you stole
We never got that far
This helps me to think all through the night
Bright lights that won't kill me now or tell me how
Just you and I, your starless eyes remain
Hip hip hooray for me, you talk to me
But would you kill me in my sleep
Lay still like the dead
From the razor to the rosary
We could lose ourselves
And paint these walls in pitchfork red
I will avenge my ghost with every breath I take
I\'m coming back from the dead
And I\'ll take you home with me
I\'m taking back the life you stole
This hole that you put me in
Wasn\'t deep enough
And I\'m climbing out right now
You\'re running out of places to hide from me
When you go
Just know that I will remember you
If living was the hardest part
We\'ll then one day be together
And in the end we\'ll fall apart
Just like the leaves changing colors
And then I will be with you
I will be there one last time now
When you go
Just know that I will remember you
I lost my fear of falling
I will be with you, I will be with you'''
# DATA - mantras
AMIDA_NEMBUTSU = 'Namu Amida Butsu'
BRISKET_BEATS_YOU_TO_DEATH = "Sorry, no installment plan! Pay up, please!"
HOID_QUOTE = "Aim for the sun. That way if you miss, at least your arrow will fall far away, and the person it kills will likely be someone you don\'t know."


# the input, what we want to encode
def huffman(msg:str) -> float:
    msg = msg.upper()

    # the output, should be all 0's and 1s
    result: str = str()

    # for counting the letter frequencies
    freq: dict = dict() # key  -> a letter
                        # item -> num of occurences

    # for holding the nodes of the huffman tree
    nodes: list = list() 

    # for storing the code for each letter
    global coding 
    coding = dict()   # key  -> a letter
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
        coding
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

    result = ""
    for letter in msg:
        result += coding[letter]

    print(result)

    # STEP 5
    ## analyize compression performance
    n_original_bits: int = len(msg) * 8
    n_encoded_bits: int = len(result)
    compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)

    return result, coding, compression_ratio

# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Terlato Analyzing Huffman')
plt.gcf().supylabel("Compression %")
plt.gcf().supxlabel("Length of Message")
MAX_N: int = int(128 * 3 / 2)
xsize = [i for i in range(1, MAX_N)]

# PLOT 1
## Guerilla Radio
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = GUERILLA_RADIO[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(xsize, ratios, linestyle="dashdot", linewidth=2)


## Cult Of Dionysus
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = CULT_OF_DIONYSUS[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(xsize, ratios, linestyle="dashdot", linewidth=2)

## It's Not A Fashion Statement It's A Deathwish
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = ITS_NOT_A_FASHION_STATEMENT_ITS_A_DEATHWISH[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(xsize, ratios, linestyle="dashdot", linewidth=2)
plt.legend(["Guerilla Radio (n=" + str(len(GUERILLA_RADIO)) + ")", "The Cult of Dionysus (n=" + str(len(CULT_OF_DIONYSUS)) + ")", "It\'s Not a Fashion Statement It\'s a Deathwish (n=" + str(len(ITS_NOT_A_FASHION_STATEMENT_ITS_A_DEATHWISH)) + ")"])


# PLOT 2
plt.subplot(2, 1, 2)

## Amida's Nembutsu
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = AMIDA_NEMBUTSU[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(xsize, ratios, linestyle="dashdot", linewidth=2)

## Bridget Victory Line
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = BRISKET_BEATS_YOU_TO_DEATH[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(xsize, ratios, linestyle="dashdot", linewidth=2)    

## Hoid Quote
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = HOID_QUOTE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(xsize, ratios, linestyle="dashdot", linewidth=2)    
plt.legend(["Amida\'s Nembutsu (n=" + str(len(AMIDA_NEMBUTSU)) + ")", "Bridget Voice Line Guilty Gear Strive (n=" + str(len(BRISKET_BEATS_YOU_TO_DEATH)) + ")", "Hoid Quote (n=" + str(len(HOID_QUOTE)) + ")"])

plt.show()
