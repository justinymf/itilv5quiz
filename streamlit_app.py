import streamlit as st
import random

# Set Page Configuration
st.set_page_config(page_title="ITIL Foundation v5 Exam Simulator", layout="wide")

# Internal Question Bank Data
def get_question_bank():
    return [
        {
            "id": 1,
            "question": "Which facet of offering and service oversight concentrates on establishing a system of rules, policies, and standards to govern data resources?",
            "options": ["Partners and suppliers", "Organizations and people", "Information and technology", "Value streams and processes"],
            "answer": "C",
            "rationale": "The Information and technology dimension is concerned with Data Governance, which is the system of rules, policies, and standards implemented to manage data assets."
        },
        {
            "id": 2,
            "question": "What defines a service request?",
            "options": ["A flaw or vulnerability in a product or platform", "A user-initiated action that activates an established service", "A cause of one or more service disruptions", "A change of state significant for oversight"],
            "answer": "B",
            "rationale": "A service request represents a routine interaction where a user asks for a pre-defined task, such as requesting information or resetting a password."
        },
        {
            "id": 3,
            "question": "Following evaluating its existing client support performance, a telecommunications organization establishes an objective to decrease mean call times from 10 minutes to 3 minutes within six months. What Continual Improvement phase are they executing?",
            "options": ["Take Action", "Where do we want to be?", "What is the vision?", "Where are we now?"],
            "answer": "B",
            "rationale": "The phase 'Where do we want to be?' focuses on defining specific, measurable targets (SMART objectives) based on identified baselines."
        },
        {
            "id": 4,
            "question": "What are digital products in the context of digital services?",
            "options": ["The means to deliver value to service users", "The governance framework for service administration", "The technical capabilities that facilitate service delivery", "The contract between service supplier and customer"],
            "answer": "C",
            "rationale": "Digital products represent the underlying capabilities and technical resources (technology, people, processes) required to make a service possible."
        },
        {
            "id": 5,
            "question": "What constitutes NOT one of the four classifications of service level metrics?",
            "options": ["Warranty", "Utility", "Sustainability", "Governance"],
            "answer": "D",
            "rationale": "Governance is a management framework, not a service level metric. The core categories are Utility, Warranty, Sustainability, and Experience."
        },
        {
            "id": 6,
            "question": "What is the ITIL Service Value System?",
            "options": ["A collection of institutional competencies intended for executing work", "A framework by which digital innovation is regulated", "A model representing how all components of an organization work together to facilitate value creation", "The set of activities that generate value through delivery"],
            "answer": "C",
            "rationale": "The SVS describes how all components and activities of an organization work together as a system to enable value creation."
        },
        {
            "id": 7,
            "question": "What component of the operating model pertains to the workflows used by an organization to generate value?",
            "options": ["Value streams and processes", "Partners and suppliers", "Information and technology", "Organizations and people"],
            "answer": "A",
            "rationale": "This dimension focuses on the activities, workflows, and controls necessary to transform demand into value."
        },
        {
            "id": 8,
            "question": "Which BEST characterizes service actions?",
            "options": ["Integration of digital assets delivering value", "Actions facilitating value without conveying possession", "Actions performed by a service provider or jointly with a consumer", "Consumer's access to provider resources"],
            "answer": "C",
            "rationale": "Service actions are specific tasks performed to meet consumer needs, often involving collaboration between provider and consumer."
        },
        {
            "id": 9,
            "question": "What is the customer of a service accountable for?",
            "options": ["Utilizing the service", "Defining the service requirements", "Supplying the service", "Approving the budget for the service"],
            "answer": "B",
            "rationale": "The customer defines the requirements for the service and is responsible for the outcomes. The sponsor authorizes the budget."
        },
        {
            "id": 10,
            "question": "What BEST characterizes the tenet of 'Keep it simple and practical'?",
            "options": ["Solutions architected to handle exceptions through rules", "Include as many functionalities as possible", "Distinct and comprehensive procedures for all exceptions", "Add as many steps as possible for regulation"],
            "answer": "A",
            "rationale": "Simplicity involves using the minimum number of steps and using established rules to manage exceptions rather than complex custom workflows."
        },
        {
            "id": 11,
            "question": "The purpose of the 'deliver' activity is to:",
            "options": ["Align service offerings with corporate strategy", "Develop and incorporate functional solutions", "Resolve incidents and guarantee disaster recovery", "Provide services and manage user onboarding/offboarding"],
            "answer": "D",
            "rationale": "The deliver activity focuses on the actual provision of services and managing the lifecycle of the user relationship."
        },
        {
            "id": 12,
            "question": "What does the 'Partners and suppliers' practice guide offer?",
            "options": ["Dependencies on third parties", "Capability levels and suggestions for self-assessment", "Purpose and summary of the practice", "Key information, automation, and instruments"],
            "answer": "A",
            "rationale": "This section details the external relationships, vendor reliance, and dependencies required for the practice to function."
        },
        {
            "id": 13,
            "question": "What constitutes an illustration of access to resources?",
            "options": ["Staff participating in training", "Hardware setup by a technician", "Notebook delivery to workplace", "Permission provided to use a cloud-based app"],
            "answer": "D",
            "rationale": "Access to resources means the consumer is granted the right to use a resource (like SaaS) without transferring ownership."
        },
        {
            "id": 14,
            "question": "What represents a series of steps that an organization undertakes to facilitate benefit for consumers through oversight of products and services?",
            "options": ["Product and service lifespan", "Service journey", "Value stream", "Value stream mapping"],
            "answer": "C",
            "rationale": "A value stream is the end-to-end sequence of activities performed to create and deliver value."
        },
        {
            "id": 15,
            "question": "How is Site Reliability Engineering (SRE) defined?",
            "options": ["Integrating code into a centralized codebase", "Strategy to mitigate unforeseen incidents", "Evaluating product dependability", "Applying software engineering to infrastructure and operations"],
            "answer": "D",
            "rationale": "SRE treats operations as a software problem, using engineering practices to manage systems and ensure reliability."
        },
        {
            "id": 16,
            "question": "Within the 'partners and suppliers' dimension, what characterizes entities establishing flexible partnerships?",
            "options": ["Avoid cooperation to preserve autonomy", "Operate exclusively through formal contracts", "Rely on suppliers without cooperation", "Share common goals and risks to achieve outcomes"],
            "answer": "D",
            "rationale": "Flexible partnerships involve high collaboration where parties align objectives and share both risks and rewards."
        },
        {
            "id": 17,
            "question": "Which statement regarding the relationship between management practices and value chain activities is ACCURATE?",
            "options": ["Each value chain activity is assisted by several management practices", "Each practice bolsters one value chain activity", "Practices supersede the need for value chain activities", "Activities and practices function autonomously"],
            "answer": "A",
            "rationale": "Value chain activities define the flow of work, while multiple practices provide the specialized tools and skills to execute that work."
        },
        {
            "id": 18,
            "question": "In what way do guiding principles and continual improvement affect governance activities?",
            "options": ["They are optional components", "They provide a framework for defining governance and ensure alignment", "They focus exclusively on fiscal performance", "They apply strictly to management practices"],
            "answer": "B",
            "rationale": "Guiding principles inform how governance is conducted, and continual improvement ensures governance remains relevant over time."
        },
        {
            "id": 19,
            "question": "What constitutes a key success metric for 'Transition'?",
            "options": ["Number of operational variances", "Quality of resources from vendors", "Negative impact of changes on service availability", "Performance against SLA objectives"],
            "answer": "C",
            "rationale": "Transition success is measured by the smooth introduction of changes without disrupting existing operations."
        },
        {
            "id": 20,
            "question": "What most accurately defines the notion of utility?",
            "options": ["Assurance assisting in fit for use", "Functionality offered to meet a specific need", "Assurance fulfilling criteria", "Emotional interactions with a service"],
            "answer": "B",
            "rationale": "Utility is 'fit for purpose'—it describes what the service does to support performance or remove constraints."
        },
        {
            "id": 21,
            "question": "How is an error defined?",
            "options": ["Reduction in quality", "Unplanned interruption", "Event resulting in loss", "A flaw or vulnerability in a service"],
            "answer": "D",
            "rationale": "An error is a weakness, mistake, or vulnerability within a product or service that has potential to cause incidents."
        },
        {
            "id": 22,
            "question": "What assertion concerning a basic relationship is ACCURATE?",
            "options": ["Operates across all enterprise tiers", "Involves out-of-the-box solutions", "Customized to satisfy client requirements", "Focuses on innovation and expansion"],
            "answer": "B",
            "rationale": "Basic relationships are transactional and involve standardized, off-the-shelf products for mass-market needs."
        },
        {
            "id": 23,
            "question": "What constitutes the primary focus of the 'start where you are' guiding principle?",
            "options": ["Reduce complexity by doing fewer tasks", "Ensure cycles align with MVP", "Assessing current resources before decisions", "Understanding who the consumers are"],
            "answer": "C",
            "rationale": "This principle emphasizes looking at current assets to avoid wasting time 'reinventing the wheel'."
        },
        {
            "id": 24,
            "question": "Which of the subsequent items represents an illustration of a service action?",
            "options": ["Cloud entry to virtual nodes", "User viewing content on a portal", "Delivery of physical token", "Online training session for users"],
            "answer": "D",
            "rationale": "A service action is an activity performed by the provider; training is a proactive task to help the user."
        },
        {
            "id": 25,
            "question": "In what way can continual improvement of value streams be realized?",
            "options": ["Removing external dependencies", "Creating new streams for each offering", "Improving management practices that support value streams", "Directly controlling variability"],
            "answer": "C",
            "rationale": "Value streams are enabled by practices; therefore, improving the underlying practices naturally improves the value streams."
        },
        {
            "id": 26,
            "question": "In what manner should an organization apply the guiding principles?",
            "options": ["Sequentially", "As optional suggestions", "Relying on just one or two", "Considering relevance in every situation"],
            "answer": "D",
            "rationale": "Principles are universal and holistic; they should be weighed based on the specific context of the challenge."
        },
        {
            "id": 27,
            "question": "What aspect of product management emphasizes making decisions according to various levels of complexity?",
            "options": ["Organizations and people", "Partners and suppliers", "Information and technology", "Value streams and processes"],
            "answer": "D",
            "rationale": "The Value streams and processes dimension introduces complexity thinking to design agile workflows."
        },
        {
            "id": 28,
            "question": "For what reason are management practices crucial?",
            "options": ["Define enterprise mission", "Replace the need for value streams", "Provide resources and capabilities to accomplish goals", "Influence fiscal results"],
            "answer": "C",
            "rationale": "Practices are sets of organizational resources designed to perform specific work or achieve goals."
        },
        {
            "id": 29,
            "question": "Which type of risk is introduced to users by a service?",
            "options": ["Shortage of personnel accessibility", "The service provider ceasing to operate", "Failure of client-owned hardware", "Requirement for staff education"],
            "answer": "B",
            "rationale": "Dependency on a provider is an 'imposed risk'—if the provider stops operating, the consumer loses the service."
        },
        {
            "id": 30,
            "question": "What is the objective of 'transition'?",
            "options": ["To introduce products into live environment", "Ensure alignment with user demands", "Create blueprints and prototypes", "Develop and evaluate products"],
            "answer": "A",
            "rationale": "Transition focuses on moving a service from development/testing into the live production environment."
        },
        {
            "id": 41,
            "question": "What is 'A formal description of one or more services designed to address the needs of a target consumer group'?",
            "options": ["Service offering", "Service actions", "Service value", "Service catalog"],
            "answer": "A",
            "rationale": "This is the definition of a service offering, which includes goods, access to resources, and service actions."
        },
        {
            "id": 42,
            "question": "What is defined as 'A configuration of an organization's resources designed to offer value for a consumer'?",
            "options": ["Digital product", "Product", "Service offering", "Digital service"],
            "answer": "B",
            "rationale": "A product is a specific configuration of resources (people, info, tech, processes) intended for a consumer."
        },
        {
            "id": 43,
            "question": "What is 'A means of enabling value co-creation by facilitating outcomes that consumers want to achieve, without the consumer having to manage specific costs and risks'?",
            "options": ["Service level", "Service quality", "Service", "Service action"],
            "answer": "C",
            "rationale": "This is the core ITIL definition of a Service."
        },
        {
            "id": 47,
            "question": "What is 'A recurring organizational activity performed at all levels to ensure stakeholders' expectations are met'?",
            "options": ["Continual improvement", "Continuous delivery", "Continuous deployment", "Continuous integration"],
            "answer": "A",
            "rationale": "Continual improvement happens at every level of the organization to maintain performance and alignment."
        },
        {
            "id": 52,
            "question": "What is 'The functionality offered by a product or service; often described as fit for purpose'?",
            "options": ["Warranty", "Utility", "Sustainability", "Reliability"],
            "answer": "B",
            "rationale": "Utility refers to what the service does."
        },
        {
            "id": 53,
            "question": "What is 'Assurance that a product or service will meet agreed requirements; often described as fit for use'?",
            "options": ["Utility", "Reliability", "Warranty", "Observability"],
            "answer": "C",
            "rationale": "Warranty refers to how the service performs (availability, security, etc.)."
        },
        {
            "id": 63,
            "question": "What is 'The perceived benefits, usefulness, and importance of something'?",
            "options": ["Output", "Outcome", "Value", "Utility"],
            "answer": "C",
            "rationale": "Value is subjective and defined by the importance or benefits perceived by the stakeholder."
        },
        {
            "id": 71,
            "question": "What is 'A series of steps an organization undertakes to enable value for consumers through management of products and services'?",
            "options": ["Value", "Value stream", "Service journey", "Operating model"],
            "answer": "B",
            "rationale": "This is the definition of a Value Stream."
        },
        {
            "id": 73,
            "question": "What is 'An unplanned interruption to a service or reduction in the quality of a service'?",
            "options": ["Problem", "Error", "Incident", "Event"],
            "answer": "C",
            "rationale": "An incident is an interruption to normal operation."
        },
        {
            "id": 91,
            "question": "Which of the following terms BEST defines a change?",
            "options": ["Unplanned disruption", "Addition, alteration, or removal of anything that may impact a product", "Component managed to enable IT delivery", "Root cause of incidents"],
            "answer": "B",
            "rationale": "A change is defined as the addition, modification, or removal of anything impacting products and services."
        }
    ]

