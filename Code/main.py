import streamlit as st
import student_dashboard
import chat_bot
def main():
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'student_dashboard'
        # student_dashboard.main()
    if st.session_state['current_page'] == 'student_dashboard':
        student_dashboard.main()
    elif st.session_state['current_page'] == 'chat_bot':
        chat_bot.d_main()
        
if __name__=="__main__":
    main()