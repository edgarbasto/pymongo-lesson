import datetime

class FestaForm(Form):
    dia = datetime.date
    titulo = StringField('Artist')
    #comes = [('Carne', 'Carne'), ('Morcelas', 'Morcelas')]
    #comes_base = SelectField('Comida', choices=comes)

