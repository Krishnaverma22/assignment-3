SID = int(input("Enter your SID:"))
Name = str(input("Enter your name here:"))
Department_Name = str(input("Enter your department name here:"))
CGPA = float(input("Enter your CGPA here:"))

if str(SID).startswith("2110"):
    SID = str(SID)[:8]
else:
    print("Invalid SID")

try:
    CGPA = float(CGPA)
    if 0 <= CGPA <= 10:
        CGPA = round(CGPA, 2)
    else:
        print("Invalid CGPA")
except ValueError:
    print("Invalid CGPA")

print("Hey,", Name, "Here!")
print("My SID is", SID)
print("I am from", Department_Name, "department and my CGPA is", CGPA)
