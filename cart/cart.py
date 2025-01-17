

class Cart:

    def __init__(self, request):
        self.session = request.session

        cart = self.session.get("session_key")

        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        self.cart = cart
        
    def add(self, product, quantity):
        # Check if the product is already in the cart
        if str(product.pk) in self.cart:
            self.cart[str(product.pk)]["quantity"] += int(quantity)
        else:
            self.cart[str(product.pk)] = {"id": product.pk, "name": product.name, "quantity": int(quantity)}
        
        self.session.modified = True
        
    def remove(self, product):
        # Remove the product from the cart
        if str(product.pk) in self.cart:
           del self.cart[str(product.pk)]
           
        self.session.modified = True