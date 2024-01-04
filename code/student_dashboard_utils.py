import random
from gpt4all import GPT4All
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(doc1, doc2):
    # Create CountVectorizer
    vectorizer = CountVectorizer()

    # Fit and transform the documents
    vectorized_docs = vectorizer.fit_transform([doc1, doc2])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(vectorized_docs)

    # The cosine similarity matrix is symmetric, and we're interested in the off-diagonal element.
    # The element at [0, 1] or [1, 0] is the cosine similarity between doc1 and doc2.
    similarity_score = cosine_sim[0, 1]

    return similarity_score

def expected_answer(index,user_answer):
    # print(index)
    Understanding_the_Material_answer='''Yes, I found the material to be quite challenging, especially the advanced topics.
    Some parts were challenging, but overall, I managed to grasp the concepts.
    The material was challenging, but the explanations in the textbook helped.
    Initially, it was challenging, but with regular study, it became more manageable.
    Certain sections of the material posed a significant challenge for me.
    The difficulty varied, but I generally found the material to be challenging.
    I found the material challenging, which motivated me to seek additional resources.
    There were moments of difficulty, but seeking clarification from the instructor helped.
    The challenging aspects of the material pushed me to engage in deeper learning.
    Yes, it was challenging, but the practical examples in class made it clearer.
    I struggled with the more abstract concepts in the later chapters.
    Specific mathematical concepts were challenging for me to grasp.
    The programming syntax in certain topics posed a struggle for me.
    I found it difficult to understand the theoretical framework in some areas.
    Advanced statistical concepts were particularly challenging for me.
    The concepts related to data structures were a bit of a struggle.
    I had difficulty with the historical context of certain topics.
    Quantum mechanics concepts were particularly challenging to comprehend.
    Understanding the economic theories presented was a struggle.
    The intricacies of organic chemistry concepts were hard to master.
    Yes, I felt well-prepared due to consistent revision and practice.
    I dedicated extra time to preparation, so I felt adequately ready.
    The practice exams helped, and I felt reasonably well-prepared.
    I had some concerns initially, but additional study time boosted my confidence.
    Mock exams were beneficial, and I felt adequately prepared as a result.
    I engaged in group study sessions, which contributed to my preparedness.
    The review sessions conducted by the instructor were instrumental in my preparation.
    I could have been more prepared, but last-minute review sessions helped.
    A comprehensive study schedule ensured I felt well-prepared.
    Despite initial worries, consistent study habits left me feeling ready for the exam.
    No, the material was not challenging at all; it felt too easy.
    No, I didn't struggle with any topics; everything seemed straightforward.
    No, I didn't feel prepared at all; I lacked sufficient understanding of the content.
    No difficulties whatsoever; studying was a breeze.
    No, I never felt overwhelmed; the workload was quite manageable.
    No obstacles; I easily grasped every aspect of the subject.
    No, I didn't need any additional help; the standard resources were more than enough.
    No, the exam was exactly as expected; no surprises or challenges.
    No stress or anxiety; I was completely at ease during the exam.
    No uncertainties; I felt completely confident in my knowledge of the exam material.'''


    Study_Habits_Answer='''I followed a structured study schedule, covering one topic each day leading up to the exam.
    My preparation involved creating concise study notes and reviewing them regularly.
    I utilized flashcards to reinforce key concepts and definitions.
    I joined a study group to discuss and quiz each other on different topics.
    Mock exams played a crucial role in my preparation, helping me gauge my understanding.
    I focused on practicing past exam papers to familiarize myself with the question patterns.
    Seeking clarification from the instructor on challenging topics was a key part of my preparation.
    I used online resources and video tutorials to supplement my textbook readings.
    Mind mapping helped me visualize the relationships between different concepts.
    I incorporated short breaks into my study sessions to maintain focus and avoid burnout.
    The Pomodoro Technique was effective for me—25 minutes of focused study followed by a 5-minute break.
    I adopted the Feynman Technique, teaching the concepts to someone else to solidify my understanding.
    Visual aids, such as diagrams and charts, were instrumental in my study approach.
    I practiced active recall by quizzing myself on key concepts without looking at my notes.
    Utilizing mnemonic devices helped me remember complex sequences and lists.
    Cornell note-taking system improved my organization and retrieval of information.
    The SQ3R method (Survey, Question, Read, Recite, Review) guided my textbook reading strategy.
    Creating concept maps allowed me to see the connections between different ideas.
    I embraced the Leitner system for flashcards, prioritizing the review of cards I struggled with.
    Reflective journaling at the end of each study day helped reinforce what I had learned.
    I aimed for at least 2 hours of focused study each day in the weeks leading up to the exam.
    My schedule allowed for 4-5 hours of daily study, balancing work and other commitments.
    I dedicated weekends to more extended study sessions, totaling around 15-20 hours per week.
    Closer to the exam, I increased my daily study time to 6-8 hours to cover all topics.
    I followed a flexible study routine, adjusting the time based on the difficulty of the material.
    On average, I dedicated around 25-30 hours per week to exam preparation during peak study periods.
    I prioritized consistency, spreading my study hours evenly over the entire study period.
    Balancing work and family responsibilities, I managed to dedicate 10-15 hours per week to studying.
    I strategically front-loaded my study hours, focusing more intensely in the weeks preceding the exam.
    Reflecting on my approach, I realized that quality study sessions were more effective than sheer quantity, averaging around 3-4 hours a day.
    I mostly relied on last-minute cramming.
    No, I didn't use any methods; I just read through the material without a plan.
    I barely dedicated any time to studying; I thought I could wing it.
    No schedule; I studied sporadically without any consistency.
    I didn't find any resources helpful; I didn't bother seeking extra materials.
    No, I didn't seek any guidance; I preferred figuring things out on my own.
    I didn't take any practice exams; I assumed I knew the material well enough.
    No distractions; my study environment was perfect, but I still didn't put in much effort.
    No goals; I approached studying without a clear objective in mind.
    I rarely reviewed my notes; I thought I could remember everything without reinforcement.'''



    class_engagement_answer='''Yes, I actively participated in class discussions, sharing my perspectives on various topics.
    Being engaged in class discussions was a priority for me, as it enhanced my understanding of the material.
    I made a conscious effort to contribute to group activities, fostering a collaborative learning environment.
    Actively engaging in class discussions helped me connect theoretical concepts to real-world scenarios.
    I not only participated in discussions but also volunteered for class activities to reinforce my learning.
    Class engagement was a key aspect of my learning strategy, as it kept me motivated and focused.
    I found that actively participating in activities helped me absorb and retain information more effectively.
    I made it a habit to listen attentively and respond thoughtfully during class discussions to maximize my learning.
    Engaging with my peers and the instructor in class discussions enriched my overall learning experience.
    Actively participating in class discussions was instrumental in building my confidence to express my ideas.
    Absolutely, I made a point to ask questions whenever I needed clarification on a concept.
    Asking questions was a crucial part of my learning process, ensuring I had a solid grasp of the material.
    I never hesitated to seek clarification by asking questions, especially when faced with challenging topics.
    I found that asking questions not only helped me but also prompted valuable discussions in the class.
    Whenever uncertainty arose, I proactively raised questions to address any gaps in my understanding.
    Asking questions during class was a proactive measure to address any confusion and deepen my understanding.
    I recognized the importance of seeking clarification, and asking questions became a regular part of my learning routine.
    I made it a habit to jot down questions as they arose during lectures and sought answers afterward.
    Actively seeking feedback from the instructor by asking questions was a key strategy in my learning approach.
    I viewed asking questions as a sign of curiosity and a way to continuously improve my understanding of the subject matter.
    No, I rarely participated in class discussions or activities; I preferred staying quiet.
    No, I never asked questions; I didn't want to draw attention to my lack of understanding.
    I avoided engaging in class discussions or activities; it seemed like a waste of time.
    No, I stayed passive in class; participation didn't interest me.
    I didn't contribute to class discussions or activities; I kept to myself.
    No questions from me; I didn't want to appear confused or uninformed.
    I wasn't actively engaged in class; I found it easier to zone out.
    No participation in discussions or activities; I felt it wasn't necessary for my learning.
    I refrained from asking questions; I thought I could figure things out later.
    No, I didn't actively participate in class; I felt it wasn't worth the effort.
    Yes,I asked questions'''


    Resource_Utilization_Answer='''Yes, I extensively used supplementary textbooks to delve deeper into certain topics covered in class.
    Online materials, including video lectures and interactive simulations, played a significant role in my learning process.
    I sought tutoring for specific challenging subjects to receive personalized guidance and clarification.
    Additional resources like academic journals and research papers were invaluable in gaining a more comprehensive understanding.
    I utilized online forums and discussion boards to connect with peers and expand my knowledge base.
    Podcasts and educational podcasts were part of my routine, providing an alternative perspective on certain subjects.
    I attended workshops and seminars, complementing my classroom learning with practical insights.
    Khan Academy and similar platforms were instrumental in providing step-by-step explanations for complex problems.
    I joined study groups where we collectively explored additional resources to enhance our understanding.
    Educational apps and interactive online quizzes were used for self-assessment and reinforcing key concepts.
    The supplementary textbook for the course was exceptionally helpful, providing in-depth explanations and examples.
    Online forums were beneficial, but I found some discussions to be less relevant or accurate.
    Tutoring sessions were highly effective, offering personalized assistance that significantly improved my understanding.
    A particular online simulation tool proved to be unhelpful, as it lacked the depth required for a thorough understanding.
    I discovered that a specific YouTube channel provided clear and concise explanations, making complex topics more accessible.
    Some online courses were less helpful due to a misalignment of content with the course curriculum.
    Educational podcasts offered unique perspectives but were not as beneficial for the specific topics covered in my course.
    I found academic journals to be extremely helpful, especially when researching for assignments and projects.
    Interactive learning modules on certain websites were engaging and effective in reinforcing key concepts.
    A specific tutoring service was less helpful because the teaching style didn't align with my learning preferences.
    No, I didn't use any additional resources; I solely relied on the class materials.
    I didn't bother with extra resources; I thought they wouldn't add much value.
    No textbooks, online materials, or tutoring for me; I thought it was unnecessary.
    I didn't seek any additional help; I assumed the provided resources were sufficient.
    No, I didn't find any extra resources helpful; they seemed like a waste of time.
    I didn't explore additional materials; I thought they wouldn't make a difference.
    No, I didn't use any outside resources; I stuck to what was given in class.
    I didn't consider using other materials; I believed the class materials were comprehensive enough.
    No, I didn't find any external resources helpful; they didn't contribute to my understanding.
    I didn't use textbooks, online materials, or tutoring; I didn't see the need for them.'''

    Understanding_the_Material_answer=Understanding_the_Material_answer.lower()
    Study_Habits_Answer=Study_Habits_Answer.lower()
    class_engagement_answer=class_engagement_answer.lower()
    Resource_Utilization_Answer=Resource_Utilization_Answer.lower()
    lis=[Understanding_the_Material_answer,Study_Habits_Answer,class_engagement_answer,Resource_Utilization_Answer]
    user_answer=user_answer.lower()
    
    
    simi= calculate_cosine_similarity(lis[index-1],user_answer)
    if simi>0:
        return 1
    else:
        return 0

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
        return "Please wait while we analyse your resposne and generate a feedback report."
