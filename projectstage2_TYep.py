Q1 = ''' In the Periodic table, there are 18 groups. Of those groups, groups numbers _a_, _b_, and _c_ contains the most elements that can be classified as metalloids or semi-metals.'''

Q2 = '''_d_ is a process by which molecules are separated based on their respective charged groups.In this process, analyte molecules adhere to the column based on _e_ interactions. The _f_ phase or the analytes undergo electrostatic interactions with opposite charges on the _g_ phase. The immobile matrix consists of charged ionizable functional groups or _h_ which
acts as the active site for interaction with the analyte molecules. '''

Q3 = '''_i_ carry oxygen-rich blood from the heart to all parts of the body and _j_ carry carbon dioxide-rich blood from all parts of the body back to the heart.
 _k_ have thin walls and _l_ have thick elastic walls.
Blood flows at high pressure in _m_. Valves are present in _n_ which allow blood to flow only towards the heart. _o_ divide into smaller vessels. These vessels further divide into extremely thin tubes called capillaries.
These capillaries join up to form _p_.'''

Q1key = ['_a_','_b_','_c_']

q1answerkey = ['14','15','16']
Q2key = ['_d_','_e_','_f_','_g_','_h_']

q2answerkey = ['Ion exchange','ionic','mobile','stationary','ligands']
Q3key = ['_i_','_j_','_k_','_l_','_m_','_n_','_o_','_p_']

q3answerkey = ['arteries','veins','veins','arteries','veins','arteries','veins','venules']

# Function requests for user's choice/input which is then used to execute game levels based on choice.
def LevelDiff():
    print "Choose a level of difficulty [Easy] [Medium] [Hard]"
    CurrentLevel = raw_input(": ")
    CurrentLevel = CurrentLevel.upper()
    # converts all user inputs into all-caps inputs
    if CurrentLevel == 'EASY':
        easyGame()
    elif CurrentLevel == 'MEDIUM':
        medGame()
    elif CurrentLevel == 'HARD':
        hardGame()
        # All the if and elif statements call game based on the user input
    else:
        print 'Thank you for trying my quiz! Goodbye!'

# function looks for word in array that matches parts_of_speech and returns the word.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Function replaces blank with correct answers, displays updated question_duplicate and returns updated question_duplicate
# Calls all necessary variables that are required for carrying out the updates.
def correct_ans(question_duplicate,replacement,user_input,word,replaced, answerkey):
    question_duplicate = question_duplicate.replace(replacement, user_input)
    # replaces replacement word/blank with correct user_input
    print question_duplicate
    word = word.replace(replacement, user_input)
    # updates word with correct user_input
    replaced.append(word)
    # adds correct user_input into array 'replaced'
    return question_duplicate
    # returns updated question_duplicate which will then be stored as new question_duplicate in play_game function

# function loops until correct answer is input
def re_game(question_duplicate, answerkey, user_input, Ans_index, replacement):
    while user_input != answerkey[Ans_index]:
        print "Incorrect answer. Try again."
        print question_duplicate
        user_input = raw_input("What is " + replacement + "? ")
        if user_input == answerkey[Ans_index]:
            question_duplicate = question_duplicate.replace(replacement, user_input)
            print question_duplicate
            break

# main game function, takes 3 inputs to compare answers to user input
def play_game(question, questionkey, answerkey):
    replaced = []
    question_duplicate = question
    question = question.split()
    for word in question:
        # loops through all elements of list 'question'
        replacement = word_in_pos(word, questionkey)
        if replacement != None:
            # blank found, user input required
            user_input = raw_input("What is " + replacement + "? ")
            # user input is compared to question key to find index, which is then stored in variable
            # ans_index which is then used to compare it to answerkey
            Ans_index = questionkey.index(replacement)
            # when answer is correct, the answer replaces blank in final prompt.
            if answerkey[Ans_index] == user_input:
                # question_duplicate acts as string where correct user input replace blanks
                question_duplicate = correct_ans(question_duplicate,replacement,user_input,word, replaced,answerkey)
                # stores returned question_duplicate value for later use.
                # # prompt question with blanks replaced.
            else:
                re_game(question_duplicate,answerkey,user_input,Ans_index, replacement)
                # calls function re_game that loops until user inputs correct answer
        else:
            replaced.append(word)
            # Keeps appending words that are not picked out by word_in_pos

# 'level'Game() functions display questions based on LevelDiff() input and calls play_game function to execute game.
# If all answers are correct, it will prompt 'Game complete'.
def easyGame():
    print Q3
    play_game(Q3,Q3key,q3answerkey)
    print "Game complete"


def medGame():
    print Q2
    play_game(Q2,Q2key,q2answerkey)
    print "Game complete"

def hardGame():
    print Q1
    play_game(Q1,Q1key,q1answerkey)
    print "Game complete"

def GameOn():
    LevelDiff()
    # function asks for level preference

GameOn()
