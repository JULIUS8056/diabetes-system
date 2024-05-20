import streamlit as st
#st.title("WELCOME TO TYPE-2-DIABETES PREDICTION SYSTEM")
#def cred_entered():
 #    if st.session_state["usern"].strip()=="admin" and st.session_state["psword"].strip()=="julius":
  #      st.session_state["authenticated"]=True
   #  else:
    #    st.session_state["authenticated"]=False
     #   st.error("Invalid Username/Password")

#def acct():
 #   if "authenticate"  not in st.session_state:
  #          username=st.text_input("Enter your Username", key="usern", on_change=cred_entered)
   #         password=st.text_input("Enter your Password", type='password', key="psword", on_change=cred_entered)
    #        return False
    #else:
     #    if st.session_state["authenticate"]:
      #        return True
       #  else:
        #   username=st.text_input("Enter your Username", key="usern", on_change=cred_entered)
         #  password=st.text_input("Enter your Password", type='password', key="psword", on_change=cred_entered)
          # return False
st.set_page_config(
page_title="Multiple App",
layout="wide"
       )
with open("design.css") as ds:
    st.markdown(f"<style>{ds.read()}</style>", unsafe_allow_html=True)
    st.title(":blue[CLINICAL DECISION SUPPORT SYSTEM FOR EARLY PREDICTION OF TYPE 2 DIABETES]")
    st.title(":green[This System was developed to predict Type 2 Diabetes. Kindly select your preferred language from the left side of this page to interact with the system.]")
    st.sidebar.success("Select your preffered Language above.")
     
#if acct():
 #   st.set_page_config(
  #  page_title="Multiple App",
   # layout="wide"
    #    )
    #with open("design.css") as ds:
     #   st.markdown(f"<style>{ds.read()}</style>", unsafe_allow_html=True)
      #  st.title("Clinical Decision Support System for early detection of type 2 diabetes ".upper())
       # st.sidebar.success("Select your preffered Language above.")
