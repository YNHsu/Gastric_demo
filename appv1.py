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
    st.session_state.images_count = len(images)
    # st.subheader('Raw image:', images_count)
    st.write('Raw image:', st.session_state.images_count)
  
    # img = Image.open(f'CTimage/{imgname}')
    # st.subheader('CT image')
    # st.image(img, width=340, caption=f'{imgname}')
    
    
    # exclude = st.button('Click here to exclude')
    # if exclude is True:
    #     keep_images = os.listdir('Step1_ExclusionCriteria/')
    #     st.session_state.keep_images_count = len(keep_images)
    #     # st.subheader('Step1_ExclusionCriteria:', keep_images_count)
    # st.write('Step1_ExclusionCriteria:', st.session_state.keep_images_count)
      
    #     # st.text('Predicting...')
    #     # col1, col2 = st.columns(2)
        
    #     # time.sleep(1)
    #     # Segment = Image.open(f'CToverlay/{imgname}')
    #     # col1.subheader('Segmentation')
    #     # col1.image(Segment, use_column_width=True)
    #     # col1.text('Red line (Ground Truth)\nBlue line (Prediction)')
        
    #     # time.sleep(1)
    #     # GradCAM = Image.open(f'GradCAM/{imgname}')
    #     # col2.subheader('GradCAM')
    #     # col2.image(GradCAM, use_column_width=True)
  
    # ABF = st.button('Click here to recognize Antrum/Body/Fundus')
    # if ABF is True:
    #     A = os.listdir('Step2and3_ABF/A/')
    #     st.session_state.A_count = len(A)
    #     # st.subheader('Antrum:', st.session_state.A_count)
    #     st.write('Antrum:', st.session_state.A_count)
      
    #     B = os.listdir('Step2and3_ABF/B/')
    #     st.session_state.B_count = len(B)
    #     # st.subheader('Body:', B_count)
    #     st.write('Body:', st.session_state.B_count)

    #     F = os.listdir('Step2and3_ABF/F/')
          # st.session_state.F_count = len(F)
          # # st.subheader('Fundus:', F_count)
          # st.write('Fundus:', st.session_state.F_count)


    # 初始化流程狀態
    if "step" not in st.session_state:
        st.session_state.step = 1    
    if "keep_images_count" not in st.session_state:
        st.session_state.keep_images_count = None    
    if "A_count" not in st.session_state:
        st.session_state.A_count = None
    if "B_count" not in st.session_state:
      st.session_state.B_count = None
    if "F_count" not in st.session_state:
      st.session_state.F_count = None
    
    # ===== Step 1 =====
    st.subheader("Step 1: Exclusion criteria")
    
    if st.session_state.step == 1:
        if st.button('Click here to exclude'):
            keep_images = os.listdir('Step1_ExclusionCriteria/')
            st.session_state.keep_images_count = len(keep_images)
            st.session_state.step = 2   # 前進到下一步
    
    # 顯示 Step 1 結果（永遠保留）
    if st.session_state.keep_images_count is not None:
        st.write('Step1_Exclusion criteria:', st.session_state.keep_images_count)
    
    
    # ===== Step 2 =====
    st.subheader("Step 2: Gastric-Antrum/Body/Fundus classification")
    
    if st.session_state.step >= 2:
        if st.button('Click here to classify Antrum/Body/Fundus'):
            A = os.listdir('Step2and3_ABF/A/')
            st.session_state.A_count = len(A)
            B = os.listdir('Step2and3_ABF/B/')
            st.session_state.B_count = len(B)
            F = os.listdir('Step2and3_ABF/F/')
            st.session_state.F_count = len(F)
            st.session_state.step = 3
    
    # 顯示 Step 2 結果
    cols = st.columns(5)
    if st.session_state.A_count is not None:
        st.write('Antrum:', st.session_state.A_count)
        cols = st.columns(5)
        for idx, img_name in enumerate(A):
            img_path = os.path.join('Step2and3_ABF/A/', img_name)
            image = Image.open(img_path)
            cols[idx % 5].image(image, caption=img_name, use_container_width=True)
    if st.session_state.B_count is not None:
        st.write('Body:', st.session_state.B_count)
        cols = st.columns(5)
        for idx, img_name in enumerate(B):
            img_path = os.path.join('Step2and3_ABF/B/', img_name)
            image = Image.open(img_path)
            cols[idx % 5].image(image, caption=img_name, use_container_width=True)
    if st.session_state.F_count is not None:
        st.write('Fundus:', st.session_state.F_count)
        cols = st.columns(5)
        for idx, img_name in enumerate(F):
            img_path = os.path.join('Step2and3_ABF/F/', img_name)
            image = Image.open(img_path)
            cols[idx % 5].image(image, caption=img_name, use_container_width=True)
