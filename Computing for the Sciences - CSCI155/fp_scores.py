"""
CSCI 150 Final Program 1

Name: Dean Smith
Section: V

"""


def cut_next_comma(string):
    """
    This function slices a string after the first comma in the string
    Inputs string(str)
    Return: string after first comman in input string
    """
    return string[string.find(',') + 1:]


def read_scores(grade_file):
    """
    This function opens and reads a input text file and sorts the values into a tuple of
    weights for grades, max scores, and the score the person got.
    Inputs: grade_file (text file)
    Return: tuple of list of weights, list of max scores, and list of scores the student got.
    """
    
    weights = []
    weight = ''
    
    max_scores = []
    max_score = ''
    
    my_scores = []
    my_score = ''
    
    with open(grade_file, 'r') as file:
        for line in file:
            
            stat_line = cut_next_comma(line) #string after name of the assignment
            
            weight = stat_line[:stat_line.find(',')] #first value
            weights.append(float(weight))
            
            stat_line = cut_next_comma(stat_line) #string after weight value
            
            max_score = stat_line[:stat_line.find(',')] #second value
            max_scores.append(float(max_score))
            
            stat_line = cut_next_comma(stat_line) #string after max score
            
            my_score = stat_line.strip() #third value
            my_scores.append(float(my_score))
            
            
            
        return (weights, max_scores, my_scores)
    
    
def final_score(grade_file):
    """
    This function calculates a students final_score with a parameter of a text file of their grades
    Inputs: grade_file (text file)
    Return: final score (int)
    """
    
    scores_tupil = read_scores(grade_file)
    
    relative_scores = []
    
    for i in range(len(scores_tupil[0])): #for the amount of assignments in the file
        
        relative_score = scores_tupil[0][i] * (scores_tupil[2][i] / scores_tupil[1][i])
        relative_scores.append(relative_score)
        
    final_score = sum(relative_scores)
    
    return int(final_score + 0.5) #rounded


def letter_grade(score):
    """
    This function returns the letter grade of the input score
    Inputs: score (int)
    Return: letter grade (string)
    """
    
    letter_scale = {'A' : list(range(93, 101)), 'A-' : list(range(90, 93)), 'B+' : list(range(87, 91)), 'B' : list(range(83, 87)),
                    'B-' : list(range(80, 83)), 'C+' : list(range(77, 80)), 'C' : list(range(73, 77)), 'C-' : list(range(70, 73)),
                    'D' : list(range(60, 70)), 'F' : list(range(0,60))}
    
    for k in letter_scale: #for the keys in the letter scale
        if score in letter_scale[k]: #if the score is in the given key's values
            
            return k


