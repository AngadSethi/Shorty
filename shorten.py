from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField

class ShortenForm(Form):
    text = StringField('Text', [validators.DataRequired()])
    num_sentences = IntegerField('Number of Sentences', [validators.NumberRange(3, 50)])