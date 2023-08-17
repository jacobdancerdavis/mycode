#!/usr/bin/env python3

wordbank= ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria','Mohamed', 'PJ', 'Philip', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

num= input("Pick a student number!")
num= int(input("Pick a student number!"))
choice= int(input("Pick a student number!"))
student_name= tlgstudents[choice]

print(student_name, "always uses", wordbank[1], wordbank[2], "to indent.")

