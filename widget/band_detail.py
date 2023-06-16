import streamlit as st

def get_band_detail():
    st.header(st.session_state['detail'])
    # 대표음악
    # st.image("https://cdn.pixabay.com/photo/2018/05/17/16/03/compass-3408928_1280.jpg")
    st.image(st.session_state['music'], use_column_width=True)
    link = st.session_state['link']
    st.write(f"[**뮤직비디오**]({link})")
