"""A small module to practise testing on."""


def letter(mark: float) -> str:
    """Return the letter grade for a mark from 0 to 100."""
    if not 0 <= mark <= 100:
        raise ValueError(f"A mark must be from 0 to 100, not {mark}.")
    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    return "F"


def average(marks: list[float]) -> float:
    """Return the mean of a non-empty list of marks, rounded to one decimal place."""
    if not marks:
        raise ValueError("Cannot average an empty list of marks.")
    return round(sum(marks) / len(marks), 1)
