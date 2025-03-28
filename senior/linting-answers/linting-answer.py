class Stack:
    """
    A custom stack implementation for the linting challenge.
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


class BraceValidator:
    """
    A class to validate braces in a given string of code.
    """
    def __init__(self):
        self.stack = Stack()
        self.brace_pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

    def is_opening_brace(self, char):
        return char in self.brace_pairs.keys()

    def is_closing_brace(self, char):
        return char in self.brace_pairs.values()

    def is_not_a_match(self, opening, closing):
        return self.brace_pairs.get(opening) != closing

    def validate(self, code):
        for char in code:
            if self.is_opening_brace(char):
                self.stack.push(char)
            elif self.is_closing_brace(char):
                top = self.stack.pop()
                if top is None:
                    return f"{char} doesn't have an opening brace"
                if self.is_not_a_match(top, char):
                    return f"{char} has a mismatched opening brace"

        if not self.stack.is_empty():
            return f"{self.stack.pop()} doesn't have a closing brace"

        return True


if __name__ == "__main__":
    # Read the input from linting-input.txt
    input_file = "./questions/linting-input.txt"
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Create an instance of BraceValidator
    validator = BraceValidator()

    # Validate each line of code and print the results
    for i, line in enumerate(lines, start=1):
        line = line.strip()
        if not line or line.startswith("//"):  # Skip empty lines and comments
            continue
        result = validator.validate(line)
        print(f"Line {i}: {result}")
