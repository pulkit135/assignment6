

#Q1
def divisors(num):
    sum=0
    for number in range(1,num):
        if num%number==0:       #checking for divisor
            sum+=number
    if sum==num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")

divisors(int(input("Enter a number")))

#Q2
def reverse(word):
    word=word.lower()
    word=word.replace(" ","")
    rev_word=""
    for letter in range(len(word)):         #formation of reverse word
        rev_word+=word[len(word)-1-letter]
    if rev_word==word:
        print("Palindrome")
    else:
        print("Not a palindrome")

reverse(input("enter a word"))


#Q3
n = int(input("Enter the number of rows"))

# iterarte upto n
for i in range(n):
    # adjust space
    print(' ' * (n - i), end='')

    # compute power of 11
    print(' '.join(map(str, str(11 ** i))))



#Q4
import string
alphabet_string=string.ascii_lowercase
alphabet_list=list(alphabet_string)     #print the letters in list form
def pangram(word):
    word=word.lower()
    c=0
    for letter in alphabet_list:
        if letter in word:
            c+=1
    if c==26:
        print("Pangram")
    else:
        print("Not a pangram")


pangram(input("Enter a word"))



#Q5
def sorting():
    sequence=input("Enter a set of words")
    seq_list=sequence.split('-')
    seq_list.sort()         #sorts the sequence of words
    print('-'.join(seq_list))

sorting()




#Q6
def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")

    if 'student_name' and 'student_class' in kwargs:
        print(f"\nStudent Name:  {kwargs['student_name']}")
        print(f"Student Class:  {kwargs['student_class']}")


student_data(student_id='21107094', student_name='Pulkit Dembla')

student_data(student_id='21107094', student_name='Pulkit Dembla', student_class='XIII')



#Q7
class Student:
    pass

class Marks:
    pass

student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))



#Q8
def triplets(array):
    found=False
    for i in range(0,len(array)-2):
        for j in range(i+1,len(array)-1):
            for k in range(j+1,len(array)):
                if array[i]+array[j]+array[k]==0:
                    print(array[i],array[j],array[k])
                    found=True

    if found==False:      #if condition turns false it stops searching for triplets
        print("Triplets do not exist")

triplets([-25, -10, -7, -3, 2, 4, 8, 10])



#Q9
class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))






