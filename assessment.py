"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Answer: The three main design advantages provided by object orientation are: 1. Encapsulation - This means that all the attributes and methods of the
		class object are kept together and cannot be accessed by outside objects. 
		(reference: class notes, http://www.python-course.eu/object_oriented_programming.php)
		2. Abstraction - This means that we do not need to know the details of a method in a class object. Object orientation hides the details
		that are not required.
		3. Polymorphism and Inheritance - Polymorphism means that a class can have many children classes which are interchangeable. Inheritance is the 
		feature that allows us to define a class which modified version of a previously defined class. 




2. What is a class?

Answer: A class is a type of data, for example, file, string, list, etc.. Classes are structured constructs used when you want predicatble 
		data and predictable actions. 

3. What is an instance attribute?

Answer: An instance attribute is a type of attribute set directly on an instance of the class.

4. What is a method?

Answer: A method is a special type of function that is defined inside a class and is accessible only to an instance of the class or its subclasses.

5. What is an instance in object orientation?

Answer: An instance is an object of a class created by calling the class. For example if Tree is a class and cedarwood = Tree(), heer cedarwood is the
instance of the class, Tree.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

Answer: A class attribute is defined within the class and is common for all instances of that class. An instance attribute is defined on the instance
of a class. 
Example -
class Flower(object):
	petal_number = 5

rose = Flower()
rose.color = "red"

Here, petal_number is a class attribute and color is an instance attribute for the instance (rose) of the class (Flower).
"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
	"""Captures first name, last name and address of students."""

	def __init__(self, first_name, last_name, address):
		"""To do on instantiation."""
		self.first_name = first_name
		self.last_name = last_name
		self.address = address


class Question(object):
	"""Captures questions and their correct answers."""

	def __init__(self, question, correct_answer):
		"""To do on instantiation."""
		self.question = question
		self.correct_answer = correct_answer


	def check_answer(self):
		"""Prints question, prompts user for an answer and checks it against the correct answer."""
		print self.question
		user_answer = raw_input('\n >')
		#return true if user answer matches correct answer
		if user_answer == self.correct_answer:
			return True
		else:
			return False	


class Exam(object):
	"""Captures the name of an exam and the questions for that exam."""

	def __init__(self, name):
		"""To do on instantiation."""
		self.name = name
		self.questions = []
		self.answers = []

	def add_question(self, question):
		"""Adds questions to the list of questions and answers to the list of answers."""
		self.questions.append(question.question)
		self.answers.append(question.correct_answer)

	def administer_questions(self):
		"""Administers quesions in an exam returns the user's score as a percentage."""
		score = 0
		#looping over the indices of the list of questions, to print each question 
		#compare each user answer with the list of answers at the same index as the question
		#add a score of 1 for each correct answer
		#calculate percentage of correct answers
		for index in range(len(self.questions)):
			print self.questions[index]
			answer = raw_input(' \n >')
			if answer == self.answers[index]:
				score += 1
		if score == 0:
			return 0.00
		else:
			total_score = float(score)
			percentage = total_score * 100 / (len(self.questions)) 
			return percentage


class StudentExam():
	""" Stores student, exam details and scores for the exam."""

	def __init__(self,student,exam):
		"""To do on instantiation."""
		self.score = None
		self.student = student
		self.exam = exam
	

	def take_test(self):
		"""Administers the questions in an exam and prints a message with the score."""
		self.score = self.exam.administer_questions()
		print "Your score is " + str(self.score)


def example():
	"""Administers the exam to a student and provides the score."""
	#create an exam
	midterm = Exam("midterm")
	#create questions and add it to the exam
	q1 = Question("How do you get all the keys from a dictionary in python?", ".keys()")
	q2 = Question("How do you convert a string to a float in python?", "float(str)")
	q3 = Question("How do you get the length of a list?", "len(list)")
	midterm.add_question(q1)
	midterm.add_question(q2)
	midterm.add_question(q3) 

	#create a student
	student1 = Student("Ann", "Rose", "California Street")

	#create an instance of StudentExam, which allows the exam to be administered for the student
	student1_midterm = StudentExam(student1, midterm)
	student1_midterm.take_test()
	

class Quiz(Exam):
	"""Inherits from the parent class exam but records pass/fail instead of percentage scores."""

	def administer_questions(self):
		"""The parent's administer_questions is modified to return 1 if passed and 0 if failed."""
		percentage = super(Quiz, self).administer_questions()
		
		if percentage >= 50.0:
			return 1
		else:
			return 0


class StudentQuiz(StudentExam):
	"""Allows students to take a quiz and stores the scores received."""
	#uses inheritance, whereby StudentQuiz inherits the methods and attributes from its parent StudentExam
	#since no new attribute is required, it can directly use the parent's methods and attributes

	pass











		
















