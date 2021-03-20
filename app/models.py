from . import db
class UserProp(db.Model):
    __tablename__= 'user_property'

    id=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    bedroom_num = db.Column(db.String(80))
    bathroom_num = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(255))
    price = db.Column(db.String(80))
    types = db.Column(db.String(80))
    desciption = db.Column(db.String(80))
    filename = db.Column(db.String(500))
    photo= db.Column(db.String(500))

    def __init__(self, title, bedroom_num, bathroom_num, location,price,types,desciption,filename,photo):
        self.title = title
        self.bedroom_num=bedroom_num
        self.bathroom_num=bathroom_num
        self.location=location
        self.price=price
        self.types=types
        self.desciption=desciption
        self.filename=filename
        self.photo=photo
