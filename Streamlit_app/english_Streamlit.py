#!/usr/bin/env python
# coding: utf-8

# ## Imports

import streamlit as st
import pandas as pd
import numpy as np

import os
import joblib
import pickle
from io import StringIO

import sklearn
from sklearn.base import BaseEstimator, TransformerMixin


# ## Constants

PATH_DATA_LOCAL = ''
PATH_DATA_REMOTE = 'Streamlit_app/'

TITLE = 'English Movie Level Prediction'

CR='\n'

# text styles
class f:
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    END = "\033[0m"


# ## Settings

st.set_page_config(
                   page_title=TITLE,
                   page_icon='🎦',
                   initial_sidebar_state='expanded',
                   menu_items={
#                                'Get Help': 'https://....',
#                                'Report a bug': "https://....",
                               'About': 'Written by Sergei Vasilev. Fell free contact to me in Telegram @nanobelkads.'
                              }
                 )


# ## Functions

class TextSelector(BaseEstimator, TransformerMixin):

    def __init__(self, field):
        self.field = field
    def fit(self, X, Y=None):
        return self
    def transform(self, X):
        return X[self.field]


# @st.cache_resource
# def load_model():
#     return joblib.load(f'{PATH_DATA}model_dump.mdl')


@st.cache_resource
def load_model():
    
    with open('model_dump.pcl', 'rb') as file:
        model = pickle.load(file)
        
    return model


@st.cache_resource
def load_model(model_name):
    
    file_local = f'{PATH_DATA_LOCAL}{model_name}'
    file_remote = f'{PATH_DATA_REMOTE}{model_name}'
    
    if os.path.isfile(file_local):
        with open(file_local, 'rb') as file:
            model = pickle.load(file)
    else:
        with open(file_remote, 'rb') as file:
            model = pickle.load(file)
        
    return model


@st.cache_data
def image_path(image_name):
    
    file_local = f'{PATH_DATA_LOCAL}{image_name}'
    file_remote = f'{PATH_DATA_REMOTE}{image_name}'
    
    if os.path.isfile(file_local):
        return file_local
    else:
        return file_remote


# ## Loads

# загрузка модели из файла
model = load_model('model_dump.pcl')


# ## Output basic info

# баннер приложения
st.image(image_path('images/banner.jpg'))

# заголовок приложения
# st.title(TITLE)
st.markdown(f'<h1 style="text-align: center;">{TITLE}</h1>', unsafe_allow_html=True)


# ## Input user's data

column_1, column_2 = st.columns(2)

with column_2:
    # поле для ввода файла с субтитрами
    uploaded_file = st.file_uploader('Choose a file with subtitles in english', type=['txt','srt'], label_visibility='collapsed')    

with column_1:
    # пояснительный текст
    description_text_1 = 'This application helps English learners to determine the CEFR-level of a movie by subtitles.'
    description_text_2 = 'Just drag your subtitle file into the input field and the incredibly cool artificial intelligence will do it.'
    st.markdown(f'<h6 style="text-align: right; font-size: 16px;">{description_text_1}</h6>', unsafe_allow_html=True)
    st.markdown(f'<h6 style="text-align: right; font-size: 16px;">{description_text_2}</h6>', unsafe_allow_html=True)


# ## Processing user's data

if uploaded_file is not None:

    subs_str = StringIO(uploaded_file.getvalue().decode('utf-8')).read()

    # объединение введенных данных в мини-таблицу (из одной строки)
    data_test = pd.DataFrame(data={'Subtitles':[subs_str],
    #                                'new_field':[new_field],
                                  }
                            )

    # прогноз для введенных с экрана данных
    data_test['Level'] = model.predict(data_test)
    
    # вывод результата
    level = data_test.loc[0, 'Level']
    
    if level[0] == 'A':
        value_color = 'green'
    elif level[0] == 'B':
        value_color = 'blue'
    elif level[0] == 'C':
        value_color = 'red'
    
    with column_2:
        style = "<h6 style='text-align: center; font-size: 26px;'>"
        style_end = "</h6>"
        text = f"{style}CEFR-level of your subtitles: <span style='color:{value_color};'>{level}</span>{style_end}"
        st.markdown(text, unsafe_allow_html=True)

#         st.subheader(f'CEFR-level of your subtitles: :{value_color}[{level}]')


# ## Disclamer

st.caption('------')
st.caption('**Disclaimer.** "Everything is very simple" (C)')


# ## Final service message

st.caption('------')
st.caption('*Service info: NO errors*')
