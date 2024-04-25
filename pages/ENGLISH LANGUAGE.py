
from PIL import Image
import numpy as np
import pickle
from catboost import CatBoostClassifier
import streamlit as st

model=pickle.load(open('Type-2-prediction.pkl','rb'))
#global makeprediction
with open("design.css") as ds:
    st.markdown(f"<style>{ds.read()}</style>", unsafe_allow_html=True)
def main():
    with open('design.css') as f:
        #st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
            


#title of the app
        st.title("Clinical Decision Support System for Prediction of Type 2 Diabetes".upper())
#input setup
    blood=st.selectbox("Choose a unit for your fasting blood sugar level", ["mmol/L", "mg/dL"])
    if(blood=="mmol/L"):
        bsl=st.number_input("Fasting Blood Sugar level mmol/L")
        fbs=bsl*18.0182
    else:
        fbs=st.number_input("Fasting Blood Sugar level mg/dL", value=12,min_value=10)
    weight=st.number_input("Wight (kg)", value=15, min_value=10)
    height=st.number_input("Height (cm)",value=15, min_value=10)
    bmi=(weight/(height*height))*10000
    #st.write(f'Atọka Ibi Ara (BMI): {'{:.2f}'.format(bmi)}')
    #st.write(f'BMI: {"{:.1f}".format(bmi)}')
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
            st.success("The result shows that you have Type 2 Diabetes. Please visit a medical doctor as soon as possible.")  
        else:
                st.success('The result shows that you do not have Type 2 Diabetes!'+' Ensure you eat balance diet and do regular excercise.')
        #st.success(result)
#display of result
    #st.success("Your result shows that you {}".format(makeprediction))
        bmif="{:.2f}".format(bmi)
        st.caption(":blue[Interpretation of your weight]")
        if(bmi<=18.5):
            st.success("You are underweight with BMI of "+str(bmif)+". Ensure you well and eat balance diet")
        elif(18.5 < bmi <= 24.9):
            st.success("Your weight is normal with BMI of "+str(bmif)+"kg/m^2. Maintain your eating and Excercise habits")
        elif(25 < bmi <= 29.29):
            st.success("You are overweight with BMI of "+str(bmif)+"kg/m^2. Improve on your Excercise")
        elif(30< bmi <= 34.9):
            st.success("You are obese with BMI of "+str(bmif)+"kg/m^2. You are at high risk of diseases like Diabees, Hypertension, etc. Reduce you food intake and do more excercise")
        else:
            st.success("You have severe Obesity with BMI of "+str(bmif)+"kg/m^2. Kindly visit a medical Doctor as soon as possible")
        image1=Image.open('bmib.png')
        st.image(image1, width=500)
if __name__=='__main__':
  main()
