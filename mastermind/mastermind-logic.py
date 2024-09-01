import random

class Mastermind:
    def __init__(self, digits):
        self.digits = digits
        top_range = (10 ** digits) -1
        self.number = str(random.randint(0, top_range))
        while len(self.number) < self.digits:
            add_zero = "0" + self.number
            self.number = add_zero

    def correct_digits(self, guess):
        total_right = 0
        for num in guess:
            total_right += self.number.count(num)
        return total_right

    def correct_placement(self, guess):
        total_right = 0
        for num in range(0, self.digits):
            if guess[num] == self.number[num]:
                total_right += 1
        return total_right

    def evaluate_guess(self, guess):
        correct_digits = self.correct_digits(guess)
        correct_placement = self.correct_placement(guess)
        return f"Correct Digits: {correct_digits} \nCorrect Placement: {correct_placement}"




mastermind = Mastermind(4)

print(mastermind.evaluate_guess("1234"))