# Initialize Session State Variables
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "current_questions" not in st.session_state:
    st.session_state.current_questions = []
if "current_q_idx" not in st.session_state:
    st.session_state.current_q_idx = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "q_checked" not in st.session_state:
    st.session_state.q_checked = {}
if "show_results" not in st.session_state:
    st.session_state.show_results = False

def start_new_quiz():
    all_q = get_question_bank()
    num_to_pick = min(40, len(all_q))
    st.session_state.current_questions = random.sample(all_q, num_to_pick)
    st.session_state.current_q_idx = 0
    st.session_state.user_answers = {}
    st.session_state.q_checked = {}
    st.session_state.quiz_started = True
    st.session_state.show_results = False

# UI Layout
st.title("📚 ITIL Foundation (Version 5) Exam Simulator")
st.markdown("---")

if not st.session_state.quiz_started:
    st.header("Welcome to the Exam Simulator")
    st.write("This tool will randomly select **40 questions** from the ITIL Foundation v5 question bank.")
    st.info("You will answer one question at a time and see the correct answer and rationale immediately.")
    
    if st.button("Start Test / 開始測試", type="primary"):
        start_new_quiz()
        st.rerun()

else:
    if not st.session_state.show_results:
        # Display Current Question
        idx = st.session_state.current_q_idx
        q = st.session_state.current_questions[idx]
        total_q = len(st.session_state.current_questions)
        is_checked = st.session_state.q_checked.get(idx, False)
        
        st.subheader(f"Question {idx + 1} of {total_q}")
        st.progress((idx) / total_q)
        st.markdown(f"**{q['question']}**")
        
        # Determine pre-selected option if already answered
        options = q['options']
        pre_selected = None
        if idx in st.session_state.user_answers:
            ans_letter = st.session_state.user_answers[idx]
            pre_selected = ord(ans_letter) - 65
            
        choice = st.radio(
            "Select your answer:",
            options,
            index=pre_selected,
            disabled=is_checked,
            key=f"radio_{idx}"
        )
        
        st.markdown("---")
        
        if not is_checked:
            # Check Answer Button
            if st.button("Check Answer / 核對答案", type="primary"):
                if choice:
                    # Save user's answer and mark as checked
                    letter = chr(65 + options.index(choice))
                    st.session_state.user_answers[idx] = letter
                    st.session_state.q_checked[idx] = True
                    st.rerun()
                else:
                    st.warning("Please select an answer first! / 請先選擇一個答案！")
        else:
            # Feedback Section
            user_letter = st.session_state.user_answers[idx]
            correct_letter = q['answer']
            
            if user_letter == correct_letter:
                st.success(f"✅ Correct! / 答對了！")
            else:
                st.error(f"❌ Incorrect. / 答錯了。")
                st.write(f"**Your Answer:** {user_letter}. {options[ord(user_letter)-65]}")
                st.write(f"**Correct Answer:** {correct_letter}. {options[ord(correct_letter)-65]}")
                
            st.info(f"**Rationale / 解釋:**\n\n{q['rationale']}")
            
            # Navigation Buttons
            if idx < total_q - 1:
                if st.button("Next Question / 下一題", type="primary"):
                    st.session_state.current_q_idx += 1
                    st.rerun()
            else:
                if st.button("View Final Results / 查看最終成績", type="primary"):
                    st.session_state.show_results = True
                    st.rerun()
                    
    else:
        # Final Results Section
        st.subheader("Quiz Completed! / 測驗完成！")
        score = 0
        total = len(st.session_state.current_questions)
        
        for i, q in enumerate(st.session_state.current_questions):
            if st.session_state.user_answers.get(i) == q['answer']:
                score += 1
        
        percentage = (score / total) * 100
        st.header(f"Final Score: {score} / {total} ({percentage:.1f}%)")
        
        if percentage >= 65:
            st.success("Congratulations! You passed the mock exam. 🎉")
        else:
            st.error("You did not reach the 65% passing score. Keep studying! 📖")
            
        if st.button("Start a New Test / 重新開始新測驗", type="primary"):
            start_new_quiz()
            st.rerun()

st.sidebar.title("App Info")
st.sidebar.info("This app references the 'question-bank-ITIL Foundation (version 5).pdf' document.")
st.sidebar.markdown("""
**Mode:** One-by-one (Immediate check)
1. Read the question and select an option.
2. Click "Check Answer".
3. Read the rationale.
4. Proceed to the next question.
""")
