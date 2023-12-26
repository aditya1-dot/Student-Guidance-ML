import streamlit as st
import random
import time
from student_dashboard_utils import model_bot,model_loader
# model_loader()
def d_main():
    st.title("Academate-Ally")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    model_loader()
    # Accept user input
    if u_prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(u_prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": u_prompt})

        # system_prompt = "you are a personalised career guidance to students, you will chat with students regarding their academic performance and their future career aspects. Answer queries related to this field only and deny any other questions."
        # input_prompt = system_prompt + "\n" + str(u_prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Generate response using the combined prompt
            assistant_response = model_bot(prompt=u_prompt)

            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response:
                full_response += chunk + ""
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "")

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

    
    # if u_prompt := st.chat_input("Student's Response?"):

    #                                 # Display user message in chat message container
    #     with st.chat_message("user"):
    #         print("llm")
                            
    #         st.markdown(u_prompt)
    #                                 # Add user message to chat history
    #     st.session_state.messages.append({"role": "user", "content": u_prompt})

    #                                 # system_prompt = "you are a personalised career guidance to students, you will chat with students regarding their academic performance and their future career aspects. Answer queries related to this field only and deny any other questions."
    #                                 # input_prompt = system_prompt + "\n" + str(u_prompt)

    #                                 # Display assistant response in chat message container
    #     with st.chat_message("assistant"):
    #         message_placeholder = st.empty()
    #         full_response = ""
                                        
    #                                     # Generate response using the combined prompt
    #         assistant_response = model_bot(prompt=u_prompt)

    #                                     # Simulate stream of response with milliseconds delay
    #         for chunk in assistant_response:
    #             full_response += chunk + ""
    #             time.sleep(0.05)
    #                                         # Add a blinking cursor to simulate typing
    #             message_placeholder.markdown(full_response + "")

    #                                     # Add assistant response to chat history
    #         st.session_state.messages.append({"role": "assistant", "content": full_response})
                                            
d_main()