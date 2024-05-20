from pyexpat import model
import numpy as np
import pickle
from catboost import CatBoostClassifier
import streamlit as st
from PIL import Image
st.title(" Ẹrọ Ayẹwo fun Aisan ito suga iru Keji".upper())
model=pickle.load(open('Type-2-prediction.pkl','rb'))
with open("design.css") as ds:
    st.markdown(f"<style>{ds.read()}</style>", unsafe_allow_html=True)
def main():
    gender=''
    fhd=''
    fhd=''
    fhh=''
    heu=''
    hew=''
    rex=''
    hef=''
    phd=''
    blood=st.selectbox("Yan ipin kan fun ipele suga ninu ẹjẹ", ["mmol/L", "mg/dL"])
    if(blood=="mmol/L"):
        bsl=st.number_input("Ipele suga ninu ẹjẹ (mmol/L)")
        fbs=bsl*18.0182
    else:
        fbs=st.number_input("Ipele suga ninu ẹjẹ (mg/dL)", value=12,min_value=10)
    #fbs=st.number_input("Iwọn suga ninu ẹjẹ (Fasting Blood sugar)".upper(),value=15, min_value=10)
    weight=st.number_input("Iwọn (kg)", value=15, min_value=10)
    height=st.number_input("Giga (cm)",value=15, min_value=10)
    bmi=(weight/(height*height))*10000

    #st.write(f'Atọka Ibi Ara (BMI): {"{:.1f}".format(bmi)}')
    waisty=st.number_input("Ayika ẹgbẹ-ikun".upper(),value=15, min_value=10)
    waist=waisty
    agey=st.number_input("Ọjọ ori".upper(),value=15, min_value=10)
    age=agey
    gendery=st.selectbox("iwa (ọkunrin tabi obinrin?)".upper(),("ọkunrin","obinrin"))
    if(gendery=="ọkunrin"):
        gender='M'
    else:
         gender='F'
    fhdy=st.selectbox("Itan idile nipa aisan ito suga (Bẹẹni tabi Bẹẹkọ ?)".upper(),("Bẹẹni","Bẹẹkọ"))
    if(fhdy=='Bẹẹni'):
      fhd='Y'
    else:
      fhd='N' 
    fhhy=st.selectbox("Itan idile nipa Arun Ẹjẹ riru (Bẹẹni tabi Bẹẹkọ ?)".upper(),("Bẹẹni","Bẹẹkọ"))
    if(fhhy=='Bẹẹni'):
      fhh='Y'
    else:
      fhh='N' 
    
    heuy=st.selectbox("Itan ti ito loorekoore (Bẹẹni tabi Bẹẹkọ ?)".upper(),("Bẹẹni","Bẹẹkọ"))
    if(heuy=='Bẹẹni'):
      heu='Y'
    else:
      heu='N' 
    hewy=st.selectbox("Itan-akọọlẹ mimu omi loorekoore (Bẹẹni tabi Bẹẹkọ ?)".upper(),("Bẹẹni","Bẹẹkọ"))
    if(hewy=='Bẹẹni'):
      hew='Y'
    else:
      hew='N' 
    regexcercisey=st.selectbox("Ṣe o ṣe ere idaraya nigbagbogbo? (Bẹẹni tabi Bẹẹkọ ?)".upper(),("Bẹẹni","Bẹẹkọ"))
    if(regexcercisey=='Bẹẹni'):
      rex='Y'
    else:
      rex='N' 
    hefy=st.selectbox("Itan-akọọlẹ ti jijẹ ounjẹ ju bi o ṣe yẹ lọ (Bẹẹni tabi Bẹẹkọ ?)".upper(),("Bẹẹni","Bẹẹkọ"))
    if(fhdy=='Bẹẹni'):
      hef='Y'
    else:
      hef='N' 
    phdy=st.selectbox("Njẹ o ni iru arun Aisan ito suga miiran ṣaaju akoko yii (Bẹẹni tabi Bẹẹkọ ?)".upper(),("Bẹẹni","Bẹẹkọ"))
    if(phdy=='Bẹẹni'):
      phd='Y'
    else:
      phd='N' 
    makeprediction=[]
    if st.button("Ṣayẹwo"): 
        makeprediction=model.predict([[fbs,bmi,waist,age,gender,fhd,fhh,heu,hew,rex,hef,phd]])
#    result=''
        if makeprediction == 'Y':
            st.success("AISAN ITO SUGA WA LARA RE, YARA LO RI DOKITA ONISEGUN OYINBO NI KIAKIA".upper())
        else:
            st.success("O ko ni AISAN ITO SUGA, ṣugbọn rii daju pe o jẹ ounjẹ iwontunwonsi".upper())
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
