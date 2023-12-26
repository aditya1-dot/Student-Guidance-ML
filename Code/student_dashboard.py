import streamlit as st
import time
from student_dashboard_utils import Questionnaire,model_loader,expected_answer,Rephrase
import chat_bot
def initialize_chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def save_chat_history(filename="chat_history.txt"):
    with open(filename, "w") as file:
        for message in st.session_state.messages:
            file.write(f"{message['role']}: {message['content']}\n")

def main():
    st.title("Academate Ally")
    st.subheader("Hello XYZ. This chat session was set in response to your low performance in Test.")
    st.markdown("#### TABLE ###")
    st.markdown("We hope for your sincere contribution in this chatting session.\n:red[Your responses will be used for further sessions.]")
    initialize_chat_history()
    display_chat_history()
    
    # Initialize or get the flag from session_state
    if "flag" not in st.session_state:
        st.session_state.flag = 1

    # Check if it's the bot's turn to ask a question
    if st.session_state.flag == 1:
        # Display assistant question in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Get the question based on the current flag
            assistant_response = Questionnaire(st.session_state.flag)
            
            # Update the flag for the next user response
            st.session_state.flag += 1
            
            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌ ")
            message_placeholder.markdown(full_response)
            model_loader()
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    # Accept user input
    if prompt := st.chat_input("Student's Response"):
        st.session_state.flag-=1
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        updater=expected_answer(st.session_state.flag-1,prompt)
        if updater==1:
            st.session_state.flag+=1
        else:
            with st.chat_message("assistant"):
                message_placeholder=st.empty()
                full_response=""
                assistant_response=Rephrase()
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌ ")
                message_placeholder.markdown(full_response)
        
        # Check if it's the bot's turn to ask a question
        if st.session_state.flag != 6:
            # Display assistant question in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                # Get the question based on the current flag
                assistant_response = Questionnaire(st.session_state.flag)
                
                # Update the flag for the next user response
                st.session_state.flag += 1
                
                # Simulate stream of response with milliseconds delay
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌ ")
                message_placeholder.markdown(full_response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
    if st.session_state.flag==6:
        if st.button("Ask Questions related to Acedemics and Carrer"):
            st.session_state["current_page"]="chat_bot"
            save_chat_history()
            chat_bot.d_main()
    

# if __name__ == "__main__":
    
#     main()
