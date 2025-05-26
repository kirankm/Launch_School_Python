class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Wallet):
            return Wallet(self.amount + other.amount)
        return NotImplemented
    
    def __str__(self):
        return f"Wallet with ${self.amount}"


wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet)  