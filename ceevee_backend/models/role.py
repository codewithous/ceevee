from ceevee_backend import db, login_manager

""" Module for users roles"""

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    role_description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "User('{}', '{}', '{}')" \
                .format(self.id, self.name, self.role_description)
