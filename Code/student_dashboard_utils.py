import random
from gpt4all import GPT4All
import streamlit as st
def  Questionnaire(question_number):
    Understanding_the_Material=["Did you find the material challenging?",
                                "Were there specific topics or concepts that you struggled with?",
                                "Did you feel adequately prepared for the exam?"]

    Study_Habits=["How did you prepare for the exam?",
                "Did you use any specific study methods or techniques?",
                "How much time did you dedicate to studying?"]

    Class_Engagement=["Were you actively engaged in class discussions and activities?",
                    "Did you ask questions when you were unsure about something?"]

    Resource_Utilization=["Did you use additional resources, such as textbooks, online materials, or tutoring?",
                        "Were there any resources that you found particularly helpful or unhelpful?"]

    Time_Management=["Did you feel that you had enough time to complete the exam?",
                    "How did you allocate your time during the exam?"]

    Feedback_on_Teaching_Methods=["Are there specific teaching methods or approaches that you feel would help you learn better?",
    "Do you have any suggestions on how I can better support your learning?"]

    External_Factors=["Were there any external factors (personal, family, health) that may have affected your performance?",
                    "Is there anything I should be aware of that might impact your studies?"]

    if question_number==1:
        return random.choice(Understanding_the_Material)
    elif question_number==2:
        return random.choice(Study_Habits)
    elif question_number==3:
        return random.choice(Class_Engagement)
    elif question_number==4:
        return random.choice(Resource_Utilization)
    # elif question_number==5:
    #     return random.choice(Time_Management)
    # elif question_number==6:
    #     return random.choice(Feedback_on_Teaching_Methods)
    # elif question_number==7:
    #     return random.choice(External_Factors)
    else:
        return "Thanks for you valuable Time."
def model_bot(prompt):
    try:
            model=model_loader()
            # Generate response for your prompt.
            input="you are a personalised career guidance to students , you will chat with students regarding their academic performance and their future career aspects . Answer queries related to this field only and deny any other questions which are not related to education or career."
            # input="As a dedicated career guidance assistant for students, I specialize in providing personalized advice. Feel free to discuss your academic performance and inquire about future career prospects. I am here to assist with questions related to this field exclusively. Please note that I may not be able to provide information on topics outside the scope of academic and career guidance"
            # output=model.generate(prompt, max_tokens=500,streaming=True,temp=0.5,repeat_penalty=1.4,n_batch=10)
            # Retrieve conversation history from session state
            # conversation_history = st.session_state.messages
            # conversation_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation_history])

            # Combine conversation history with the prompt
            # input_text = f"{conversation_text}\n{prompt}"
            input_text=f"{input}\t{prompt}"

            # Generate response for the combined prompt.
            
            output = model.generate(input_text, max_tokens=900, streaming=True, temp=0.5, repeat_penalty=1.4, n_batch=10)
            # st.write(output)
            return output
    except RuntimeError:
        error_message = "Please refresh the website.\nThere is an error due to an interrupted server connection."
        print(error_message)
        return 
@st.cache_resource(show_spinner=False)
def model_loader():
    try :
        
        
        print("Loading model")
        falcon_model = GPT4All("ggml-model-gpt4all-falcon-q4_0.bin")
        
        return falcon_model
    except:
        print("Model can't be loaded")