A = float(input("Enter the first number: "))
B = float(input("Enter the second number: "))
C = float(input("Enter the third number: "))

print("First number:", A)
print("Second number:", B)
print("Third number:", C)

if A > B and A > C:
    greatest = A
elif B > A and B > C:
    greatest = B
elif C > A and C > B:
    greatest = C
elif A == B == C:
    greatest = A
elif A == B and A > C:
    greatest = A
elif A == C and A > B:
    greatest = A
elif B == C and B > A:
    greatest = B
else:
    print("Code Blast!!")

print("The greatest of the three numbers is:", greatest)
