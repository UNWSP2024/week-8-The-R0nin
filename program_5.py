# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
Course_info = {'ENGL':'ENGL 100: English, ENGL 203: Coversational English, ENGL 137: Creative Writing', 
               'PHYS':'PHYS 100: Physics, PHYS 335: Thermal Physics, PHYS 351: Quantum Theory', 
               'MAT':'MAT 100: Mathamatics, MAT 112: Number Theory, MAT 103: Trigonometry, MAT 200: Combinatorics', 
               'HIST':'HIST 100: History, HIST 101: World History, HIST 304: Government', 
               'CS':'CS 100: Computer Science, CS 131: Computer Organization, CS 184: Cybersecurity', 
               'ART':'ART 100: Drawing, ART 173: Animation, ART 243: Ceramic art, ART 190, Photography'}

def course_search():
    search = input('Search course(Letters in all caps): ')
    if search in Course_info:
        print('the course for the subject are:', Course_info[search])
    else:
        print('error, course not found. Try again', course_search())

course_search()