def model_bot(prompt):
    try:
            model=model_loader()
            # Generate response for your prompt.
            input="you are a personalised career guidance to students , you will chat with students regarding their academic performance and their future career aspects . Answer queries related to this field only and deny any other questions which are not related to education or career."
            
            input_text=f"{input}\t{prompt}"

            # Generate response for the combined prompt.
            
            output = model.generate(input_text, max_tokens=900, streaming=True, temp=0.5, repeat_penalty=1.4, n_batch=10)
            # st.write(output)
            return output
    except RuntimeError:
        error_message = "Please refresh the website.\nThere is an error due to an interrupted server connection."
        print(error_message)
        return 
    
def Rephrase():
    phrases="Please Give a Valid answer or try to write complete sentences."
    return str(phrases)

def feedback():
    model=model_loader()
    prompt="From the given chat session give valuable feedback and suggestion to the student personally."
    global content
    with open('/Users/adityasinha/Desktop/PROJECT/setmax/PythonFile/chat_history.txt', 'r') as file:
        content = file.read()
    prompt=prompt+"\t"+content
    output=model.generate(prompt=prompt,temp=0.7,max_tokens=450,streaming=True)
    return output

@st.cache_resource(show_spinner=False)
def model_loader():
    try :
        
        
        print("Loading model")
        falcon_model = GPT4All("ggml-model-gpt4all-falcon-q4_0.bin")
        
        return falcon_model
    except:
        print("Model can't be loaded")
        st.cache_resource.clear()
        return model_loader()