from app.extensions import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username')
