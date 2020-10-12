# Mariele Ponticiello
# CSCI 687
# Project 1
# 11 October 2020

# read in file from command line
import sys

numArg = len(sys.argv)
if numArg < 2:
    print('Insufficient arguments.')
elif numArg == 2:
    commands = sys.argv[1]
    array_size = 100
elif numArg == 3:
    commands = sys.argv[2]
    array_size = int(sys.argv[1])
else:
    print('Too many arguments.')

# Array of DNA and RNA sequences. 
sequence_array = []

# create element array (list) of DNA/RNA sequences. Fill with empty lists. 
# Empty list is represented by 'null' in DNA/RNA string and 'z' in DNA/RNA sequence list
for i in range(0, array_size):
    sequence_array += [['null', ['z']]]

def insert(pos, type, sequence_to_insert):
    if pos < 0 or pos >= len(sequence_array):
        print(f'The position indicated is out of the sequence range.')
    else:
        myType = type
        # if sequence contains only appropriate letters for its type)
        correctLetters = False 
        if type == 'DNA':
            # loop through each char in sequence 
            for char in sequence_to_insert:
                currentValue = char.upper()
                if currentValue == 'A' or currentValue == 'C' or currentValue == 'G' or currentValue == 'T':
                    correctLetters = True
        if type == 'RNA':
            for char in sequence_to_insert:
                currentValue = char.upper()
                if currentValue == 'A' or currentValue == 'C' or currentValue == 'G' or currentValue == 'U':
                    correctLetters = True
        if(correctLetters):
            sequence_array[pos] = [myType, sequence_to_insert]
            print(sequence_to_insert, ' has been inserted at position ', pos)

def print_seq():
    print('Complete list of current DNA and RNA sequences: ')
    for index, value in enumerate(sequence_array):   
        if (value[0] != 'null'):
            print(f'{index}:{value[1]}')

def print_at_pos(pos):
    if pos < 0 or pos >= len(sequence_array):
        print(f'The position indicated is out of the sequence range.')
    else:
        if (sequence_array[pos][0] != 'null'):
            print(f'{pos}: {sequence_array[pos][1]}')
        else:
            print(f'There is no sequence to print at position {pos}.')

def remove(pos):
    if pos < 0 or pos >= len(sequence_array):
        print(f'The position indicated is out of the sequence range.')
    elif sequence_array[pos] != ['null', ['z']]:    
        sequence_array[pos] = ['null', ['z']]
        print('The sequence at postition ', pos, ' has been removed.')
    else:
        print(f'There is no sequence to remove at position {pos}.')

def copy(pos1, pos2):
    size = len(sequence_array)
    if pos1 < 0 or pos1 >= size or pos2 < 0 or pos2 >= size:
        print(f'The position indicated is out of the sequence range.')
    elif sequence_array[pos1] != ['null', ['z']]:
        sequence_array[pos2] = sequence_array[pos1]
        print(f'Sequence at position {pos1} has been copied to position {pos2}')
    else:
        print('No sequence found to be copied at position ', pos1)

def swap(pos1, start1, pos2, start2):
    size1 = len(sequence_array[pos1][1])
    size2 = len(sequence_array[pos2][1])
    # check for start1 and start2 between 0 and length of string
    if start1 < 0 or start1 > size2 or start2 < 0 or start2 > size1:
        print(f'The positions are out of range of the lengths of the strings.')
    else:
        n = len(sequence_array)
        # check for pos1, pos2 within the range of sequence_array that contains elements
        if 0 <= pos1 <= n and 0 <= pos2 <= n:
            # check neither sequence slot null
                if sequence_array[pos1][0] == 'null': 
                    print(f'There is no sequence to be swapped at {pos1}.')
                elif sequence_array[pos2][0] == 'null':
                    print(f'There is no sequence to be swapped at {pos2}.')
                # check both same type
                else:
                    if sequence_array[pos1][0] != sequence_array[pos2][0]:
                        print(f'Unable to swap sequences at {pos1} and {pos2}. The sequences to be swapped must be the same types.')
                    else: 
                        string1 = sequence_array[pos1][1]
                        string2 = sequence_array[pos2][1]
                        tail1 = sequence_array[pos1][start1:]
                        tail2 = sequence_array[pos2][start2:]
                        string1 = sequence_array[pos1][:len(string1)-start1-1]
                        string2 = sequence_array[pos2][:len(string2)-start2-1]
                        sequence_array[pos1][1] = string2 + tail1
                        sequence_array[pos2][1] = string1 + tail2
                        print(f'The sequences at postions {pos1} and {pos2} have been swapped.')
        else:
            if 0 <= pos1 <= n:
                print(f'{pos2} is outside the range of the sequence array.')
            else:
                print(f'{pos1} is outside the range of the sequence array.')

def transcribe(pos):
    if pos < 0 or pos >= len(sequence_array):
        print(f'The position indicated is out of the sequence range.')
    elif (sequence_array[pos][0] != 'DNA'):
        print('Transcription may only be implemented on a DNA sequence.')
    else:
        sequence_array[pos][0] = 'RNA'
        # RNA: A, C, G, U
        # T -> U, A <-> U, C <-> G
        # reverse sequence
        DNAseq = sequence_array[pos][1].upper() # this is a list of char
        char_list = []
        for i in range(0, len(DNAseq)):
            char_list += transcription(DNAseq[i])
        transcribed_RNA = ''
        char_list = char_list[::-1]
        for char in char_list:
            transcribed_RNA += char
        sequence_array[pos][1] = transcribed_RNA
        print(f'Transcription complete on sequence at position {pos}')

def transcription(x):
    return {
        'T': 'U',
        'A': 'U',
        'U': 'A',
        'C': 'G',
        'G': 'C'
    }[x]

command_list = []
try:
    input_file = open(commands, 'r')
    for line in input_file:
        # each element of command_list is an instruction line
        command_list.append(line.split()) 

    input_file.close()
except IOError:
    print('File not found.')

for i in range(len(command_list)):
    instr = command_list[i][0]
    if instr == 'insert':
        insert(int(command_list[i][1]), command_list[i][2], command_list[i][3])
    elif instr == 'print': 
        if len(command_list[i]) == 1:
            print_seq()
        elif len(command_list[i]) == 2:
            print_at_pos(int(command_list[i][1]))
    elif instr == 'remove': 
        remove(int(command_list[i][1]))
    elif instr == 'copy': 
        copy(int(command_list[i][1]), int(command_list[i][2]))
    elif instr == 'swap': 
        swap(int(command_list[i][1]), int(command_list[i][2]), int(command_list[i][3]), int(command_list[i][4]))
    elif instr == 'transcribe': 
        transcribe(int(command_list[i][1]))
    