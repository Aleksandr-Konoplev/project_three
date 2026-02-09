from catalog.models import Product


class ProductService:
    @staticmethod
    def selected_category(category_id):
        return Product.objects.filter(category_id=category_id)
