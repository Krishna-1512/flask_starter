from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms.fields import TextField
from wtforms.fields import TextAreaField,SelectField
from wtforms.validators import DataRequired,Email
from flask_wtf.file import FileField,FileRequired,FileAllowed

class PropertyForm(FlaskForm):
    title = TextField('Title', validators=[DataRequired()])
    description=TextAreaField('Description',validators=[DataRequired()])
    bedroom_num = TextField('Number of Bedrooms', validators=[DataRequired()])
    bathroom_num = TextField('Number of Bathrooms', validators=[DataRequired()])
    price=TextField('Price',validators=[DataRequired()])
    types=SelectField("Type", choices=[('House'), ('Apartment')])
    location = TextField('Location', validators=[DataRequired()])
    photo= FileField('Image',validators=[FileRequired(), FileAllowed(['jpg','png'])])

