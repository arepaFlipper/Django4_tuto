from products.models import Product

Product.objects.create(title="Hello world", content="this is amazing!", price=0.00)
Product.objects.create(title="Hello world again", content="this is amazing!", price=12.00)
# get random products
Product.objects.all().order_by("?").first()
Product.objects.all().order_by("?").first()
Product.objects.all().order_by("?").first()
Product.objects.all().order_by("?").first()
Product.objects.all().order_by("?").first()
