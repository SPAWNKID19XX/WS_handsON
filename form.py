from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import EmailField, BooleanField
from wtforms.validators import DataRequired


class FormContact(FlaskForm):

    full_name = StringField(
        'Full Name',
        validators=[DataRequired()],
        render_kw={
            "nome": "full_name",
            "placeholder": "Nome completo",
            'class': 'form-control'
        }
    )

    email = EmailField(
        'WhatsApp',
        validators=[DataRequired()],
        render_kw={
            "nome": "Email",
            "placeholder": "Email",
            'class': 'form-control'
        }
    )


    contact = StringField(
        'WhatsApp',
        validators=[DataRequired()],
        render_kw={
            "nome": "wtsapp",
            "placeholder": "WhatsApp",
            'class': 'form-control'
        }
    )

    ACCEPT_TERMS = BooleanField(
        'Aceita os termos de uso e condições',
        validators=[DataRequired(message="Você deve aceitar os termos de uso e condições.")],
        render_kw={'class': 'form-check-input'}
    )

    submit = SubmitField(
        'Inscreve-te já',
        render_kw={
            'class': 'btn btn_firs_form btn-success my_custom_button'
        }
    )