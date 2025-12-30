import os
import streamlit as st
import numpy as np
from PIL import Image
import time



# App Title
st.title("Gastric cancer prediction")

st.markdown(unsafe_allow_html=True, body="<p>In this web, you can select the patient folder and predict the probability of gastric cancer.</p>"
                                         "<p>Step1.</p>"
                                         "<p>Step2&3.</p>"
                                         "<p>Step4.</p>"
                                         "<p>Step5.</p>"
                                         "<p>Step6.</p>")
                                        

# =============================================================================
# img = st.file_uploader(label='Load a CT brain image', type=['png','jpg','jpeg'], key='CT', accept_multiple_files=False)
# basename = img.name
# =============================================================================


imgname = st.selectbox('Select the patient', (None, 'P249750000282','6244535'))
# imgname = st.selectbox('Select the CT image', (None, 'CTbrain_1.png','CTbrain_2.png','CTbrain_3.png','CTbrain_4.png','CTbrain_5.png','CTbrain_6.png','CTbrain_7.png','CTbrain_8.png'))

if imgname is not None:
    images = os.listdir('gastric_image/')
    images_count = len(images)
    # st.subheader('Raw image:', images_count)
    st.write('Raw image:', images_count)
  
    # img = Image.open(f'CTimage/{imgname}')
    # st.subheader('CT image')
    # st.image(img, width=340, caption=f'{imgname}')
    
    
    exclude = st.button('Click here to exclude')
    if exclude is True:
        images = os.listdir('Step1_ExclusionCriteria/')
        images_count = len(images)
        # st.subheader('Step1_ExclusionCriteria:', images_count)
        st.write('Step1_ExclusionCriteria:', images_count)
      
        # st.text('Predicting...')
        # col1, col2 = st.columns(2)
        
        # time.sleep(1)
        # Segment = Image.open(f'CToverlay/{imgname}')
        # col1.subheader('Segmentation')
        # col1.image(Segment, use_column_width=True)
        # col1.text('Red line (Ground Truth)\nBlue line (Prediction)')
        
        # time.sleep(1)
        # GradCAM = Image.open(f'GradCAM/{imgname}')
        # col2.subheader('GradCAM')
        # col2.image(GradCAM, use_column_width=True)
  
    ABF = st.button('Click here to recognize Antrum/Body/Fundus')
    if ABF is True:
        A = os.listdir('Step2and3_ABF/A/')
        A_count = len(A)
        # st.subheader('Antrum:', A_count)
        st.write('Antrum:', A_count)
      
        B = os.listdir('Step2and3_ABF/B/')
        B_count = len(B)
        # st.subheader('Body:', B_count)
        st.write('Body:', B_count)

        F = os.listdir('Step2and3_ABF/F/')
        F_count = len(F)
        # st.subheader('Fundus:', F_count)
        st.write('Fundus:', F_count)
