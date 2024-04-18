
import numpy as np
import pickle
from catboost import CatBoostClassifier
import streamlit as st

model=pickle.load(open('/home/julius/python folder/Type-2-prediction.pkl','rb'))
#global makeprediction
with open("design.css") as ds:
    st.markdown(f"<style>{ds.read()}</style>", unsafe_allow_html=True)
def main():
    with open('design.css') as f:
        #st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
            


#title of the app
        st.title("Clinical Decision Support System for Prediction of Type 2 Diabetes".upper())
#input setup
    fbs=st.number_input("Blood Sugar level ", value=12,min_value=10)
    weight=st.number_input("Wight (kg)", value=15, min_value=10)
    height=st.number_input("Height (cm)",value=15, min_value=10)
    bmi=(weight/(height*height))*10000
    #st.write(f'Atọka Ibi Ara (BMI): {'{:.2f}'.format(bmi)}')
    st.write(f'BMI: {"{:.1f}".format(bmi)}')
    waist=st.number_input("Waist Circumference",value=15, min_value=10)
    age=st.number_input("Age", value=15, min_value=10)
    gender=st.selectbox("Gender",["M","F "])
    fhd=st.selectbox("Family History of Diabetes",["Y","N "])
    fhh=st.selectbox("Family History of Hypertension",["Y","N "])
    heu=st.selectbox("History of Excess Urine",["Y","N "])
    hew=st.selectbox("History of Excess Water Intake",["Y","N "])
    rex=st.selectbox("Did you do excercise regularly",["Y","N "])
    hef=st.selectbox("History of Excess Food Intake",["Y","N "])
    phd=st.selectbox("Did you have other type of diabetes before",["Y","N "])
#action button
    makeprediction=[]
    if st.button("Predict"):
        makeprediction=model.predict([[fbs,bmi,waist,age,gender,fhd,fhh,heu,hew,rex,hef,phd]])
        result=''
        if makeprediction == 'Y':
            st.success("You either have diabetes or are likely to have it. Please visit the doctor as soon as possible.".upper())  
        else:
                st.success('You do not have Diabetes!'.upper()+' Ensure you eat balance diet and do regular excercise.')
        #st.success(result)
#display of result
    #st.success("Your result shows that you {}".format(makeprediction))

if __name__=='__main__':
  main()
