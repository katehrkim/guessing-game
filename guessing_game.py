class GuessingGame():

    def __init__(self, answer):
        self.answer = answer
        self.last = False

    def guess(self, user_guess):
        if user_guess > self.answer:
            return "high"
        elif user_guess < self.answer:
            return "low"
        else:
            self.last = True
            return "correct" 

    def solved(self):
        return self.last
