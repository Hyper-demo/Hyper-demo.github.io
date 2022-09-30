from flask import render_template, request, redirect, url_for, make_response, current_app, flash, session
#from .forms import BranchSearchForm, BranchEditForm, ClientEditForm, ClientSearchForm, SavingAccountEditForm, SavingAccountSearchForm,CheckAccountEditForm, CheckAccountSearchForm
from .forms import InputWhatIfForm
# 导入蓝图程序用于构建路由
from . import main
# 导入db用于操作数据库
from .. import db
# 导入实体列 用户操作数据库
#from ..models import *
from flask_login import login_required
from datetime import date
from sqlalchemy import extract
import datetime



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/query_input_what_if', methods=['GET', 'POST'])
def query_input_what_if():
    
    form = InputWhatIfForm()
    
    print(request.form)
    if 'base_tables' in request.form:
        print('base_tables_button')
        print(form.database.data)
        session['database'] = form.database.data
        #print(session.get('database'))
        #add image here
        return render_template('query_input_what_if.html', form=form)
        #base_table = form.database.data
        #need to add: (1) connect to database (2) add casual dependencies graph
    elif 'run_relevant' in request.form:
        print('Run Revelant button')
        #need to add: show table image
    elif 'run' in request.form:
        print('RUN button')
        #run query, show graphs


    if form.is_submitted():
        print("DBG1", form.use.data)
        print('DBG2',form.output.data)
        session['use'] = form.use.data
        redirect('query_input_what_if')
        #redirect(url_for('query_input_what_if'))
        #else:
            #print('wrong')
        #form.use.data = "abcd"
        
    else:
        print('wrong')
    return render_template('query_input_what_if.html', form = form)


@main.route('/query_input_how_to')
def query_input_how_to():
    return render_template('query_input_how_to.html')

#<form method = 'post' action = '/query_input_what_if'>