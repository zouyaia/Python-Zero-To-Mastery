# a package is simply a folder containing modules (.py files)
import shopping.shopping_cart as cart # shopping is a package
import utility # utility is a module

print(utility.div(8, 3))
print(cart.buy("t-shirt"))