from sqladmin import Admin, ModelView
from .sqladmin_models import Cart, Product, User, PurchaseItem, Purchase, Vendor, Category

def create_admin(app, engine):
    admin = Admin(app, engine)

    class CartAdmin(ModelView, model=Cart):
        name = "Cart"
        name_plural = "Carts"
        icon = "fa fa-shopping-cart"
        column_default_sort = [{'cart_id', True}, {'user_id', True}]
        column_searchable_list = ['user_id']
        column_sortable_list = ['cart_id', 'product_id', 'product_vendor_id', 'user_id', 'quantity']
        column_list = ['cart_id', 'product_id', 'product_vendor_id', 'user_id', 'quantity']

    class ProductAdmin(ModelView, model=Product):
        name = "Product"
        name_plural = "Products"
        icon = "fa fa-shopping-bag"
        column_default_sort = [{'product_id', True}, {'vendor_id', True}]
        column_searchable_list = ['product_name']
        column_sortable_list = ['product_id', 'vendor_id', 'category_id', 'product_name', 'product_description', 'product_images_path', 'product_discount', 'product_price', 'product_stock']
        column_list = ['product_id', 'vendor_id', 'category_id', 'product_name', 'product_description', 'product_images_path', 'product_discount', 'product_price', 'product_stock']

    class UserAdmin(ModelView, model=User):
        name = "User"
        name_plural = "Users"
        icon = "fa-solid fa-user"
        column_default_sort = [{'user_id', True}]
        column_searchable_list = ['user_id', 'user_email', 'user_name']
        column_sortable_list = ['user_id', 'user_email', 'user_password', 'user_name', 'user_contact', 'user_address']
        column_list = ['user_id', 'user_email', 'user_password', 'user_name', 'user_contact', 'user_address']

    class PurchaseItemAdmin(ModelView, model=PurchaseItem):
        name = "Purchase Item"
        name_plural = "Purchase Items"
        icon = "fa fa-cart-plus"
        column_default_sort = [{'purchase_item_id', True}]
        column_searchable_list = ['purchase_item_id']
        column_sortable_list = ['purchase_item_id', 'purchase_id', 'product_id', 'quantity']
        column_list = ['purchase_item_id', 'purchase_id', 'product_id', 'quantity']

    class PurchaseAdmin(ModelView, model=Purchase):
        name = "Purchase"
        name_plural = "Purchases"
        icon = "fa fa-cart-arrow-down"
        column_default_sort = [{'purchase_id', True}]
        column_searchable_list = ['purchase_id']
        column_sortable_list = ['purchase_id', 'user_id', 'total_amount', 'purchase_date', 'purchase_status']
        column_list = ['purchase_id', 'user_id', 'total_amount', 'purchase_date', 'purchase_status']

    class VendorAdmin(ModelView, model=Vendor):
        name = "Vendor"
        name_plural = "Vendors"
        icon = "fa fa-industry"
        column_default_sort = [{'vendor_id', True}]
        column_searchable_list = ['vendor_id']
        column_sortable_list = ['vendor_id', 'vendor_name', 'vendor_contact', 'vendor_address']
        column_list = ['vendor_id', 'vendor_name', 'vendor_contact', 'vendor_address']

    class CategoryAdmin(ModelView, model=Category):
        name = "Category"
        name_plural = "Categories"
        icon = "fa fa-tag"
        column_default_sort = [{'category_id', True}]
        column_searchable_list = ['category_name']
        column_sortable_list = ['category_id', 'category_name']
        column_list = ['category_id', 'category_name']

    admin.add_view(CartAdmin)
    admin.add_view(ProductAdmin)
    admin.add_view(UserAdmin)
    admin.add_view(PurchaseItemAdmin)
    admin.add_view(PurchaseAdmin)
    admin.add_view(VendorAdmin)
    admin.add_view(CategoryAdmin)