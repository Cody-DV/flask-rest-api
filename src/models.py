from . import db, ma


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    email = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=db.func.now())

    def __repr__(self):
        return(f'<Title: {self.title} Email: {self.email}')


class RequestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'email', 'timestamp')


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

    def __repr__(self):
        return(f'<Title: {self.title}')
