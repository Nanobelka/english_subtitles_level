#!/usr/bin/env python
# coding: utf-8

# ## Imports

# In[2]:


import streamlit as st
import pandas as pd
import numpy as np

import joblib
import pickle
from io import StringIO

import sklearn
from sklearn.base import BaseEstimator, TransformerMixin


# ## Constants

# In[ ]:


PATH_DATA = 'Streamlit/'
CR='\n'

TITLE = 'English Subtitles Level Prediction'

# text styles
class f:
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    END = "\033[0m"


# ## Settings

# In[ ]:


st.set_page_config(
                   page_title=TITLE,
                   page_icon='🎦',
                   initial_sidebar_state='expanded',
                   menu_items={
#                                'Get Help': 'https://....',
#                                'Report a bug': "https://....",
                               'About': 'Written by Sergei Vasiliev. Fell free contact to me in Telegram @nanobelkads.'
                              }
                 )


# ## Functions

# In[ ]:


class TextSelector(BaseEstimator, TransformerMixin):

    def __init__(self, field):
        self.field = field
    def fit(self, X, Y=None):
        return self
    def transform(self, X):
        return X[self.field]


# In[ ]:


# @st.cache_resource
# def load_model():
#     return joblib.load(f'{PATH_DATA}model_dump.mdl')


# In[ ]:


@st.cache_resource
def load_model():
    
    with open(f'{PATH_DATA}model_dump.pcl', 'rb') as file:
        model = pickle.load(file)
        
    return model


# In[ ]:


# @st.cache_data
# def load_data_local(df_name, n_rows=5):
#     df = pd.read_csv(f'{PATH_DATA}{df_name}', nrows=n_rows)
#     return df


# ## Loads

# In[ ]:


# загрузка модели из файла
model = load_model()


# ## Output basic info

# In[ ]:


st.image(f'{PATH_DATA}images/banner.jpg')


# In[ ]:


# заголовок приложения
st.title(TITLE)

# пояснительный текст
st.write('This application will help English learners to determine the level of a movie by subtitles. Just drag your subtitle file into the input field and the incredibly cool artificial intelligence will do it.')


# ## Input and Processing user's data

# In[ ]:


uploaded_file = st.file_uploader('Choose a file with subtitles in english', type=['txt','srt'], label_visibility='collapsed')

if uploaded_file is not None:

    subs_file = StringIO(uploaded_file.getvalue().decode('utf-8'))
    subs_str = subs_file.read()
    # st.write(subs)

    # объединение введенных данных в мини-таблицу (из одной строки)
    data_test = pd.DataFrame(data={'Subtitles':[subs_str],
    #                                'age':[age],
    #                                'active':[active],
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
    
#     st.subheader(f'Level of your subs: :blue[{level}]')
    st.subheader(f'Level of your subs: :{value_color}[{level}]')



    # st.subheader(f'Probability of cardiovascular disease is about :{value_color}[{disease_proba : .1%}]')


# ## Disclamer

# In[ ]:


st.caption('------')
st.caption('**Disclaimer.** "Everything is very simple" (C)')


# ## Final service message

# In[ ]:


st.caption('------')
st.caption('*Service info: NO errors*')


# ## Remarks

# для удаленного запуска приложения из репозитория GitHub:

#     streamlit run https://raw.githubusercontent.com/Nanobelka/Cardiovascular-disease-prediction/main/Cardio_Streamlit.py

# для локального запуска приложения

#     d:  
#     cd DATA/Work_analytics/Jupyter_Notebook/Praktikum_DS/10_english/Streamlit_app  
#     streamlit run english_Streamlit.py  
