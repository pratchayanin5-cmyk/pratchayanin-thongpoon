# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 10:05:31 2026

@author: Lab
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#import model
loan_model = pickle.load(open("loan_model.sav",'rb'))
ridingmower_model = pickle.load(open("RidingMowers_model.sav",'rb'))


with st.sidebar:
    selected = option_menu('Classification',['LOAN','RidingMower'])

if(selected == 'RidingMower'):
    st.title('RidingMower Prediction')
    
    #user input
    Income = st.text_input('Income')
    lotsize = st.text_input('lotsize')
   
    
    RidingMower_predict = ''
    
    if st.button('Predict'):
        RidingMower_predict = ridingmower_model.predict([[
            float(Income),
            float(lotsize)
        ]])
        
        if(RidingMower_predict[0]==0):
          RidingMower_predict = 'Non Owner'
        else:
          RidingMower_predict = 'Owner'
    st.success(RidingMower_predict)

   
if(selected == 'LOAN'):
    st.title('Loan Prediction')
    
    #user input
    person_age = st.text_input('person_age')
    person_gender = st.text_input('person_gender')
    person_education = st.text_input('person_education')
    person_income = st.text_input('person_income')
    person_emp_exp = st.text_input('person_emp_exp')
    person_home_ownership = st.text_input('person_home_ownership')
    loan_amnt = st.text_input('loan_amnt')
    loan_intent = st.text_input('loan_intent')
    loan_int_rate = st.text_input('loan_int_rate')
    loan_percent_income = st.text_input('loan_percent_income')
    cb_person_cred_hist_length = st.text_input('cb_person_cred_hist_length')
    credit_score = st.text_input('credit_score')
    previous_loan_defaults_on_file = st.text_input('previous_loan_defaults_on_file')
    
    loan_predict = ''
    
    if st.button('Predict'):
        loan_predict = loan_model.predict([[
            float(person_age),
            float(person_gender),
            float(person_education),
            float(person_income),
            float(person_emp_exp),
            float(person_home_ownership),
            float(loan_amnt),
            float(loan_intent),
            float(loan_int_rate),
            float(loan_percent_income),
            float(cb_person_cred_hist_length),
            float(credit_score),
            float(previous_loan_defaults_on_file)
        ]])
        
        if(loan_predict[0]==0):
          loan_predict = 'Loan Reject'
        else:
          loan_predict = 'Loan Accept'
    st.success(loan_predict)


