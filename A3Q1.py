import psycopg2
from psycopg2 import sql

# Connect to the database
def connect():
	try:
		connection = psycopg2.connect(
			dbname="A3Q1",
			user="postgres",
			password="p",
			host="localhost",
			port="5432"
		)
		return connection
	except psycopg2.Error as err:
		print("Unable to connect to the database")
		print(err)
		return None

# Display the menu
def menu():
	print("\nMenu:")
	print("1. Retrieves and displays all records from the students table")
	print("2. Inserts a new student record into the students table")
	print("3. Updates the email address for a student with the specified student_id")
	print("4. Deletes the record of the student with the specified student_id")
	print("5. Exit the program")

# Get user menu choise
def getChoice():
	try:
		choice = int(input("Enter your choice: "))
		return choice
	except ValueError:
		print("Invalid input. Please enter a number")
		return -1

# Function to print the table (SELECT * FROM students)
def printTable():
	connection = connect()
	if connection is not None:
		try:
			cur = connection.cursor()
			cur.execute("SELECT * FROM students")
			student_table = cur.fetchall()
			print("Students Table:")
			for row in student_table:
				print(row)
		except psycopg2.Error as err:
			print("ERROR: Could not print student table")
			print(err)
		finally:
			if connection:
				connection.close()

# Add a new student
def addStudent(first_name, last_name, email, enrollment_date):
	connection = connect()
	if connection is not None:
		try:
			cur = connection.cursor()
			cur.execute(
				"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
				(first_name, last_name, email, enrollment_date)
			)
			connection.commit()
			print("Student added")
		except psycopg2.Error as err:
			print("ERROR: Could not add student")
			print(err)
		finally:
			if connection:
				connection.close()

# Edit the selected student's email address
def udpateEmail(student_id, new_email):
	connection = connect()
	if connection is not None:
		try:
			cur = connection.cursor()
			cur.execute(
				"UPDATE students SET email = %s WHERE student_id = %s",
				(new_email, student_id)
			)
			connection.commit()
			print("Email updated")
		except psycopg2.Error as err:
			print("ERROR: Could not update email address")
			print(err)
		finally:
			if connection:
				connection.close()

# Delete selected student record
def deleteStudent(student_id):
	connection = connect()
	if connection is not None:
		try:
			cur = connection.cursor()
			cur.execute(
				"DELETE FROM students WHERE student_id = %s",
				(student_id,)
			)
			connection.commit()
			print("Student deleted")
		except psycopg2.Error as err:
			print("ERROR: Could not delete student")
			print(err)	 
		finally:
			if connection:
				connection.close()

# Main function
def main():
	while True:
		menu()
		choice = getChoice()
		print("")

		if choice == 1:
			printTable()
		elif choice == 2:
			first_name = input("Enter first name: ")
			last_name = input("Enter last name: ")
			email = input("Enter email: ")
			enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
			addStudent(first_name, last_name, email, enrollment_date)
		elif choice == 3:
			student_id = input("Enter student ID: ")
			new_email = input("Enter new email: ")
			udpateEmail(student_id, new_email)
		elif choice == 4:
			student_id = input("Enter student ID: ")
			deleteStudent(student_id)
		elif choice == 5:
			print("Exiting")
			break
		else:
			print("ERROR: Please enter a number between 1 and 5")

if __name__ == "__main__":
	main()