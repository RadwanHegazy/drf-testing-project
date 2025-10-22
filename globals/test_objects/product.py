from product.models import Product, Category
from .users import create_user


def create_category(
    name = 'Default Category'
) :
    return Category.objects.create(name=name)


def create_product(
    created_by = None,
    title = 'Default Product',
    body = 'This is a default product description.',
    price = 10.0,
    category = None,
    quantity = 5
) :
    return Product.objects.create(
        created_by = created_by or create_user(),
        title = title,
        body = body,
        price = price,
        category = category or create_category(),
        quantity = quantity
)