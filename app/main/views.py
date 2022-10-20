from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
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
    # if form.use_table.data == 'product':
    #     query = 'SELECT * FROM amazon_product'
    # elif form.use_table.data == 'review':
    #     query = 'SELECT * FROM amazon_review'
    # else:
    query = form.use.data
    print('query',query)
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

def get_bar_plot(attr_x,attr_y,attr_list, items):

    df = pd.DataFrame(columns = attr_list,data=items)
    print(df)
    print(attr_x)
    print(attr_y)
    #plt.plot()
    plt.figure(figsize=(8,4))
    ax = sns.barplot(x=attr_x, y=attr_y,
                    data=df,
                    palette='Set2',
                    errwidth=0)
    #plt.xlabel('AVG(Rtng)')
    # plt.xlabel("Type")
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig('app/static/bar_graph.jpg', dpi=500)
    #fig.show()


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

    #now it means run the aggregate query and plot
    elif 'run_relevant' in request.form:
        print('RUN Agg query')
        attr_list, items = get_relevant_table(form)
        #get_bar_plot(attr_x,attr_y, attr_list, items)
        if attr_list:
            form.output_attrs.choices = [(attr,"POST(" +str(attr)+")") for attr in attr_list]
            form.update_attrs.choices = [(attr,"POST(" +str(attr)+")") for attr in attr_list]
        session['attr_list']=attr_list
        session['items'] = items
        session['default_plot'] = True #when run the aggregate query, generate a default bar plot(automatically choose the)
        
        #return render_template('query_input_what_if.html', form=form,
        #    causal_graph=casual_graph,attr_list = attr_list, items = items, len_item = len(attr_list))
  
    elif 'run' in request.form:
        print('RUN button')
        session['final_run'] = True
        attr_list = session['attr_list']
        items = session['items']
        #generate default_plot
        # attr_x = form.update_attrs.data
        # attr_y = form.output_attrs.data
        # get_bar_plot(attr_x,attr_y,attr_list, items)
        #need to add API

    if form.is_submitted():
        casual_graph = session.get("causal_graph", None)

        attr_list = session.get('attr_list', None)
        items = session.get('items', None)
        default_plot = session.get('items', None)
        
        final_run = session.get('final_run',None)
        return render_template('query_input_what_if.html', form = form,
            causal_graph=casual_graph, attr_list = attr_list, items = items, len_item = len(attr_list), default_plot = default_plot,final_run=final_run)
    else:
        print('wrong')
        return render_template('query_input_what_if.html', form = form)
    

@main.route('/query_input_how_to')
def query_input_how_to():
    return render_template('query_input_how_to.html')

#<form method = 'post' action = '/query_input_what_if'>