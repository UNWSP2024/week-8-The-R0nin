# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
import random
American_States = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix', 
                   'Arkansas':'Little Rock', 'California':'Sacramento', 'Colorado':'Denver', 
                   'Conneticut':'Hartford', 'Delaware':'Dover', 'Florida':'Tallahassee', 
                   'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise', 'Illinois':'Springfeild', 
                   'Indiana':'Indianapolis', 'Iowa':'Des Moines', 'Kansas':'Topeka', 
                   'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta', 
                   'Maryland':'Annapolis', 'Massachusetts':'Boston', 'Michigan':'Lansing', 
                   'Minnesota':'Saint Paul', 'Mississippi':'Jackson', 'Missouri':'Jefferson City', 
                   'Montana':'Helena', 'Nebraska':'Lincoln', 'Nevada':'Carson City', 
                   'New Hampshire':'Concord', 'New Jersey':'Trenton', 'New Mexico':'Santa Fe', 
                   'New York':'Albany', 'North Carolina':'Raleigh', 'North Dakota':'Bismarck', 
                   'Ohio':'Columbus', 'Oklahoma':'Oklahoma City', 'Oregon':'Salem', 
                   'Pennsyvania':'Harrisburg', 'Rhode Island':'Providence', 'South Carolina':'Columbia', 
                   'South Dakota':'Pierre', 'Tennessee':'Nashville', 'Texas':'Austin', 
                   'Utah':'Salt Lake City', 'Vermont':'Montpelier', 'Virginia':'Richmond', 
                   'Washington':'Olympia', 'West Virginia':'Charleston', 'Wisconsin':'Madison', 
                   'Wyoming':'Cheyenne',}

def state_quiz():
    question = input('What is the capital of', (random.choice(list(American_States.keys()))))
    if question == list(American_States.fromkeys(question)):
        print('correct')
    else:
        print('Incorrect, The Answer is ',{American_States.fromkeys[:'capital']})
    state_quiz()

print(state_quiz())
