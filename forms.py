from flask_wtf import FlaskForm

from wtforms.fields import StringField, PasswordField, DateField, RadioField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, length, equal_to
from flask_wtf.file import FileField



class LoginForm(FlaskForm):
    username = StringField("შეიყვანეთ იუზერნეიმი", validators=[DataRequired()])
    password = PasswordField("შეიყვანეთ პაროლი", validators=[DataRequired()])

    login = SubmitField("შესვლა")





class RegisterForm(FlaskForm):
        username = StringField("შეიყვანე იუზერნეიმი", validators=[DataRequired(message="ეს ველი არის სავალდებულო")], )
        password = PasswordField("შეიყვანე პაროლი", validators=[DataRequired(), length(min=8, max=16,
                                                                                       message="პაროლი უნდა იყოს 8-16 სიმბოლო")])
        repeat_password = PasswordField("გაიმეორე პაროლი", validators=[DataRequired(), equal_to("password",
                                                                                                message="პაროლები უნდა იყოს  ერთნაირი")])

        submit = SubmitField("რეგისტრაცია")


class ProductForm(FlaskForm):
    img = FileField(" აირჩიეთ პროდუქტის ფოტო",validators=[DataRequired()])
    name  = StringField("მიუთითეთ პროდუქტის სახელი", validators=[DataRequired()])
    price = IntegerField("მიუთითეთ პროდუქტის ფასი", validators=[DataRequired()])

    submit = SubmitField("პროდუქტის დამატება")

