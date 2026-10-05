"""Part 1: class attributes (shared) versus instance attributes (per object).

Run:  python class_attributes.py
"""


class Book:
    library_name = "Humber Learning Commons"   # class attribute: shared by every instance
    total_books = 0                             # a shared counter

    def __init__(self, title, copies=1):
        self.title = title
        self.copies = copies
        Book.total_books += 1                   # update the CLASS attribute through the class name


b1 = Book("Fluent Python")
b2 = Book("Clean Code")

print(Book.total_books)                          # 2
print(b1.library_name, "|", b2.library_name)     # both read the shared class attribute

# Assigning through an instance creates a NEW instance attribute on b1 only.
# It shadows the class attribute for b1; b2 and the class itself are unchanged.
b1.library_name = "North Campus Library"
print(b1.library_name, "|", b2.library_name, "|", Book.library_name)


# --- The mutable class attribute trap ------------------------------------------
class BadStudent:
    courses = []                    # ONE list, shared by every BadStudent

    def enrol(self, course):
        self.courses.append(course)


class GoodStudent:
    def __init__(self):
        self.courses = []           # a NEW list for each student

    def enrol(self, course):
        self.courses.append(course)


a, b = BadStudent(), BadStudent()
a.enrol("AIGC 5005")
print("BadStudent b.courses :", b.courses, " <- b never enrolled, but sees a's course")

c, d = GoodStudent(), GoodStudent()
c.enrol("AIGC 5005")
print("GoodStudent d.courses:", d.courses, " <- independent, as intended")
