# Trabajando con variables en python
brand = "catellaTech"
email = "catellatech@gmail.com"
year = 2022

# concatenando variables
print(f"{brand} * {email} - {str(year)}")
print(f"hola como estan? somos {brand}")
# utilizando el metodo format
print(
    "hello our brand is {} and our email is {}, also we created this brand in {}".format(
        brand, email, year
    )
)
