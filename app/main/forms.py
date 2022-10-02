from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FloatField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Regexp, Optional, Email
from wtforms.fields import DateField
#from ..models import Branch, Employee, Client, Loan
#from ..models import *


class InputWhatIfForm(FlaskForm):
    database = SelectField('Database', choices = [
         ('amazon_product','Amazon Product'),
         ('adult_income','Adult Income'),
    ])
    base_tables = SubmitField('BaseTables',validators=None)

    #USE part
    use_table = SelectField('USE Table', choices=[
        ('product','Product'),
        ('review','Review'),
        ('custom','Custom'),
    ])
    #need to change: to dynamic choices related to datasets
    use = TextAreaField('USE', default="")
    run_relevant = SubmitField('RunRelevantView',validators=None)
    
    #OUTPUT part
    output_type = SelectField('OutputType', choices = [
        ('avg','AVG'),
        ('sum','SUM'),
        ('count','COUNT')
    ])
    # output_attrs = SelectField('OutputAttrs',choices= [
    #     ('post_rtng','POST(Rtng)'),
    #     ('post_brand','POST(Brand)'),
    #     ('post_senti','POST(Senti)'),
    #     ('post_price','POST(Price)')
    # ])
    #dynamic button
    output_attrs = SelectField('OutputAttrs',coerce=str)
    
    #need to change: to dynamic choices when connect to database
    output = TextAreaField('OUTPUT',default = "")
    #output_for = SubmitField('+ FOR')
    #need to add: +FOR function
    
    #UPDATE part
    # update_attrs = SelectField('UpdateAttrs',choices=[
    #     ('rtng','Rtng'),
    #     ('brand','Brand'),
    #     ('senti','Senti'),
    #     ('price','Price')
    # ])
    update_attrs = SelectField('UpdateAttrs', coerce=str)
    #need to change: to dynamic choices when connect to database
    update_const = FloatField('UpdateConst')
    #need to change the constant
    update_sign = SelectField('UpdateSign', choices=[
        ('add','+'),
        ('multiply','x'),
        ('dot','.')
    ])
    #the meaning of "."

    #need to add: PRE(xxx)
    #need to add: +WHEN function
    when = TextAreaField('WHEN', default="")
    
    run = SubmitField('RUN')
