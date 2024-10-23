# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):
    # place string of personsname into personsinitail string
    personsInitials = ""
    personsInitials.replace("", personsName)
    
    #for loop for uppercase character checking
    for character in personsInitials:
        personsInitials.replace(personsName, personsInitials.find(character.isupper()))
        
    
    #place dot inbetween the initials
    personsInitials.split('.')

    #IDK what this is for or what to do with it
    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name: ')

initials = initials_generator(personsName)

print(initials)
