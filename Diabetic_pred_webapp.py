# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 18:17:23 2024

@author: bharu
"""

import pickle
import numpy as np
import streamlit as st
load_m=pickle.load(open('C:/Users/bharu/train_model.sav','rb'))
def prediction(input_d):
    
    x=np.asarray(input_d)
    nx=x.reshape(1,-1)
    npred=load_m.predict(nx)
    if npred[0]==1:
        return 'Diabetic'
    else:
        return 'Not Diabetic'
def main():
    st.title('Diabetic prediction app')
    preg=st.text_input('no of Pregnencies')
    gluc=st.text_input('amount of glucose')
    bp=st.text_input('amount of bp')
    skin_thick=st.text_input('skin thickness')
    insulin=st.text_input('amount of insulin')
    bmi=st.text_input('amount of bmi')
    dpf=st.text_input('amount of dpf')
    age=st.text_input('age value')
    diag=""
    if st.button('Diabetes test Result'):
        diag=prediction([preg,gluc,bp,skin_thick,insulin,bmi,dpf,age])
    st.success(diag)
if __name__=='__main__':
    main()
    