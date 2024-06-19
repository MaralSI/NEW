
# bank.py
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class ExtendedBank(Bank):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, rate):
        if rate < 0:
            raise ValueError("Interest rate cannot be negative")
        self._interest_rate = rate

class MoreExtendedBank(ExtendedBank):
    def __init__(self, name, balance, interest_rate, branch):
        super().__init__(name, balance, interest_rate)
        self._branch = branch

    @property
    def branch(self):
        return self._branch

    @branch.setter
    def branch(self, new_branch):
        self._branch = new_branch
