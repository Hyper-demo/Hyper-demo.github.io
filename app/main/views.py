from flask import render_template, request, redirect, url_for, make_response, current_app, flash, session
from .forms import InputWhatIfForm

from . import main

from .. import db

from ..models import Product, Review
from flask_login import login_required
from datetime import date
from sqlalchemy import extract
import datetime
import sqlite3

def get_relevant_table(form):
    conn = sqlite3.connect('data-dev.sqlite')
    #print(form.use_table.data)
    if form.use_table.data == 'product':
        query = 'SELECT * FROM amazon_product'
    elif form.use_table.data == 'review':
        query = 'SELECT * FROM amazon_review'
    else:
        query = form.use.data
    #print('query',query)
    cursor = conn.execute(query)
    attributes = cursor.description
    if attributes:
        attr_list = []
        for attr in attributes:
            attr_list.append(attr[0])

        items = cursor.fetchall()
    else:
        attr_list = None
        items = None
    conn.close()
    return attr_list,items


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/query_input_what_if', methods=['GET', 'POST'])
def query_input_what_if():

    form = InputWhatIfForm()
    print(request.form)

    casual_graph = False

    if 'base_tables' in request.form:
        print('base_tables_button')
        print(form.database.data)
        session['daimagetabase'] = form.database.data
        #generate  API
        session['causal_graph'] = True
        casual_graph = True
        #return render_template('query_input_what_if.html', form=form, causal_graph = casual_graph)


    elif 'run_relevant' in request.form:
        print('Run Revelant button')
        attr_list, items = get_relevant_table(form)
        if attr_list:
            form.output_attrs.choices = [(attr,"POST(" +str(attr)+")") for attr in attr_list]
            form.update_attrs.choices = [(attr,"POST(" +str(attr)+")") for attr in attr_list]
        session['attr_list']=attr_list
        session['items'] = items
        
        #return render_template('query_input_what_if.html', form=form,
        #    causal_graph=casual_graph,attr_list = attr_list, items = items, len_item = len(attr_list))
  
    elif 'run' in request.form:
        print('RUN button')
        session['final_run'] = True
        #need to add API

    if form.is_submitted():
        casual_graph = session.get("causal_graph", None)
        attr_list = session.get('attr_list', None)
        items = session.get('items', None)
        final_run = session.get('final_run',None)
        return render_template('query_input_what_if.html', form = form,
            causal_graph=casual_graph, attr_list = attr_list, items = items, len_item = len(attr_list), final_run=final_run)
    else:
        print('wrong')
        return render_template('query_input_what_if.html', form = form)
    

@main.route('/query_input_how_to')
def query_input_how_to():
    return render_template('query_input_how_to.html')

#<form method = 'post' action = '/query_input_what_if'>