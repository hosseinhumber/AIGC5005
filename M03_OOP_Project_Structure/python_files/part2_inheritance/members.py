"""Part 2: inheritance, super(), method overriding and polymorphism.

Run:  python members.py
"""


class Member:
    """A library member who can borrow books."""

    def __init__(self, name, borrow_limit=3):
        self.name = name
        self.borrow_limit = borrow_limit
        self.borrowed = []

    def borrow(self, title):
        if len(self.borrowed) >= self.borrow_limit:
            raise ValueError(f"{self.name} has reached the borrow limit.")
        self.borrowed.append(title)

    def describe(self):
        return f"{self.name}: {len(self.borrowed)}/{self.borrow_limit} books borrowed"


class StaffMember(Member):
    """A staff member gets a higher borrow limit and a department."""

    def __init__(self, name, department, borrow_limit=10):
        super().__init__(name, borrow_limit=borrow_limit)   # reuse Member's setup, do not copy it
        self.department = department

    def describe(self):
        base = super().describe()                            # reuse the parent's answer...
        return f"{base} (staff, {self.department})"          # ...then extend it


if __name__ == "__main__":
    m = Member("Aisha")
    s = StaffMember("Devon", department="IT Services")

    # Polymorphism: one line of code, two classes, two correct results.
    for person in (m, s):
        print(person.describe())

    for _ in range(4):
        s.borrow("A Python book")
    print(s.describe())

    try:
        for _ in range(4):
            m.borrow("A Python book")     # Member's limit is 3, so the 4th borrow raises
    except ValueError as error:
        print(f"Caught: {error}")

    print(isinstance(s, Member))          # True: every StaffMember is a Member
    print(isinstance(m, StaffMember))     # False: not every Member is a StaffMember
