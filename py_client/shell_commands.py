from products.models import Products
prod_obj = Product.objects.first()
user = prod_obj.user
user_products = user.product_set.all()
user
prod_obj
user_products
