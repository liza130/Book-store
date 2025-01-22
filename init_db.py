from ext import app, db
from models import Product, User
from routes import create_product

with app.app_context():

    db.drop_all()
    db.create_all()

    admin_user = User(username="admin", password="adminpass", role="Admin")
    admin_user.create()

    product1=Product(name="შაგრენის ტყავი",price="17.95",img="1.jpg")
    product1.create()

    product1 = Product(name="სამი მუშკეტერი", price="17.95", img="#4.2.jpg")
    product1.create()

    product1 = Product(name="ჰამლეტი", price="17.95", img="#5.jpg")
    product1.create()
    product1 = Product(name="80 000 კილომეტრი წყალქვეშ", price="17.95", img="#6.jpg")
    product1.create()
    product1 = Product(name="დორიან გრეის პორტრეტი", price="17.95", img="#8.png")
    product1.create()
    product1 = Product(name="ილია ჭავჭავაძე-მოთხრობები", price="17.95", img="#40.png")
    product1.create()
    product1 = Product(name="ფორსაიტების საგა", price="17.95", img="#44.jpg")
    product1.create()
    product1 = Product(name="მისის დოლოვეი", price="17.95", img="#46.jpg")
    product1.create()