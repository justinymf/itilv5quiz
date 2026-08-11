import streamlit as st
import random

# Set Page Configuration
st.set_page_config(page_title="ITIL Foundation v5 Exam Simulator", layout="wide")

# Internal Question Bank Data
def get_question_bank():
    part1 = [
        {
            "id": 1,
            "question": "Which facet of offering and service oversight concentrates on establishing a system of rules, policies, and standards to govern data resources?",
            "options": ["Partners and suppliers", "Organizations and people", "Information and technology", "Value streams and processes"],
            "answer": "C",
            "rationale": """The Information and technology dimension is concerned with the information and knowledge necessary for the management of services, as well as the technologies required. A critical component of this dimension is Data Governance, which is defined as the system of rules, policies, and standards an organization implements to manage its data assets. It ensures that information is accurate, protected, and used effectively to support business goals.

Why Other Answers are Wrong
A: Partners and suppliers: This dimension focuses on an organization's relationships with other businesses involved in the design, development, and delivery of services. While partners might handle data, the specific focus on implementing a system of rules and standards for data assets is a governance function within the Information and Technology dimension.
B: Organizations and people: This dimension focuses on the human side of service management, including organizational structures, culture, roles, responsibilities, and necessary skills. It deals with how people work together rather than the technical policies used to manage data assets.
D: Value streams and processes: This dimension focuses on the activities, workflows, and coordination needed to create value. While processes use data, the overarching "system of rules and standards" for the data itself is categorized under Information and Technology to ensure the data used in those processes is reliable and secure."""
        },
        {
            "id": 2,
            "question": "What defines a service request?",
            "options": ["A flaw or vulnerability in a product or platform", "A user-initiated action that activates an established service", "A cause of one or more service disruptions", "A change of state significant for oversight"],
            "answer": "B",
            "rationale": """A service request represents a routine interaction where a user asks the service provider to fulfill a pre-defined task. These are standard, low-risk actions that have been agreed upon in advance, such as requesting information, resetting a password, or asking for access to a specific folder. It is a normal part of service delivery and does not imply that anything is broken.

Why the other answers are wrong
A: A flaw or vulnerability in a product or system - This describes an Error. An error is a weakness or a fault within a system that has the potential to cause a failure. A service request is a request for a standard action, not a description of a technical flaw.
C: A cause of one or more service incidents - This describes a Problem. A problem is the underlying root cause that leads to one or more interruptions in service (incidents). While a problem relates to fixing a failure, a service request relates to fulfilling a user's standard need.
D: A change of state significant for management - This describes an Event. An event is a notification or a piece of data indicating that something has happened within the infrastructure (like a system log or a status change). While a service request might create an event, the request itself is the human-initiated demand for service, not just the data indicating a state change."""
        },
        {
            "id": 3,
            "question": "Following evaluating its existing client support performance, a telecommunications organization establishes an objective to decrease mean call times from 10 minutes to 3 minutes within six months. What Continual Improvement phase are they executing?",
            "options": ["Take Action", "Where do we want to be?", "What is the vision?", "Where are we now?"],
            "answer": "B",
            "rationale": """The ITIL Continual Improvement Model is a structured approach for implementing improvements. The step "Where do we want to be?" focuses on defining specific, measurable, and time-bound targets (often called SMART objectives). While the "Vision" provides the high-level direction, this step translates that direction into concrete milestones that the organization aims to reach.
The company has already identified its baseline (10 minutes) and is now defining a specific target state (3 minutes) with a clear deadline (six months). Setting these measurable objectives is the core activity of the "Where do we want to be?" phase.

Why the other answers are wrong
A: Take Action - This step involves the actual execution of the improvement plan. It is the "doing" phase where changes are implemented. Setting a target happens before you take action to reach it.
C: What is the vision? - This is the first step of the model and focuses on high-level business goals and the overall direction. A specific metric like "3 minutes" is a target that supports the vision, not the vision itself.
D: Where are we now? - This step is about conducting a baseline assessment to understand the current situation. Knowing that the current call time is "10 minutes" was part of this step, but the act of setting the new target belongs to the next phase."""
        },
        {
            "id": 4,
            "question": "What are digital products in the context of digital services?",
            "options": ["The means to deliver value to service users", "The governance framework for service administration", "The technical capabilities that facilitate service delivery", "The contract between service supplier and customer"],
            "answer": "C",
            "rationale": """In modern service management, a digital product is a configuration of an organization's resources (such as technology, people, and processes) that are based on digital technology. These products serve as the foundation or the "building blocks" for services. While a service is the actual experience or outcome provided to a user, the digital product represents the underlying capabilities and technical resources required to make that service possible.
Digital products are defined by the resources and technology that compose them. In the relationship between products and services, the product provides the specific capabilities (the functionality and technical setup) that a service provider uses to deliver a service to the consumer.

Why the other answers are wrong
A: The means to deliver value to service consumers - This is the formal definition of a Service. While products are used to create services, the "means of enabling value co-creation" specifically describes the service itself, not the underlying product.
B: The governance framework for service management - Governance refers to the system by which an organization is directed and controlled. It is a set of rules and oversight mechanisms, not a product or a resource configuration used for service delivery.
D: The contract between service provider and consumer - This describes a Service Level Agreement (SLA) or a service agreement. A contract is a documented set of terms and expectations, whereas a digital product is a tangible or intangible technical resource."""
        },
        {
            "id": 5,
            "question": "What constitutes NOT one of the four classifications of service level metrics?",
            "options": ["Warranty", "Utility", "Sustainability", "Governance"],
            "answer": "D",
            "rationale": """In modern service management, service quality is measured through a specific set of dimensions known as service level metrics. These metrics are used to evaluate how well a service meets the needs of the consumer and contributes to value co-creation. They focus on the functionality of the service, its performance reliability, the user's interaction with it, and its impact on broader organizational goals.
Governance is the correct answer because it is NOT one of the four categories of service level metrics. Governance refers to the system by which an organization is directed and controlled (oversight, rules, and decision-making). While governance is a component of the overall Value System, it is a management framework rather than a metric used to measure the specific quality or performance of a service.

Why the other answers are wrong
A: Warranty - This is a core metric category. It measures "how" a service performs and provides assurance that it will meet agreed requirements (e.g., availability, capacity, and security).
B: Utility - This is a core metric category. It measures "what" the service does. It focuses on the functionality offered to support the performance of the consumer or remove their constraints.
C: Sustainability - This is a core metric category. It measures the assurance that a product or service meets requirements for environmental stewardship, social progress, and economic growth.
(Note: The fourth category not listed in the options is Experience or User Experience)."""
        },
        {
            "id": 6,
            "question": "What is the ITIL Service Value System? (What is the ITIL Value System?)",
            "options": ["A collection of institutional competencies intended for executing work or achieving a goal", "A framework by which the present and forthcoming utilization of digital innovation is regulated", "A model representing how all the components and activities of an organization work together to facilitate value creation through digital offerings and solutions", "The entire set of activities that generate value through the delivery of a product or service"],
            "answer": "C",
            "rationale": """The Service Value System (SVS) / The Value System (VS) is the overarching framework in ITIL that describes how an organization functions as a whole. It is designed to break down "silos" by showing how various components—such as leadership values, governing rules, specific work activities, and technical capabilities—interact as a unified system to turn opportunities and demands into actual value.
Option C is the best answer because it captures the holistic nature of the SVS/VS. It isn't just a list of tasks or a single department; it is a "system" view that explains how everything from the organization's guiding principles to its continual improvement efforts works together to ensure value is co-created with stakeholders.

Why the other answers are wrong
A: This is the definition of a Management Practice. Practices are specific sets of resources used within the SVS, but they are only one part of the larger system.
B: This describes Governance. While Governance is a critical component of the SVS, it does not represent the entire system of value creation.
D: This is the definition of the Value Chain. The Value Chain represents the specific sequence of activities that happens inside the SVS, but it excludes the surrounding elements like guiding principles and governance."""
        },
        {
            "id": 7,
            "question": "What component of the operating model pertains to the workflows used by an organization to generate value?",
            "options": ["Value streams and processes", "Partners and suppliers", "Information and technology", "Organizations and people"],
            "answer": "A",
            "rationale": """In ITIL, the "Four Dimensions" represent the different perspectives required to manage products and services effectively. The dimension of Value Streams and Processes specifically looks at the "how" of an organization. It focuses on the activities, workflows, and controls necessary to transform an initial demand or opportunity into actual value for the customer.
Option A is correct because it is the specific dimension dedicated to defining the sequence of steps (value streams) and the sets of activities (processes) that an organization follows to get work done.

Why the other answers are wrong
B: Partners and suppliers - Focuses on the organization's relationships with external entities and third-party dependencies, not the workflows themselves.
C: Information and technology - Covers the data, knowledge, and technical tools used to support services, not the structural design of the work steps.
D: Organizations and people - Focuses on the human side, including corporate culture, staffing, roles, and leadership."""
        },
        {
            "id": 8,
            "question": "Which BEST characterizes service actions?",
            "options": ["An integration of digital assets that deliver user value", "Actions facilitating value through digital offerings without conveying possession", "Actions performed by a service provider or jointly with a consumer", "Consumer's access to a provider's resources according to established terms"],
            "answer": "C",
            "rationale": """In the context of service offerings, service actions represent the "activity" component of a service. Unlike goods (which are physical things) or access to resources (which is permission to use something), service actions are the specific tasks or procedures carried out to meet a consumer's needs. These actions can be performed entirely by the provider (like a technician fixing a server) or as a collaborative effort between the provider and the consumer (like a support agent guiding a user through a software setup).
Option C is the most accurate definition because it captures the collaborative nature of service management.

Why the other answers are wrong
A: This describes a digital product. While service actions may involve digital products, the product itself is the "configuration of resources," whereas the "actions" are the specific activities performed.
B: While it is true that services generally do not transfer ownership, this description is too narrow. It focuses only on the "digital" aspect and the "lack of ownership," failing to define the actual nature of the actions themselves.
D: This is the definition of access to resources. This refers to the permission to use a provider's assets, rather than the performance of a specific task."""
        },
        {
            "id": 9,
            "question": "What is the customer of a service accountable for?",
            "options": ["Utilizing the service", "Defining the service requirements", "Supplying the service", "Approving the budget for the service"],
            "answer": "B",
            "rationale": """In service management, it is important to distinguish between different roles involved in receiving a service:
Sponsor: The person who provides the money (authorizes the budget).
Customer: The person who defines what is needed (requirements) and is responsible for the outcomes of the service.
User: The person who actually interacts with and uses the service on a day-to-day basis.
Option B is the correct definition of the customer role. The customer acts as the "business representative" who negotiates the specific needs and goals that the service must fulfill.

Why the other answers are wrong
A: This describes the user role.
C: This is the responsibility of the service provider. The provider creates, delivers, and supports the service.
D: This describes the sponsor role. The sponsor is specifically focused on the financial aspect and the authority to spend organizational funds."""
        },
        {
            "id": 10,
            "question": "What BEST characterizes the tenet of 'Keep it simple and practical'?",
            "options": ["Solutions should be architected to handle exceptions through rules", "Every product should include as many functionalities as possible to address all anomalies", "All exceptions must be resolved with distinct and comprehensive procedures", "Add as many steps as possible to guarantee every anomaly is fully regulated"],
            "answer": "A",
            "rationale": """The principle of 'Keep it simple and practical' focuses on eliminating waste and avoiding over-complication. Instead of creating a complex process for every possible scenario, organizations should establish simple, clear rules that allow for the handling of exceptions without bloating the system.
Option A is the best answer because it aligns with the idea of being "practical." Rather than trying to map out a unique, complex workflow for every rare event (which leads to over-complication), a simple and practical approach uses established design rules to manage those exceptions efficiently.

Why the other answers are wrong
B: This contradicts the principle. Adding "as many features as possible" leads to "feature creep" and over-complication.
C: Creating unique, detailed processes for every exception is the opposite of simplicity.
D: This is incorrect because the principle specifically advises to "minimize the number of steps" to accomplish an objective."""
        },
        {
            "id": 11,
            "question": "The purpose of the 'deliver' activity is to:",
            "options": ["Align service offerings with corporate strategy", "Develop and incorporate functional solutions", "Resolve incidents and guarantee disaster recovery", "Provide services and manage user onboarding/offboarding"],
            "answer": "D",
            "rationale": """The 'deliver' activity is a specific stage in the product and service lifecycle focused on the actual provision of services to the end-users. While other stages focus on planning, building, or fixing, 'deliver' is about the execution of the service itself. This includes managing the lifecycle of the user's relationship with the service—specifically how they start using it (onboarding) and how they stop using it (offboarding).
Option D is the best answer because it accurately captures the core operational focus of the 'deliver' stage.

Why the other answers are wrong
A: This describes the 'discover' activity.
B: This describes the 'build' activity. The 'build' stage is where the technical work happens.
C: This describes the 'support' activity. 'Support' is focused on the "fix-it" aspect of the lifecycle—restoring service when things go wrong."""
        },
        {
            "id": 12,
            "question": "What does the 'Partners and suppliers' practice guide offer?",
            "options": ["Dependencies on third parties", "Capability levels, criteria, and suggestions for self-assessment", "Purpose and summary of the practice", "Key information, automation, and instruments for a practice"],
            "answer": "A",
            "rationale": """ITIL practice guides are structured to cover various facets of a management practice, aligned with the "four dimensions" of service management. The 'Partners and suppliers' section specifically focuses on the external relationships required for the practice to function. It details how an organization relies on third-party vendors, partners, or contractors, outlining the specific dependencies.
Option A is the best answer because it directly identifies the core content of this specific chapter.

Why the other answers are wrong
B: This information is found in the 'Capability assessment and development' chapter.
C: This is covered in the 'General Information' chapter.
D: This describes the 'Information and technology' chapter."""
        },
        {
            "id": 13,
            "question": "What constitutes is an illustration of access to resources?",
            "options": ["An staff member participates in a training session delivered by an instructor", "A technician performs on-site local setup of hardware", "A supplier delivers new notebooks to the client's workplace", "A user is provided permission to use a cloud-based app"],
            "answer": "D",
            "rationale": """In service management, service offerings are typically categorized into three types: Goods, Access to Resources, and Service Actions.
Access to Resources refers to a setup where the ownership of a resource is not transferred to the consumer. Instead, the consumer is granted the right to use the resource under agreed-upon terms and conditions.
Option D is the best answer because it perfectly illustrates the concept of resource access. In a cloud-based application (SaaS), the user is simply given "access" or permission to use the platform.

Why the other answers are wrong
A: This is an example of a Service Action.
B: This is also a Service Action.
C: This is an example of Goods (ownership is transferred)."""
        },
        {
            "id": 14,
            "question": "What represents a series of steps that an organization undertakes to facilitate benefit for consumers through oversight of products and services?",
            "options": ["Product and service lifespan", "Service journey", "Value stream", "Value stream mapping"],
            "answer": "C",
            "rationale": """In service management, a Value Stream represents the actual end-to-end sequence of activities that an organization performs to create and deliver value to its consumers.
Option C is the correct answer because it matches the formal definition of the term.

Why the other answers are wrong
A: The lifecycle refers to the various stages and statuses that a product or service passes through, not a specific "series of steps" used to enable value in a single operational flow.
B: The service journey describes the sum of activities and interactions from the perspective of both the service provider and the service consumer.
D: Value stream mapping is a technique or tool used to visually represent and analyze value streams, not the "series of steps" itself."""
        },
        {
            "id": 15,
            "question": "How is Site Reliability Engineering (SRE) defined?",
            "options": ["Regularly integrating code into a centralized codebase", "Applying a strategy to mitigate unforeseen incidents that might cause organizational damage", "Evaluating how dependable a product is against its requirements", "Applying software engineering to address infrastructure and operations problems"],
            "answer": "D",
            "rationale": """Site Reliability Engineering (SRE) is a specific discipline that bridges the gap between software development and IT operations. It treats operations as if it were a software problem, using engineering practices and automation to manage systems, solve problems, and ensure that software services are highly reliable and scalable.
Option D is the correct answer because it accurately defines SRE.

Why the other answers are wrong
A: This describes Continuous Integration (CI).
B: This refers to Disaster Recovery or general risk management.
C: This is a general description of Reliability Testing or Quality Assurance."""
        },
        {
            "id": 16,
            "question": "Within the 'partners and suppliers' dimension, what characterizes entities establishing flexible partnerships?",
            "options": ["They avoid cooperation to preserve absolute autonomy", "They operate exclusively through formal contracts with no mutual obligations", "They rely only on suppliers for technical resources without cooperation", "They share common goals and risks while partnering to achieve desired outcomes"],
            "answer": "D",
            "rationale": """In the "partners and suppliers" dimension, a flexible partnership (also referred to as a collaborative relationship) is the most integrated form. It is characterized by a high degree of collaboration where organizations move beyond rigid, standard contracts to focus on mutual innovation and growth. In these arrangements, parties align their objectives and share both the risks and the rewards.
Option D is the best answer because it captures the essence of a collaborative partnership.

Why the other answers are wrong
A: This is incorrect because partnerships are defined by cooperation.
B: This describes a Basic Relationship.
C: This describes a simple supply chain transaction."""
        },
        {
            "id": 17,
            "question": "Which statement regarding the relationship between management practices and value chain activities is ACCURATE?",
            "options": ["Each value chain activity is assisted and facilitated by several management practices", "Each management practice bolsters one value chain activity", "Management practices supersede the need for value chain activities", "Value chain activities and management practices function autonomously of each other"],
            "answer": "A",
            "rationale": """In the ITIL Service Value System, the Service Value Chain represents the high-level operating model consisting of activities like Discover, Design, Build, and Support. Management practices are sets of organizational resources and capabilities designed to perform specific types of work. These two components are deeply integrated: the value chain activities define the flow of work, while the practices provide the specialized tools required to execute that work effectively.
Option A is correct because to perform an activity such as "Support", an organization must utilize multiple specialized practices at once.

Why the other answers are wrong
B: This is incorrect because management practices are versatile and cross-functional.
C: This is incorrect because they serve different purposes. The value chain is the operating model, whereas practices are the capabilities. One cannot exist without the other.
D: This is incorrect because they are highly interdependent."""
        },
        {
            "id": 18,
            "question": "In what way do guiding principles and continual improvement affect governance activities within the ITIL Service Value System (SVS) / Value System (VS)?",
            "options": ["They are optional components that organizations may elect to ignore without affecting governance", "They provide a framework for defining governance principles and ensure ongoing improvement aligns with stakeholder expectations", "They focus exclusively on fiscal performance and do not pertain to governance oversight", "They apply strictly to management practices and do not influence governance activities"],
            "answer": "B",
            "rationale": """In the ITIL Service Value System (SVS), all components are interconnected. Guiding principles provide a consistent approach to decision-making and behavior, which includes how governance is conducted. Continual improvement ensures that the governing body's direction is based on sound principles and that performance is refined to meet expectations.
Option B is correct because it accurately describes the holistic relationship within the SVS/VS.

Why the other answers are wrong
A: This is incorrect because guiding principles and continual improvement are core, non-optional components of the SVS.
C: This is incorrect because ITIL concepts are multidimensional; they focus on broader value, not just fiscal performance.
D: This is incorrect because the ITIL framework explicitly states that guiding principles and continual improvement apply to the entire SVS, including governance."""
        },
        {
            "id": 19,
            "question": "What constitutes a key success metric for 'Transition'?",
            "options": ["Number and consequence of disruptions and operational variances", "Quality of the resources and services sourced from vendors", "Negative impact of changes on service availability and efficiency", "Service performance against the stipulated SLA objectives"],
            "answer": "C",
            "rationale": """The Transition activity in the ITIL Product and Service Lifecycle is responsible for seamlessly introducing new or updated products and services into the live operational environment. A successful transition is one where the change is implemented smoothly without disrupting existing operations. Therefore, the primary way to measure success is to look at whether the deployment caused any "negative impact"—such as downtime or performance degradation.
Option C is the best answer because it directly measures the effectiveness of the transition process.

Why the other answers are wrong
A: This is a key success metric for the Operate activity.
B: This is a key success metric for the Acquire activity.
D: This is a key success metric for the Deliver activity."""
        },
        {
            "id": 20,
            "question": "What most accurately defines the notion of utility?",
            "options": ["The assurance that assists in deciding if a service is fit for use", "The functionality offered by a product or service to meet a specific need", "The assurance that product or service will fulfill stipulated criteria", "The functional and emotional interactions with a service and provider as sensed by a stakeholder"],
            "answer": "B",
            "rationale": """In service management, Utility refers to the functional requirements of a service. It represents "what" the service does for the consumer. A service has utility if it either supports the performance of the user or removes constraints that the user faces. It is often summarized by the phrase "fit for purpose."
Option B is the best answer because it perfectly aligns with the definition of utility.

Why the other answers are wrong
A: This describes Warranty, not utility ("fit for use").
C: This is also a definition of Warranty.
D: This describes User Experience (UX)."""
        },
        {
            "id": 21,
            "question": "How is an error defined?",
            "options": ["A reduction in the quality of a solution", "An unplanned interruption to a solution", "An event resulting in critical loss", "A flaw or vulnerability in a service"],
            "answer": "D",
            "rationale": """In service management, an error is the underlying cause of a potential problem. It represents a specific weakness, mistake, or vulnerability within a product or service.
Option D is the best answer because it provides the formal definition of an error.

Why the other answers are wrong
A: This is part of the definition of an incident.
B: This is also a definition of an incident.
C: This describes a disaster."""
        },
        {
            "id": 22,
            "question": "What assertion concerning a basic relationship is ACCURATE?",
            "options": ["It operates across day-to-day, managerial, and visionary enterprise tiers", "It typically involves out-of-the-box solutions provided to clients", "Services are usually customized to satisfy the requirements of clients", "It focuses on innovation and business expansion"],
            "answer": "B",
            "rationale": """In service management, a basic relationship is the simplest form of interaction between a service provider and a consumer. It is characterized by low levels of complexity and minimal collaboration. These relationships are usually "transactional," meaning the provider offers standardized products or services that are ready to use immediately without any specialized modifications.
Option B is the best answer because it correctly identifies the nature of the services provided in this relationship type. "Out-of-the-box" (or COTS) services are highly standardized.

Why the other answers are wrong
A: A basic relationship typically only occurs at the operational level.
C: This describes a collaborative (or partnership) relationship, where services are customized.
D: This is the typical focus of a collaborative relationship."""
        },
        {
            "id": 23,
            "question": "What constitutes the primary focus of the 'start where you are' guiding principle?",
            "options": ["Reduce complexity by focusing on executing fewer tasks, but doing them better", "Ensure that each iteration cycle aligns with the framework of a Minimum Viable Product", "Assessing the current resources before making decisions", "Encourage all staff to precisely understand who their service consumers are"],
            "answer": "C",
            "rationale": """The "Start where you are" principle advises against starting a project or improvement from scratch without first considering what is already available. It emphasizes that there is almost always something in the current state that can be reused, repurposed, or improved.
Option C is the best answer because it captures the core requirement of this principle: objective assessment of current resources.

Why the other answers are wrong
A: This describes the "Keep it simple and practical" principle.
B: This describes the "Progress iteratively with feedback" principle.
D: This is a primary focus of the "Focus on value" principle."""
        },
        {
            "id": 24,
            "question": "Which of the subsequent items represents an illustration of a service action?",
            "options": ["A cloud vendor granting consumers entry to virtualized computing nodes", "A user accessing a media portal to view content", "A software company delivering a physical authentication device to the client", "A digital learning platform conducting a real-time online training session for users"],
            "answer": "D",
            "rationale": """In service management, a service action is a specific activity or task performed by the service provider (or jointly with the consumer) to address a user's needs. Unlike simply providing a tool or a physical object, a service action is "doing something" for the customer.
Option D is the best answer because conducting a training session is a proactive activity performed by the provider to help the user.

Why the other answers are wrong
A: This is an example of access to resources.
B: Similar to Option A, this is access to resources.
C: This is an example of a transfer of goods."""
        },
        {
            "id": 25,
            "question": "In what way can continual improvement of value streams be realized?",
            "options": ["By removing external dependencies altogether", "By creating new value streams for each offering or solution", "By improving the management practices that support and facilitate value streams", "By directly controlling variability in operational sequences"],
            "answer": "C",
            "rationale": """A value stream is the series of steps an organization takes to deliver value to a consumer. These steps are not performed in a vacuum; they are powered by management practices. The efficiency and quality of a value stream are directly dependent on the maturity and effectiveness of the practices that support it.
Option C is the best answer because improving practices naturally leads to the continual improvement of the value stream's overall performance.

Why the other answers are wrong
A: Eliminating external dependencies is unrealistic and counterproductive.
B: Creating new streams for each offering leads to "reinventing the wheel," operational bloat, and waste.
D: Directly controlling variability is often impossible in complex digital environments."""
        },
        {
            "id": 26,
            "question": "In what manner should an organization apply the guiding principles?",
            "options": ["Sequentially, following a predetermined sequence of importance", "As optional suggestions, that may be ignored", "By relying on just one or two principles for productivity", "By considering the relevance of each principle in every situation"],
            "answer": "D",
            "rationale": """The guiding principles are universal recommendations designed to guide an organization in all circumstances. They are not independent silos; instead, they interact with and depend on one another.
Option D is the best answer because it reflects the flexible and holistic nature of the principles. Organizations are encouraged to look at all the principles and determine how they complement each other.

Why the other answers are wrong
A: There is no predefined hierarchy or "step-by-step" order for the principles.
B: They are not optional suggestions to be ignored; doing so risks failing to deliver actual value.
C: Relying on too few principles leads to a narrow perspective."""
        },
        {
            "id": 27,
            "question": "What aspect of product and service management emphasis analyzing and making decisions in accordance to understanding various levels of complexity?",
            "options": ["Organizations and people", "Partners and suppliers", "Information and technology", "Value streams and processes"],
            "answer": "D",
            "rationale": """The Value streams and processes dimension focuses on the activities an organization undertakes and how they are structured. Within this dimension, ITIL introduces complexity thinking, which is defined as an approach to analysis and decision-making based on recognizing and understanding various levels of complexity.
Option D is correct because the ITIL framework specifically categorizes "complexity thinking" under the Value streams and processes dimension.

Why the other answers are wrong
A: Organizations and people focuses on roles, culture, and leadership.
B: Partners and suppliers addresses relationships with third parties.
C: Information and technology covers data, knowledge, and technical resources."""
        },
        {
            "id": 28,
            "question": "For what reason are management practices crucial in digital product and service management?",
            "options": ["They define the mission of the enterprise", "They replace the requirement for value streams", "They provide resources and capabilities to accomplish goals", "They influence the fiscal results of the enterprise"],
            "answer": "C",
            "rationale": """In digital product and service management, management practices are defined as sets of organizational resources and capabilities (including people, information, technology, and processes) designed and adopted to perform work or achieve a particular goal. They act as the "toolbox."
Option C is the best answer because it directly reflects the core definition and role of management practices.

Why the other answers are wrong
A: The organization's purpose/mission exists before practices are established.
B: Practices and value streams are complementary, they do not replace each other.
D: Influencing fiscal results is a secondary outcome, not the primary reason why they are crucial or how they are defined."""
        },
        {
            "id": 29,
            "question": "Which type of risk is introduced to users by a service?",
            "options": ["Shortage of personnel accessibility within the client entity", "The service provider ceasing to operate", "Failure of hardware owned and managed by the client", "Requirement for consumer staff education to utilize the service efficiently"],
            "answer": "B",
            "rationale": """In service management, every service relationship involves a shift in risks. "Risks imposed" are new risks that a consumer takes on as a direct result of using the service. These typically involve dependencies on the provider.
Option B is the best answer because it represents a fundamental risk of dependency. If the service provider goes out of business, the consumer loses the service. This risk is "imposed" because it only exists because the consumer decided to use that specific service.

Why the other answers are wrong
A: This is an internal operational risk for the consumer.
C: This is a risk that the consumer is responsible for managing themselves.
D: This is classified as a cost of service consumption (internal resource cost) rather than a risk."""
        },
        {
            "id": 30,
            "question": "What is the objective of 'transition'?",
            "options": ["To seamlessly introduce new products into live environment", "To ensure continual alignment of product roadmap with the demands of users", "To create prototypes and blueprint for products and services", "To develop, integrate and evaluate products"],
            "answer": "A",
            "rationale": """The 'transition' activity is a specific stage in the product and service lifecycle focused on deployment. Its primary goal is to move a product or service from the development and testing phase into the live, operational environment where users can actually use it.
Option A directly aligns with the fundamental definition of the transition stage.

Why the other answers are wrong
B: This describes the Discover activity.
C: This describes the Design activity.
D: This describes the Build activity."""
        },
        {
            "id": 31,
            "question": "What aspect of service management is concerned with ensuring that a company's structure supports the fulfillment of long-term strategic goals?",
            "options": ["Organizations and people", "Value streams and processes", "Partners and suppliers", "Information and technology"],
            "answer": "A",
            "rationale": """The Organizations and people dimension focuses on the human and structural elements of service management. It encompasses organizational structures, roles, responsibilities, systems of authority, and communication. A key part is ensuring that the formal hierarchy and the culture are designed to align with and support its overall strategy.
Option A is the best choice because it specifically deals with how a company is organized.

Why the other answers are wrong
B: Focuses on how work is done rather than the formal structure of the company.
C: Focuses on external third parties.
D: Concerned with data, knowledge, and technological assets."""
        },
        {
            "id": 32,
            "question": "What among the subsequent options assists in understanding the internal state of a complex system by reviewing its external outputs?",
            "options": ["Continuous Integration", "Continuous Delivery", "Observability", "Site Reliability Engineering"],
            "answer": "C",
            "rationale": """Observability is the ability to measure the internal state of a system by examining the data it generates externally, such as logs, metrics, and traces.
Option C is the best answer because the definition provided in the question is the literal definition of observability.

Why the other answers are wrong
A: This is a software development practice about merging code, not system state analysis.
B: This ensures software can be deployed at any time.
D: SRE is a broad discipline that uses software engineering to solve infrastructure problems, while observability is the specific capability to measure internal states."""
        },
        {
            "id": 33,
            "question": "What is the primary objective of collecting feedback during digital product development?",
            "options": ["To record the final project outcomes following finalization", "To limit information sharing to senior management to prevent disorder", "To ensure that improvement efforts remain aligned with changing priorities", "To reduce stakeholder participation to minimize complexity"],
            "answer": "C",
            "rationale": """Feedback is information regarding stakeholder reactions and opinions used as a foundation for improvement. By integrating feedback loops, an organization can validate whether they are still creating value and adjust their direction based on real-world data and shifting requirements.
Option C is the best answer because it highlights the navigational role of feedback, allowing teams to respond faster to evolving needs.

Why the other answers are wrong
A: Feedback should be used iteratively while work is in progress, not just documented at the end.
B: Feedback should promote visibility and collaboration, not restrict information.
D: Collecting feedback is intended to increase meaningful stakeholder involvement, not reduce it."""
        },
        {
            "id": 34,
            "question": "What among the subsequent options is a key success metric for 'Operate' activity?",
            "options": ["Number and impact of incidents and performance variances", "Service performance against the agreed SLA benchmarks", "Quality of the resources and services sourced from vendors", "Negative impact of changes on service uptime and performance"],
            "answer": "A",
            "rationale": """The 'Operate' activity is focused on maintaining and monitoring live digital products and their supporting systems. Because this stage is about the day-to-day stability of the environment, success is measured by how few disruptions occur and how well the system stays within its expected performance parameters.
Option A is the best answer because incidents and performance deviations are direct indicators of operational health.

Why the other answers are wrong
B: This is a success metric for the 'Deliver' activity.
C: This is a key success metric for the 'Acquire' activity.
D: This is a key success metric for the 'Transition' activity."""
        },
        {
            "id": 35,
            "question": "What most accurately describes a digital service?",
            "options": ["A combination of an organization's resources based on advanced systems intended to provide benefit to users", "A means of enabling value for consumers through digital products without ownership transfer", "The adoption and facilitating of digital technologies across all sectors of an enterprise", "The maintaining and improving the productive, capable, and accessible utilization of data"],
            "answer": "B",
            "rationale": """In ITIL, a service is fundamentally defined as a way to enable value for customers by helping them achieve their desired outcomes without them having to own the underlying resources. A digital service specifically applies this concept by relying on digital products to deliver that value.
Option B is the best answer because it correctly synthesizes two core ITIL concepts: The definition of a service (a "means of enabling value" where the consumer does not take on ownership/risk) and the definition of digital (delivered "through digital products").

Why the other answers are wrong
A: This is the specific definition of a digital product, not a service.
C: This is the definition of digital transformation.
D: This is a general description of information management."""
        },
        {
            "id": 36,
            "question": "When implementing the 'collaborate and promote visibility' principle to an organization's initiative, which is NOT a required action?",
            "options": ["Ensuring everyone involved in the initiative agrees about it prior to starting", "Making decisions about the initiative on observable metrics", "Considering different methods of communication for various target groups", "Communicating details about the initiative to other parts of the organization"],
            "answer": "A",
            "rationale": """The principle of 'collaborate and promote visibility' focuses on involving the right people, emphasizing transparency. However, collaboration does not mean consensus. While input should be gathered, waiting for every single person to agree can lead to delays and "analysis paralysis."
Option A is the best answer because it describes "consensus," which is explicitly stated as not being a requirement of effective collaboration.

Why the other answers are wrong
B, C, and D are all necessary actions for effective collaboration and visibility."""
        },
        {
            "id": 37,
            "question": "What activity is responsible for resolving incidents?",
            "options": ["Support", "Design", "Operate", "Transition"],
            "answer": "A",
            "rationale": """In the ITIL Product and Service Lifecycle, Support is the activity specifically dedicated to restoring normal service operation when interruptions occur. It focuses on identifying issues, fixing them, and ensuring that users can continue to use the service effectively.
Option A is correct because the primary purpose of the "Support" activity is to identify and resolve incidents.

Why the other answers are wrong
B: Design happens before a service is live, so it does not deal with resolving active incidents.
C: Operate involves monitoring and maintaining systems, but the specific task of fixing broken services falls under Support.
D: Transition is responsible for moving new products into the live environment."""
        },
        {
            "id": 38,
            "question": "Which stakeholder oversee the procurement and use of services?",
            "options": ["Service provider", "Digital product vendor", "Service consumer", "Sponsors"],
            "answer": "C",
            "rationale": """In service management, the entity that receives the service, pays for it (or arranges for payment), and utilizes it to achieve their own objectives is categorized as the consumer.
Option C is the correct answer because a service consumer is the organization or entity responsible for the procurement and the actual use of services.

Why the other answers are wrong
A: The service provider delivers and supports the services.
B: A digital product vendor provides resources, rather than consuming them.
D: A sponsor specifically authorizes the budget for service consumption; they are a subset of the broader "Service consumer" role."""
        },
        {
            "id": 39,
            "question": "What most accurately characterizes the 'think and work holistically'?",
            "options": ["Encourage all staff to precisely recognize their service recipients", "Ensure that each iteration corresponds with the concept of a Minimum Viable Product / MVP", "Reduce complexity by focusing on executing limited tasks with superior quality", "Identify patterns in interactions between system elements to anticipate requirements"],
            "answer": "D",
            "rationale": """The 'think and work holistically' principle is based on the idea that no part of an organization or service exists in isolation. It involves understanding how different parts of the system interact, recognizing interdependencies, and seeing how a change in one area might impact the entire system.
Option D is the best choice because identifying patterns in interactions is a core application of holistic thinking.

Why the other answers are wrong
A: This is a key part of the 'Focus on value' principle.
B: This describes a technique used within the 'Progress iteratively with feedback' principle.
C: This is a primary goal of the 'Keep it simple and practical' principle."""
        },
        {
            "id": 40,
            "question": "Which of the following concentrates on securing and allocating necessary resources efficiently?",
            "options": ["Acquire", "Build", "Discover", "Deliver"],
            "answer": "A",
            "rationale": """The activity focused on resource management ensures that the organization has everything it needs (technology, people, or third-party components) to create and maintain its offerings.
Option A is the best choice because the primary purpose of the 'acquire' activity is to secure and allocate resources efficiently.

Why the other answers are wrong
B: Build focuses on actual development, integration, and testing.
C: Discover is an exploratory activity focused on understanding customer needs.
D: Deliver is concerned with the actual provision of services to users."""
        },
        {
            "id": 41,
            "question": "What is 'A formal description of one or more services designed to address the needs of a target consumer group. A service offering may include goods, access to resources, and service actions.'?",
            "options": ["service offering", "service actions", "service value", "service catalog"],
            "answer": "A",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 42,
            "question": "What is defined as 'A configuration of an organization's resources designed to offer value for a consumer.'?",
            "options": ["digital product", "product", "service offering", "digital service"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 43,
            "question": "What is 'A means of enabling value co-creation by facilitating outcomes that consumers want to achieve, without the consumer having to manage specific costs and risks.'?",
            "options": ["service level", "service quality", "service", "service action"],
            "answer": "C",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 44,
            "question": "What is 'A set of specialized organizational capabilities for enabling value for customers in the form of digital products and services.'?",
            "options": ["digital transformation", "digital product and service management", "digital service lifecycle", "digital value co-creation"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 45,
            "question": "What is 'A combination of an organization's resources based on digital technology and designed to offer value to consumers.'?",
            "options": ["digital service", "digital product", "digital asset", "digital platform"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 46,
            "question": "What is 'A service that fully or largely relies on digital products.'?",
            "options": ["digital product", "digital service", "digital offering", "digital outcome"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 47,
            "question": "What is 'A recurring organizational activity performed at all levels of an organization to ensure that the organization continually meets stakeholders' expectations.'?",
            "options": ["continual improvement", "continuous delivery", "continuous deployment", "continuous integration"],
            "answer": "A",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 48,
            "question": "What is 'The full set of stages, transitions, and associated statuses in the life of a service, product, practice, or other entity.'?",
            "options": ["service journey", "lifecycle", "value stream", "operating model"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 49,
            "question": "What are 'Tangible resources that are transferred or available for transfer from a service provider to a service consumer, together with ownership and associated rights and responsibilities.'?",
            "options": ["service actions", "access to resources", "goods", "digital products"],
            "answer": "C",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 50,
            "question": "What is 'The sum of the characteristics of a service that are relevant to its ability to satisfy stated and implied needs.'?",
            "options": ["service level", "service quality", "service value", "service warranty"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 51,
            "question": "What is 'A set of metrics that define expected or achieved service quality.'?",
            "options": ["service level", "service quality", "service utility", "service experience"],
            "answer": "A",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 52,
            "question": "What is 'The functionality offered by a product or service; often described as what the service does or fit for purpose.'?",
            "options": ["Warranty", "Utility", "Sustainability", "Reliability"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 53,
            "question": "What is 'Assurance that a product or service will meet agreed requirements; often described as how the service performs or fit for use.'?",
            "options": ["Utility", "Reliability", "Warranty", "Observability"],
            "answer": "C",
            "rationale": "This is a BL1 definition question, no need to explain. Please review and memorize the definition."
        },
        {
            "id": 54,
            "question": "What is 'The assurance that a product or service meets, and will continue to meet, requirements for environmental stewardship, social progress, and economic growth.'?",
            "options": ["Sustainability", "Governance", "Resilience", "Reliability"],
            "answer": "A",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 55,
            "question": "What is 'The sum of functional and emotional interactions with a service and provider as perceived by the user.'?",
            "options": ["customer experience (CX)", "user experience (UX)", "service journey", "human-centred design"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 56,
            "question": "What is 'The sum of functional and emotional interactions with a service and provider as perceived by a service customer.'?",
            "options": ["user experience (UX)", "customer experience (CX)", "service relationship", "value co-creation"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 57,
            "question": "What is 'A service agreement that measures and manages the actual user experience and outcomes of a service not just its technical performance.'?",
            "options": ["Service Level Agreement (SLA)", "Experience Level Agreement (XLA)", "Operational Level Agreement (OLA)", "Service Quality Agreement"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 58,
            "question": "What is 'A problem-solving approach that prioritizes the needs, experiences, and perspectives of the people for whom a solution is being designed.'?",
            "options": ["service design", "human-centred design (HCD)", "digital transformation", "complexity thinking"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 59,
            "question": "What is 'A short but complete description of the overall purpose and intentions of an organization.'?",
            "options": ["vision", "mission", "strategy", "operating model"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 60,
            "question": "What is 'A defined aspiration of what an organization would like to become in the future.'?",
            "options": ["mission", "strategy", "vision", "purpose"],
            "answer": "C",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        }
        part2 = [
        {
            "id": 61,
            "question": "What is 'The addition, modification, or removal of anything that could have a direct or indirect effect on products and services.'?",
            "options": ["transformation", "change", "incident", "release"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 62,
            "question": "What is 'The strategic adoption and integration of digital technologies into all areas of an organization, fundamentally changing how the organization operates and creates value.'?",
            "options": ["digital transformation", "digital management", "digital innovation", "digital evolution"],
            "answer": "A",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 63,
            "question": "What is 'The perceived benefits, usefulness, and importance of something.'?",
            "options": ["output", "outcome", "value", "utility"],
            "answer": "C",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 64,
            "question": "What is 'A tangible or intangible deliverable of an activity.'?",
            "options": ["outcome", "output", "product", "service action"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 65,
            "question": "What is 'A result for a stakeholder enabled by one or more outputs.'?",
            "options": ["output", "value", "outcome", "utility"],
            "answer": "C",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 66,
            "question": "What is 'An organization responsible for delivery and support of services.'?",
            "options": ["service consumer", "service provider", "digital product vendor", "sponsor"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 67,
            "question": "What is 'The sum of activities and interactions performed by organizations engaged in service relationships to fulfil their roles as a service provider and a service consumer.'?",
            "options": ["service level", "service journey", "service offering", "service action"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 68,
            "question": "What is 'The role that authorizes budget for service consumption.'?",
            "options": ["customer", "user", "sponsor", "provider"],
            "answer": "C",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 69,
            "question": "What is 'A documented agreement between a service provider and a customer that identifies the services provided and the agreed level of each service.'?",
            "options": ["Experience Level Agreement (XLA)", "Service Level Agreement (SLA)", "Service Contract", "Service Specification"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 70,
            "question": "What is 'A system of rules, policies, standards, processes, and controls organizations implement to manage their data assets effectively.'?",
            "options": ["information management", "data governance", "IT management", "knowledge management"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 71,
            "question": "What is 'A series of steps an organization undertakes to enable value for consumers through management of products and services.'?",
            "options": ["value", "value stream", "service journey", "operating model"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 72,
            "question": "What is 'The system by which an organization is directed and controlled.'?",
            "options": ["management", "leadership", "governance", "strategy"],
            "answer": "C",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 73,
            "question": "What is 'An unplanned interruption to a service or reduction in the quality of a service.'?",
            "options": ["problem", "error", "incident", "event"],
            "answer": "C",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 74,
            "question": "What is 'Any change of state that has significance for the management of a service or other configuration item.'?",
            "options": ["incident", "Event", "change", "alert"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 75,
            "question": "What is 'A version of a product, service, or other configuration item that is made available for use.'?",
            "options": ["Release", "Deployment", "Prototype", "Specification"],
            "answer": "A",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 76,
            "question": "What is 'The ability of a product, service, or other configuration item to perform its intended function for a specified period of time or number of cycles.'?",
            "options": ["warranty", "sustainability", "reliability", "utility"],
            "answer": "C",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 77,
            "question": "What is 'A cause, or potential cause, of one or more incidents.'?",
            "options": ["error", "problem", "known error", "disaster"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 78,
            "question": "What is 'A flaw or vulnerability that may cause incidents.'?",
            "options": ["problem", "incident", "error", "risk"],
            "answer": "C",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 79,
            "question": "What is 'A set of organizational resources and capabilities designed and adopted for performing work or accomplishing an objective.'?",
            "options": ["management practice", "operating model", "value stream", "service offering"],
            "answer": "A",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 80,
            "question": "What is 'A necessary precondition for the achievement of intended results.'?",
            "options": ["Metric", "Critical Success Factor (CSF)", "Key Performance Indicator (KPI)", "Service level"],
            "answer": "B",
            "rationale": "This is a BL1 definition question, so no explanation is needed. Please review and memorize the definition."
        },
        {
            "id": 81,
            "question": "What is the primary objective of the ITIL AI Capability Framework?",
            "options": ["To outline how service entities, users, and stakeholders engage with AI to generate mutual value", "To explain how enterprises can evaluate and enhance competencies for efficient utilization of AI", "To mandate particular AI tools necessary for service creation and management", "To gauge the effectiveness of AI-driven services relative to established service levels"],
            "answer": "B",
            "rationale": "The ITIL AI Capability Framework, often referred to as the 6C model (comprising Creation, Curation, Clarification, Cognition, Communication, and Coordination), is designed to provide a functional classification of AI solutions. Its primary purpose is to help organizations understand the various ways AI can be applied across different management areas so they can assess their current maturity and develop the specific organizational capabilities needed for effective AI integration. While AI certainly involves interactions for value co-creation, this specific model serves as a framework for organizations to identify what they need to \"be able to do\" with AI to support their digital products and services. It helps in tailoring risk profiles and management practices to the specific functions of AI solutions, ensuring that the adoption of technology is strategic rather than just a reaction to market trends."
        },
        {
            "id": 82,
            "question": "Why is project management vital within the ITIL framework?",
            "options": ["To handle daily operational tasks and service requests", "To establish governance oversight throughout the ITIL Value System", "To execute time-constrained endeavors that implement new or modified services", "To facilitate organized delivery of change while services continue to operate"],
            "answer": "D",
            "rationale": "Project management is a critical general management practice in ITIL because it provides the necessary structure to deliver significant changes such as the introduction of entirely new services or major architectural overhauls—while ensuring that existing services remain stable and operational. While projects are by definition time-bound initiatives, their specific importance within a service management framework like ITIL lies in the coordination of resources and the mitigation of risks during the transition phase. This structured approach allows an organization to innovate and evolve its service offerings in a controlled manner, preventing the \"siloed\" or chaotic implementation of changes that could lead to service outages. By balancing the need for rapid change with the requirement for operational stability, project management ensures that the value chain continues to function effectively even during periods of significant transformation."
        },
        {
            "id": 83,
            "question": "Which is the MAIN form of service engagement between service users and digital offerings?",
            "options": ["Transfer of physical items", "Delivery of products", "Access to resources", "Service-related activities"],
            "answer": "C",
            "rationale": "According to the ITIL 5 framework, access to resources is the primary form of interaction between service consumers and digital services because digital products typically rely on providing users with the ability to use a provider's infrastructure, applications, or data. In a digital context, this often means the consumer gains the right to use a software-as-a-service (SaaS) platform or a mobile application under specific terms and conditions without ever taking ownership of the underlying technology. While other forms of interaction like the transfer of goods (e.g., receiving a physical laptop) or service actions (e.g., a support desk agent fixing a bug) can occur, they are either rare or secondary in the digital realm. Emphasizing access to resources allows digital service providers to achieve high levels of scalability and availability, as digital assets can be accessed by a vast number of users simultaneously with minimal manual intervention from the provider's personnel."
        },
        {
            "id": 84,
            "question": "Which of the following is a primary success indicator for the 'transition' process?",
            "options": ["Speed of restoring regular service operations", "Quality of resources and services procured from external vendors", "Service performance measured against the established SLA objectives", "Number and impact of deployment errors"],
            "answer": "D",
            "rationale": "The 'transition' activity in the ITIL Product and Service Lifecycle focuses on deploying new or changed products into the live environment and ensuring effective onboarding or offboarding of suppliers. According to the ITIL Foundation (Version 5) content, key success metrics for the transition activity include transition cycle time, negative impact on service availability, and the number and impact of transition errors. Option D directly reflects this by focusing on deployment errors, which are a core indicator of how successful and stable the transition has been.\nOption A refers to the speed of restoring normal service, which is a metric of the support activity, not transition.\nOption B relates to the acquire activity, where supplier quality and outsourced resources are evaluated.\nOption C refers to the deliver activity, which measures service performance against SLA targets. Therefore, only option D aligns specifically with transition success metrics."
        },
        {
            "id": 85,
            "question": "What function does governance serve within the ITIL Service Value System?",
            "options": ["To establish and oversee process activities for delivering services", "To carry out day-to-day service operations", "To ensure organizational activities are guided and regulated", "To supply comprehensive technical direction for service design"],
            "answer": "C",
            "rationale": "Within the ITIL Value System, governance is defined as the system by which an organization is directed and controlled. It ensures that organizational activities, including digital product and service management, are aligned with strategic objectives and external requirements. Option C accurately reflects this purpose by stating that governance ensures activities are directed and controlled.\nOption A describes operational management and practice-level responsibilities, not governance.\nOption B refers to operational execution, which belongs to management and value chain activities rather than governance.\nOption D relates to service design practices and technical guidance, which fall under management practices rather than governance. Governance operates at a higher level, setting direction and oversight rather than executing detailed work."
        },
        {
            "id": 86,
            "question": "Which of the following activities BEST illustrates the transfer of goods within a service offering?",
            "options": ["A cloud user utilizes shared online storage", "A service provider delivers new laptops to the customer", "A customer obtains guidance from a helpdesk representative", "A team participates in a virtual training session"],
            "answer": "B",
            "rationale": "In ITIL, a service offering may include three forms of interaction: access to resources, service actions, and transfer of goods. Transfer of goods involves tangible items being provided to the consumer, typically with ownership or usage rights transferred. Option B, where a service provider supplies new laptops to the customer, clearly represents transfer of goods because physical equipment is delivered to the consumer.\nOption A describes access to resources, since the cloud user is accessing shared storage rather than receiving ownership of a physical item.\nOption C represents a service action, where advice is provided.\nOption D also represents a service action in the form of training. Therefore, only option B correctly reflects transfer of goods."
        },
        {
            "id": 87,
            "question": "Which of the following BEST defines an outcome within a service relationship?",
            "options": ["A result attained by a stakeholder through the use of one or more outputs", "A tangible or intangible deliverable produced during a service activity", "A specific activity completed by the service provider as part of service provision", "A software solution supplied to the consumer by the service provider"],
            "answer": "A",
            "rationale": "In ITIL, an outcome is defined as a result for a stakeholder enabled by one or more outputs. Option A directly reflects this definition by describing a result achieved through the use of outputs.\nOption B describes an output, which is a tangible or intangible deliverable of an activity.\nOption C describes an activity or task performed during service delivery, not an outcome.\nOption D describes a product or deliverable, not the result achieved by using it. Therefore, option A correctly captures the meaning of an outcome in a service relationship."
        },
        {
            "id": 88,
            "question": "What does sustainability ensure in the context of a service or product?",
            "options": ["The service will fulfill the agreed-upon requirements", "The service will consistently satisfy environmental responsibility standards", "The service provides the necessary functionality to address business needs", "The service enhances the performance of the consumer"],
            "answer": "B",
            "rationale": "In ITIL, sustainability is defined as the assurance that a product or service meets and will continue to meet requirements for environmental stewardship, social progress, and economic growth. Option B correctly reflects this by emphasizing continual fulfillment of environmental responsibility requirements.\nOption A refers to warranty, which assures that the service meets agreed requirements.\nOption C describes utility, meaning the service delivers required functionality.\nOption D also relates to utility, since it refers to supporting consumer performance. Sustainability goes beyond functionality and warranty by addressing long-term environmental and societal responsibility, which is why option B is correct."
        },
        {
            "id": 89,
            "question": "Which of the following BEST defines an operating model?",
            "options": ["A set of principles that ensures uniform decision-making and accountability across the organization", "A recommendation that directs an organization's actions and choices in various situations", "A set of organizational resources structured to carry out specific tasks or accomplish a defined objective", "A conceptual and visual depiction of how an organization collaboratively creates value with its customers"],
            "answer": "D",
            "rationale": "An operating model is defined as a conceptual and/or visual representation of how an organization co-creates value with its customers and other stakeholders, and how it runs itself. This aligns directly with option D.\nOption A refers to governance, which is the system by which an organization is directed and controlled, ensuring accountability and consistent decision-making.\nOption B describes guiding principles, which are recommendations that guide actions and decisions in all circumstances.\nOption C defines a management practice, which is a set of organizational resources designed to perform specific work or achieve an objective. Therefore, D best matches the formal definition of an operating model."
        },
        {
            "id": 90,
            "question": "Which option BEST clarifies why an organization may decide to engage external suppliers?",
            "options": ["To maintain increased control and transparency over service provision", "To minimize dependence on third-party vendors", "To remove the requirement for oversight, governance, and internal administration", "To obtain capabilities that are challenging to develop in-house"],
            "answer": "D",
            "rationale": "Organizations often engage external suppliers to access specialized expertise, technology, or capabilities that are difficult, costly, or time-consuming to develop internally. Option D reflects this strategic reason, as supplier engagement frequently enables organizations to focus on their core competencies while leveraging external subject matter expertise.\nOption A is incorrect because engaging external suppliers typically introduces shared control and requires structured oversight rather than increasing direct internal control.\nOption B contradicts the purpose of supplier engagement, as working with suppliers increases reliance on third parties rather than minimizing it.\nOption C is also incorrect because governance and oversight remain essential even when services are outsourced; responsibility cannot be transferred entirely. Thus, D is the best explanation."
        },
        {
            "id": 91,
            "question": "Which of the following terms BEST defines a change?",
            "options": ["An unplanned disruption to a service or a decrease in service quality", "The addition, alteration, or removal of anything that may impact a product or service", "Any component that must be managed to enable the delivery of an IT service", "The root cause of one or more incidents"],
            "answer": "B",
            "rationale": "A change is formally defined as the addition, modification, or removal of anything that could have a direct or indirect effect on products and services. Option B reflects this definition precisely.\nOption A describes an incident, which is an unplanned interruption or reduction in service quality.\nOption C describes a configuration item, which is any component that must be managed to deliver a service.\nOption D describes a problem, which is the underlying cause of one or more incidents. Therefore, B is the correct and most accurate description of a change."
        },
        {
            "id": 92,
            "question": "Which statement about a partnership relationship is TRUE?",
            "options": ["It focuses operational efficiency and relies on standardized agreements", "It concentrates on operational and tactical levels rather than the strategic level", "It delivers commercial off-the-shelf services to a broad range of customers", "It involves bespoke services with an emphasis on innovation and growth"],
            "answer": "D",
            "rationale": "A partnership relationship represents a collaborative type of service relationship focused on innovation, growth, and shared strategic objectives. It typically involves bespoke or customized services and high levels of trust and mutual investment. Option D accurately reflects this, as partnerships often center on innovation and long-term growth rather than simple transactional efficiency.\nOption A describes a basic relationship focused on operational efficiency and standardized contracts.\nOption B aligns more with cooperative relationships that operate mainly at operational and tactical levels rather than strategic ones.\nOption C also describes basic service relationships offering commercial off-the-shelf services to many consumers. Therefore, D correctly characterizes a partnership relationship."
        },
        {
            "id": 93,
            "question": "An organization intends to enhance an existing service and wants to assess its current performance before implementing any modifications. According to the principle 'start where you are,' what should the organization consider when evaluating the service's present performance?",
            "options": ["Involve individuals who have limited or no previous knowledge of the service", "Select the appropriate message and communication method for stakeholders", "Determine who the consumer is and the reasons they utilize the service", "Refrain from applying risk management when reusing existing processes"],
            "answer": "A",
            "rationale": "The principle 'start where you are' emphasizes objectively assessing the current state before making changes and avoiding assumptions. One recommended approach is to involve individuals who have little or no prior knowledge of the service, as they may notice issues that experienced staff overlook due to familiarity or bias. Option A reflects this idea directly.\nOption B relates to the principle 'collaborate and promote visibility,' which focuses on communication methods.\nOption C aligns with 'focus on value,' which emphasizes understanding consumers and outcomes.\nOption D is incorrect because risk management should always be applied when reusing or adapting existing processes; the principle does not suggest ignoring risks. Therefore, A best aligns with 'start where you are.'"
        },
        {
            "id": 94,
            "question": "Why do many digital service providers seek to minimize or eliminate service activities?",
            "options": ["To enhance direct personal interaction between users and support personnel", "To ensure that each service interaction is managed manually for improved oversight", "To adhere to financial and regulatory requirements", "To streamline operations and improve consistency by increasing reliance on automation"],
            "answer": "D",
            "rationale": "Digital service providers often design services so that access to resources becomes the primary form of service interaction, minimizing the need for manual service actions. The ITIL guidance explains that digital services aim to maximize scalability and consistency, which are more easily achieved through automation rather than human-performed service actions. Option D is correct because reducing service actions allows providers to streamline operations, increase reliability, and ensure consistent outcomes by relying on automated processes and digital platforms.\nOption A is incorrect because reducing service actions does not aim to increase personal engagement; in fact, it typically reduces direct human interaction.\nOption B is incorrect because manually handling every interaction contradicts the goal of efficiency and scalability in digital services.\nOption C is also incorrect because while compliance may influence design decisions, the primary reason for minimizing service actions is operational efficiency and scalability, not regulatory compliance."
        },
        {
            "id": 95,
            "question": "Which dimension of product and service management encourages the use of safe-to-fail experiments in complex environments?",
            "options": ["Organizations and personnel", "Value streams and processes", "Partners and vendors", "Info and technology"],
            "answer": "B",
            "rationale": "The 'Value streams and processes' dimension addresses workflows, adaptability, and how work is organized in different contexts, including complex environments. ITIL discusses complexity thinking and emphasizes that in complex situations, experimentation and iterative approaches are necessary because cause-and-effect relationships are not always predictable. Safe-to-fail experiments are aligned with adapting workflows to complexity, which is covered under value streams and processes.\nOption A is incorrect because while organizational culture supports experimentation, the dimension specifically tied to managing workflows and adapting them to complexity is value streams and processes.\nOption C is incorrect because partners and suppliers relate to external relationships rather than experimentation strategies.\nOption D is incorrect because information and technology focuses on data and tools, not on managing complexity through adaptive workflow experimentation."
        },
        {
            "id": 96,
            "question": "Which ITIL Guiding Principle highlights the importance of understanding how all components of an organization operate together as a unified system?",
            "options": ["Think and work holistically", "Focus on value", "Keep it simple and practical", "Progress iteratively with feedback"],
            "answer": "A",
            "rationale": "The ITIL Guiding Principle 'Think and work holistically' stresses that no product, service, practice, or team stands alone. It emphasizes understanding how all components of the organization interact and contribute to value creation. This principle promotes viewing the organization as an integrated system rather than isolated silos.\nOption B focuses on ensuring all activities contribute to stakeholder value but does not specifically address systemic integration.\nOption C emphasizes simplicity and elimination of unnecessary complexity rather than system-wide integration.\nOption D encourages iterative progress and feedback loops but does not specifically focus on holistic system thinking. Therefore, only option A directly aligns with understanding the organization as an integrated whole."
        },
        {
            "id": 97,
            "question": "Which activity is responsible for developing, integrating, and validating digital products to convert designs into operational solutions?",
            "options": ["Support", "Build", "Discover", "Operate"],
            "answer": "B",
            "rationale": "According to the ITIL Product and Service Lifecycle, the 'Build' activity is responsible for developing, integrating, and testing digital products based on approved designs. It transforms specifications and prototypes into functional solutions and includes validation and testing. Option B is therefore correct.\nOption A, Support, focuses on resolving incidents and restoring normal operations rather than creating solutions.\nOption C, Discover, is concerned with identifying needs and defining direction, not implementing solutions.\nOption D, Operate, ensures live products function correctly in production environments but does not involve development or testing of new solutions. Hence, Build is the only activity that matches the described purpose."
        },
        {
            "id": 98,
            "question": "Which of the following BEST defines a sponsor within a consumer organization?",
            "options": ["An individual or group that possesses its own responsibilities and authorities", "An individual or group that approves a change", "The role responsible for defining the requirements for a service", "The role that approves the budget for service consumption"],
            "answer": "D",
            "rationale": "In ITIL, within a service relationship, the sponsor is defined as the role that authorizes the budget for service consumption. The sponsor ensures that funding is approved and aligned with organizational priorities. Option D accurately reflects this definition.\nOption A describes an organization in general, not the sponsor role specifically.\nOption B refers to a change authority, which is responsible for approving changes, not funding service consumption.\nOption C describes the customer role, which defines service requirements and takes responsibility for outcomes, but does not authorize the budget. Therefore, only option D correctly describes the sponsor within a consumer organization."
        },
        {
            "id": 99,
            "question": "What facilitates the digital product and service management activities within an organization?",
            "options": ["Value stream stages", "Management practices", "Vision and operating framework", "Value chain"],
            "answer": "B",
            "rationale": "Management practices are the organizational capabilities that enable and support the digital product and service management activities. According to ITIL, each value chain activity is enabled and supported by several management practices, which combine resources, processes, competencies, tools, and roles to achieve specific objectives. These practices provide the structured capabilities required to perform activities such as discover, design, build, transition, operate, deliver, and support effectively.\nOption A is incorrect because value stream steps describe the actual flow of work performed to deliver value, but they are not what enable the activities themselves. They represent how work is carried out, not the capabilities that make it possible.\nOption C is incorrect because the vision and operating model define direction and structure, but they do not directly enable day-to-day lifecycle activities.\nOption D is incorrect because the value chain describes the set of activities performed to create value, but those activities are enabled by management practices, not by the value chain itself."
        },
        {
            "id": 100,
            "question": "Which of the following statements regarding the Four Dimensions of product and service management is CORRECT?",
            "options": ["Each dimension individually is adequate to accomplish the intended outcomes", "All Four Dimensions are essential for the effective and efficient enablement of value", "All Four Dimensions apply solely to product design and not to management practices", "All Four Dimensions primarily concentrate on the activities within the service value chain"],
            "answer": "B",
            "rationale": "All Four Dimensions—organizations and people, information and technology, partners and suppliers, and value streams and processes—are collectively critical to effective and efficient facilitation of value. ITIL emphasizes a holistic approach, meaning that no single dimension is sufficient on its own. All dimensions must be considered together to ensure balanced and successful digital product and service management.\nOption A is incorrect because ITIL explicitly states that none of the dimensions alone is sufficient to enable desired outcomes.\nOption C is incorrect because the Four Dimensions apply broadly to the entire value system, including management practices and lifecycle activities, not just product design.\nOption D is incorrect because while the Four Dimensions relate to value chain activities, they are not limited to focusing mainly on those activities; they represent broader perspectives relevant at all levels of the organization."
        },
        {
            "id": 101,
            "question": "A team is gathering customer feedback and measuring current service response times to understand its existing performance. Which step of the ITIL Continual Improvement Model does this activity represent?",
            "options": ["Where are we now?", "Take action", "Where do we want to be?", "What is the vision?"],
            "answer": "A",
            "rationale": "Gathering customer feedback and measuring current service response times corresponds to the step 'Where are we now?' in the ITIL Continual Improvement Model. This step focuses on assessing the current state of services, practices, and performance. It involves collecting objective data and stakeholder feedback to establish a baseline understanding of existing conditions before defining improvement targets.\nOption B is incorrect because 'Take action' refers to implementing planned improvement initiatives, not assessing the current state.\nOption C is incorrect because 'Where do we want to be?' defines the target state and desired outcomes, not the current performance.\nOption D is incorrect because 'What is the vision?' relates to understanding the broader organizational objectives and strategic context, not measuring existing service performance."
        },
        {
            "id": 102,
            "question": "How do service providers contribute to the generation of service value for consumers?",
            "options": ["They reduce risks and supply resources through specialization", "They eliminate the requirement for consumers to utilize any resources", "They substitute consumers' responsibilities with their own services", "They directly determine the financial results for consumers"],
            "answer": "A",
            "rationale": "Service providers contribute to service value by facilitating desired outcomes for consumers while helping them avoid managing certain costs and risks. Through specialization, service providers develop expertise, skills, and resources that allow them to reduce or manage specific risks and costs more effectively than consumers could on their own. This aligns directly with the ITIL definition of a service as a means of enabling value co-creation without the consumer having to manage specific costs and risks.\nOption B is incorrect because service consumption always requires some consumer resources, even if the provider reduces certain burdens.\nOption C is incorrect because providers do not replace all consumer responsibilities; value is co-created, and consumers still retain certain responsibilities.\nOption D is incorrect because financial outcomes depend on the consumer's context and decisions; providers facilitate outcomes but do not directly determine financial results."
        },
        {
            "id": 103,
            "question": "Performing routine activities such as backups, monitoring, and recording and processing events is associated with which of the following activities?",
            "options": ["Deliver", "Support", "Operate", "Transition"],
            "answer": "C",
            "rationale": "Routine tasks such as backups, monitoring, and capturing and processing events are part of the 'Operate' activity in the ITIL Product and Service Lifecycle. The purpose of the operate activity is to maintain and monitor digital products and supporting systems to ensure optimal performance and reliability. It includes routine operational tasks that keep products functioning as designed, such as monitoring systems, managing events, running backups, and maintaining operational stability.\nOption A is incorrect because 'Deliver' focuses on providing services to users and managing service interactions, not on maintaining product operations.\nOption B is incorrect because 'Support' focuses on responding to incidents and restoring service when disruptions occur, rather than routine operational maintenance.\nOption D is incorrect because 'Transition' involves deploying new or changed products into the live environment, not ongoing operational activities."
        },
        {
            "id": 104,
            "question": "Which term BEST defines a group of individuals that possesses its own functions, including responsibilities, authorities, and relationships, to accomplish its objectives?",
            "options": ["Organization", "Partnership", "Culture", "Service Journey"],
            "answer": "A",
            "rationale": "The definition given in the question matches precisely the ITIL glossary definition of an organization, which is described as a person or group of people that has its own functions with responsibilities, authorities, and relationships to achieve its objectives. An organization can refer to an entire company, a department, or even a structured team within a company. A partnership, while it may involve cooperation between entities, is specifically a relationship between two organizations working together toward shared goals, not the structured entity itself. Culture refers to shared values, beliefs, and behaviors within a group, which influence how people act but do not define the formal structure of responsibilities and authorities. A service journey describes the sequence of interactions and activities between a service provider and consumer, not a structured group with defined objectives and roles. Therefore, 'organization' is the best and most accurate term."
        },
        {
            "id": 105,
            "question": "What is meant by a product prototype?",
            "options": ["A request that initiates an agreed service action", "The procedure for deploying new or updated products to users", "An initial version of a product that demonstrates its fundamental form and functionality", "A completed product specification authorized for development"],
            "answer": "C",
            "rationale": "A product prototype is defined as an initial version of a product that demonstrates its basic form, functionality, and operational capabilities. It is used to test and refine the design and validate assumptions before full development or large-scale release.\nOption A describes a service request, which is a request that initiates a service action.\nOption B refers to release management or deployment activities, which concern making products available to users.\nOption D describes a product specification, which is a documented description of requirements and characteristics, not a working or demonstrable version of the product. Therefore, only option C aligns with the formal definition of a product prototype in ITIL guidance."
        },
        {
            "id": 106,
            "question": "A telecommunications provider develops an enterprise solution that integrates internet connectivity, VoIP, network security, and technical support. Which concept does this example demonstrate?",
            "options": ["Transfer of products", "Service take action", "Access to resources", "Service offering"],
            "answer": "D",
            "rationale": "The scenario describes combining multiple services into a structured package designed to meet the needs of a specific consumer group. In ITIL terminology, this is a service offering, which is a formal description of one or more services designed to address the needs of a target consumer group. It may include access to resources, service actions, and possibly goods.\nTransfer of products refers specifically to the movement of tangible resources from provider to consumer.\nService take action refers to an activity performed by the provider or jointly with the consumer.\nAccess to resources refers to providing the consumer with access to systems or infrastructure. While the package may include access and actions, the key concept illustrated is the bundling and formal presentation of multiple services as a structured offering. Therefore, service offering is the correct concept."
        },
        {
            "id": 107,
            "question": "Which statement BEST defines service quality?",
            "options": ["The totality set of characteristics of a service that determines its capability to fulfill specified needs", "The functionality delivered by a product or service to address a particular requirement", "A formal agreement between a service provider and a customer", "The assurance that a service satisfies agreed requirements and is suitable for use"],
            "answer": "A",
            "rationale": "Service quality in ITIL is defined as the sum or totality of characteristics of a service that determine its ability to satisfy stated and implied needs. This aligns directly with option A.\nOption B describes utility, which refers specifically to the functionality of a service and answers the question of what the service does.\nOption C describes a Service Level Agreement (SLA), which is a documented agreement between a provider and a customer.\nOption D describes warranty, which refers to assurance that a service will meet agreed requirements and is fit for use. Since service quality encompasses utility, warranty, sustainability, and experience characteristics collectively, option A provides the most complete and accurate definition."
        },
        {
            "id": 108,
            "question": "Which approach to software development allows software to be released to production at any point once the team makes the decision?",
            "options": ["CD (Continuous deployment)", "CI (Continuous integration)", "CD (Continuous delivery)", "DevOps"],
            "answer": "C",
            "rationale": "Continuous delivery is defined as a set of techniques and tools that enables software updates to be deployed to production at any time, once the team decides to do so. The key distinction is that deployment is possible at any time but still requires an explicit decision.\nContinuous deployment, by contrast, automatically deploys every change that passes automated tests without additional human authorization.\nContinuous integration focuses on frequently merging code changes and running automated builds and tests, but it does not inherently enable production release at any time.\nDevOps is a broader cultural and professional movement that integrates development and operations but is not a specific release approach. Therefore, continuous delivery best matches the description provided in the question."
        },
        {
            "id": 109,
            "question": "What is meant by a value stream?",
            "options": ["A collection of organizational resources and capabilities used to accomplish an objective", "A series of steps a company performs to facilitate value for consumers through the management of products and services", "A tangible or intangible output generated by an activity", "A arrangement of an organization's resources structured to deliver value to a consumer"],
            "answer": "B",
            "rationale": "A value stream is defined in ITIL as a series of steps that an organization undertakes to create and deliver value to consumers through the management of products and services. Option B correctly reflects this definition, as it emphasizes the flow of activities that enable value creation.\nOption A describes a management practice or organizational capability, not a value stream.\nOption C refers to an output, which is a deliverable of an activity.\nOption D describes a product, which is a configuration of resources designed to offer value, but not the end-to-end flow of activities that constitute a value stream."
        },
        {
            "id": 110,
            "question": "Which dimension of digital product and service management ensures that individuals within an organization possess adequate skills to meet anticipated demands?",
            "options": ["Organizations and people", "Value streams and processes", "Information and technology", "Partners and suppliers"],
            "answer": "A",
            "rationale": "The 'Organizations and people' dimension focuses on organizational structure, roles, culture, leadership, skills, and competencies. It ensures that individuals and teams have the necessary capabilities to meet current and anticipated needs.\nOption B concerns workflows and processes, not workforce skills.\nOption C addresses data, information, and technology infrastructure rather than people's competencies.\nOption D focuses on third-party relationships and suppliers. Therefore, the dimension responsible for ensuring sufficient skills and competencies is Organizations and people."
        },
        {
            "id": 111,
            "question": "Which value chain activity is evaluated by reviewing the quality of resources and services obtained from an external provider?",
            "options": ["Build", "Design", "Acquire", "Discover"],
            "answer": "C",
            "rationale": "The 'Acquire' value chain activity focuses on securing and allocating necessary resources, including those sourced from third parties. Evaluating the quality of externally sourced resources and services is a key part of this activity.\nOption A (Build) refers to developing and testing digital products.\nOption B (Design) concerns creating specifications and prototypes.\nOption D (Discover) focuses on identifying needs and opportunities. Since assessing third-party sourced resources directly relates to procurement and allocation, the correct answer is Acquire."
        },
        {
            "id": 112,
            "question": "The board of directors endorses a new digital strategy and instructs management to prioritize investment in cloud infrastructure to enable future expansion. Which governance activity does this illustrate?",
            "options": ["Monitor", "Evaluate", "Direct", "Engage / Engage stakeholders"],
            "answer": "C",
            "rationale": "In ITIL governance, the 'Direct' activity involves setting strategic direction and assigning responsibility for implementing strategy and policies. When the board approves a digital strategy and instructs management to prioritize investment, it is providing direction.\nOption A (Monitor) involves overseeing performance against strategy.\nOption B (Evaluate) refers to assessing organizational performance and context.\nOption D (Engage stakeholders) involves identifying and aligning stakeholders. Because the board is establishing direction and instructing management, the correct governance activity is Direct."
        },
        {
            "id": 113,
            "question": "Which component of the operating model refers to external parties contributing to value creation activities?",
            "options": ["Partners and suppliers", "Value streams and processes", "Value chain", "Organizations and people"],
            "answer": "A",
            "rationale": "Within the ITIL operating model, the 'Partners and suppliers' dimension refers to third-party organizations that contribute to value creation activities, including external vendors, service providers, and strategic partners.\nOption B (Value streams and processes) relates to workflows and how work flows across the organization.\nOption C (Value chain) represents the high-level activities that enable value creation.\nOption D (Organizations and people) concerns internal structure and competencies. Since the question specifically refers to third parties contributing to value creation, the correct answer is Partners and suppliers."
        },
        {
            "id": 114,
            "question": "Why is it essential to obtain feedback before, during, and after each iteration?",
            "options": ["To record all activities comprehensively prior to beginning the next iteration", "To ensure the project plan stays fixed and unaltered throughout development", "To enable the team to adhere to the original design without disruption", "To ensure that each iteration remains aligned with evolving circumstances"],
            "answer": "D",
            "rationale": "Seeking feedback before, during, and after each iteration ensures that the work remains relevant and aligned with evolving stakeholder needs, environmental changes, and organizational priorities. According to the ITIL Guiding Principle 'Progress iteratively with feedback,' feedback loops help organizations adapt to changing circumstances and adjust direction as necessary.\nOption A is incorrect because feedback is not primarily about documenting activities; documentation is a separate governance and control activity.\nOption B is incorrect because iterative approaches assume that plans may change in response to new information, rather than remain fixed.\nOption C is incorrect because the purpose of feedback is not to preserve the original design unchanged but to refine and improve it. Only option D reflects the core purpose of feedback in iterative development: maintaining alignment with dynamic conditions and stakeholder expectations."
        },
        {
            "id": 115,
            "question": "Which part of an ITIL practice guide offers guidance for the effective automation of the practice?",
            "options": ["Information and technology", "Partners and suppliers", "Organizations and people", "Value streams and processes"],
            "answer": "A",
            "rationale": "In the structure of ITIL, the 'Information and technology' chapter includes guidance on automation and tooling. This section describes key information used by the practice and provides recommendations for successful automation.\nOption B is incorrect because the 'Partners and suppliers' chapter focuses on dependencies and third-party support.\nOption C is incorrect because 'Organizations and people' addresses roles, competencies, and organizational structures rather than automation guidance.\nOption D is incorrect because 'Value streams and processes' explains workflows and how the practice contributes to value streams, not automation recommendations. Therefore, the correct chapter for automation guidance is 'Information and technology.'"
        },
        {
            "id": 116,
            "question": "Which of the following statements regarding value streams is INCORRECT?",
            "options": ["Value streams are enabled and supported by the organization's value chain", "Value streams should omit suppliers", "Value streams continuously develop over time", "Value streams may involve many practices"],
            "answer": "B",
            "rationale": "Value streams represent end-to-end flows of work, information, and value creation, and they can involve internal teams as well as external partners and suppliers. Option B is incorrect because value streams should not exclude suppliers; in fact, many value streams depend on third-party services and supplier contributions.\nOption A is correct because value streams are enabled and supported by the organization's value chain and management practices.\nOption C is correct because value streams are dynamic and continue to evolve as circumstances, technologies, and stakeholder needs change.\nOption D is correct because value streams typically involve multiple management practices working together to enable value creation. Therefore, the incorrect statement is B."
        },
        {
            "id": 117,
            "question": "Which of the following BEST defines a release?",
            "options": ["The addition, alteration, or removal of anything that may impact services", "A version of a product, service, or other configuration item that is made available for use", "An unplanned disruption to a service or a decrease in service quality", "A cause, or possible cause, of one or more incidents"],
            "answer": "B",
            "rationale": "A release is defined in ITIL as a version of a product, service, or other configuration item that is made available for use. This aligns directly with option B.\nOption A describes a change, which is broader and refers to any addition, modification, or removal that could affect services.\nOption C defines an incident, which refers to an unplanned interruption or reduction in service quality.\nOption D defines a problem, which is a cause or potential cause of one or more incidents. Therefore, the best description of a release is option B."
        },
        {
            "id": 118,
            "question": "Which of the following is NOT included among the digital product and service lifecycle management activities?",
            "options": ["Acquire", "Agree", "Discover", "Build"],
            "answer": "B",
            "rationale": "The ITIL Product and Service Lifecycle includes the activities Discover, Design, Acquire, Build, Transition, Operate, Deliver, and Support. 'Agree' is not one of the lifecycle management activities; rather, 'Agree' is a step within the ITIL Service Journey Model related to establishing service relationships.\nOption A (Acquire), option C (Discover), and option D (Build) are all legitimate lifecycle management activities. Therefore, the correct answer is B, as it does not belong to the digital product and service lifecycle management activities."
        },
        {
            "id": 119,
            "question": "In what way should the ITIL Guiding Principles be integrated when an organization is making a decision?",
            "options": ["By applying all of the guiding principles equally when making any decision", "By choosing one guiding principle to serve as the primary foundation for every decision", "By evaluating each guiding principle to determine its relevance prior to implementing it", "By utilizing the 'keep it simple and practical' principle along with one or two additional principles that are applicable to the specific decision"],
            "answer": "C",
            "rationale": "Organizations should not use just one or two of the principles but should consider the relevance of each of them and how they complement each other. There is no particular order or hierarchy of these principles; they are equally important... However, in any given situation, some principles may be more critical than others."
        }
    ]

    return part1 + part2
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
