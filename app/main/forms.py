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

    #groupby query part
    use_table = SelectField('USE Table', choices=[
        ('product','Product'),
        ('review','Review'),
        ('custom','Custom'),
    ])
    #not use now
    use = TextAreaField('USE', default="")
    run_relevant = SubmitField('Run Aggregate Query',validators=None)


    #dropdown menu field for placeholder query
    #OUTPUT part
    output_type = SelectField('OutputType', choices = [
        ('avg','AVG'),
        ('sum','SUM'),
        ('count','COUNT')
    ])
    output_attrs = SelectField('OutputAttrs',choices= [
        ('post_rtng','POST(Rtng)'),
        ('post_brand','POST(Brand)'),
        ('post_senti','POST(Senti)'),
        ('post_price','POST(Price)')
    ])
    #dynamic button
    #output_attrs = SelectField('OutputAttrs',coerce=str)
    
    #UPDATE part
    update_attrs = SelectField('UpdateAttrs',choices=[
        ('rtng','Rtng'),
        ('brand','Brand'),
        ('senti','Senti'),
        ('price','Price')
    ])
    #update_attrs = SelectField('UpdateAttrs', coerce=str)
    update_const = FloatField('UpdateConst')
    update_sign = SelectField('UpdateSign', choices=[
        ('add','+'),
        ('multiply','x'),
        ('dot','.')
    ])
    #the meaning of "."

    for_attrs = SelectField('ForAttrs',choices=[
        ('rtng','Rtng'),
        ('brand','Brand'),
        ('senti','Senti'),
        ('price','Price')
    ])
    for_comp = SelectField('ForComp', choices=[
        ('bigger','>'),
        ('equal','='),
        ('smaller','<'),
        ('bigger_equal','>='),
        ('smaller_equal','<=')
    ])
    for_const = FloatField('ForConst')


    show_attrs = SelectField('ShowAttrs',choices=[
        ('rtng','Rtng'),
        ('brand','Brand'),
        ('senti','Senti'),
        ('price','Price')
    ])
    show_comp = SelectField('ShowComp', choices=[
        ('bigger','>'),
        ('equal','='),
        ('smaller','<'),
        ('bigger_equal','>='),
        ('smaller_equal','<=')
    ])
    show_const = FloatField('ShowConst')



    #need to change: to dynamic choices when connect to database
    output = TextAreaField('OUTPUT',default = "")
    #output_for = SubmitField('+ FOR')
    #need to add: +FOR function
    #need to add: PRE(xxx)
    #need to add: +WHEN function
    when = TextAreaField('WHEN', default="")
    
    run = SubmitField('RUN')
