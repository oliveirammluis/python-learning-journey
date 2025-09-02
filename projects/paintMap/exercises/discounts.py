"""
Discounts

You would like to determine the final price of the three games — “Mario Kart”, “Legend of Zelda”, and “Animal Crossing” — but with some discounts applied. Your starting code contains two variables that assign a small or a big discount — 10% or 50%.

Apply the small discount to the “Mario Kart” game and the big discount to “Animal Crossing”. The “Zelda” game doesn’t have any discounts. You can create as many variables as you wish to help you, but you must not change the values of smallDiscount or bigDiscount.

Calculate the final price for all three games and assign the value of this calculation to finalPrice. Then print the value of finalPrice.

Hint 1: In math, 10% and 50% can be represented by 0.1 and 0.5. This is how percentages in calculations are also used in JavaScript.
Hint 2: Think carefully about how to correctly calculate the price after applying a discount. There is no problem in googling how to do this. In programming, it’s often helpful to search for information to learn new concepts and techniques.

"""

marioKart = int(input("Enter the price of Mario Kart: "))
zelda = int(input("Enter the price of Legend of Zelda: "))
animalCrossing = int(input("Enter the price of Animal Crossing: "))

smallDiscount = 0.1
bigDiscount = 0.5

marioKartAfterDiscount = (marioKart - (marioKart * smallDiscount))
animalCrossingAfterDiscount = (animalCrossing - (animalCrossing * bigDiscount))
finalPrice = marioKartAfterDiscount + zelda + animalCrossingAfterDiscount

print("\n--- Prices after discounts ---")
print(f"Mario Kart After Discount: {marioKartAfterDiscount}")
print(f"Animal Crossing After Discount: {animalCrossingAfterDiscount}")

print(f"\nFinal price of the 3 games is: {finalPrice}")