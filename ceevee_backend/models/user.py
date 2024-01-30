from ceevee_backend import db, login_manager
from ceevee_backend.models.role import Role

""" User class"""
user_role = db.Table('users_roles', 
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer, db.ForeignKey('role.id')))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    photo = db.Column(db.String(20), nullable=False, default='default.jpg')
    roles = db.relationship("Role", secondary='users_roles', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return "User('{}', '{}', '{}', '{}', '{}')" \
                .format(self.id, self.first_name, self.last_name, 
                        self.email, self.roles)
