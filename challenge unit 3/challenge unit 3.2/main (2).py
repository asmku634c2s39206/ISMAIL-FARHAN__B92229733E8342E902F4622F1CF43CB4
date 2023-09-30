






class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
    

def sort_students(student_list):
  # sort the list of students in desending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
# Syntax - lambda arg:exp  
  return sorted_students


# Example usage:
students = [
  Student("Bharathi","204", 9.1),
  Student("Ismail farhan", "206", 9.2),
  Student("Karthik", "207", 9.3),
  Student("Senthamil surya", "208", 9.4),
  Student("Varun","209", 9.5),
  Student("Veerapandi","210", 9.6),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number,
                                                     student.cgpa))



  