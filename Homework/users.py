
# users.py
from bank import MoreExtendedBank

bank_instance = MoreExtendedBank("Test Bank", 1000, 5, "Downtown")

# Изменяем значения через property
bank_instance.interest_rate = 7
bank_instance.branch = "Uptown"

