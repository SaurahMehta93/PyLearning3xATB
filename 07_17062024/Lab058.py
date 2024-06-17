def make_pizza(*topping):
    for t in topping:
        print(f"Adding {t}.")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
make_pizza('Olvies', 'anchovies', 'pineaple')
