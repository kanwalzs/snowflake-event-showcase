import streamlit as st
from datetime import datetime

# --- 1. CONFIGURATION AND MOCK DATA ---
# Set the page configuration for a professional look and use a dark theme
st.set_page_config(
    page_title="Snowflake at PyTorch Conference 2025",
    page_icon="❄️", # Snowflake icon
    layout="wide",
    initial_sidebar_state="expanded" 
)

# Mock data for the event, company, and schedule
TEAM_NAME = "Snowflake Developer Relations"
EVENT_NAME = "PyTorch Conference 2025"
BOOTH_LOCATION = "Main Expo Hall, Booth S-20 (near the ML Track)"
BOOTH_HOURS = "Wednesday & Thursday, 9:00 AM - 5:00 PM"

SESSIONS = [
    {
        "title": "Scaling GenAI Inference with Snowpark Containers",
        "speaker": "Alice Johnson (Lead ML Advocate)",
        "time": "Wed, Oct 22 | 11:00 AM - 11:45 AM",
        "location": "ML Track Stage 1 (Room 302)",
        "summary": "A deep dive into deploying high-throughput PyTorch models for inference using Snowpark Containers, focusing on resource optimization and security."
    },
    {
        "title": "Data Governance for PyTorch Feature Engineering",
        "speaker": "Bob Chen (Data Governance Architect)",
        "time": "Thu, Oct 23 | 2:00 PM - 2:45 PM",
        "location": "Data & Ethics Stage (Room 105)",
        "summary": "Learn how Snowflake's governance framework ensures compliance and auditability for features used in PyTorch training pipelines."
    }
]

PROJECTS = [
    {
        "title": "Snowpark for PyTorch Model Training",
        "icon": "🧠",
        "summary": "Training PyTorch models directly within Snowflake using Snowpark containers.",
        "details": "See how to eliminate data movement by running your custom PyTorch training loops inside Snowflake's secure, scalable environment. This demo includes a distributed training example.",
        "tech": ["Snowpark", "PyTorch", "Python", "MLOps"]
    },
    {
        "title": "Zero-Copy Data Access with Iceberg & Snowpark",
        "icon": "🧊",
        "summary": "Showcasing PyTorch data loading from external Iceberg tables without data movement.",
        "details": "Explore our solution for seamless, high-performance data loading from Apache Iceberg tables stored outside Snowflake, all integrated with your PyTorch data pipelines.",
        "tech": ["Iceberg", "Snowpark", "PyTorch DataLoaders"]
    },
    {
        "title": "LLM Fine-Tuning Sandbox",
        "icon": "🤖",
        "summary": "An interactive demo showing the fine-tuning of a small LLM using a PyTorch pipeline and Snowflake data.",
        "details": "Attendees can provide input data and see the model fine-tuning process start in real-time, demonstrating the power of Snowpark's compute environment for custom GenAI projects.",
        "tech": ["LLM", "PyTorch", "Snowpark Container Services", "Gemini API (Data Prep)"]
    }
]

TEAM_MEMBERS = [
    {"name": "Alice Johnson", "role": "Lead ML Advocate", "linkedin": "alice-j-sf"},
    {"name": "Bob Chen", "role": "Data Governance Architect", "linkedin": "bob-c-sf"},
    {"name": "Carol Diaz", "role": "Senior DevRel Engineer", "linkedin": "carol-d-sf"},
]


# --- 2. SIDEBAR NAVIGATION ---
st.sidebar.title(f"❄️ {TEAM_NAME}")
st.sidebar.markdown(f"**Event:** **[{EVENT_NAME}](https://pytorch.org/event/pytorch-conference-2025/)**")
st.sidebar.markdown("---")

# Navigation menu
menu = st.sidebar.radio(
    "Go to Section",
    ["🚀 Overview", "🗓️ Schedule & Sessions", "📦 Projects & Demos", "👥 Our Team", "📝 Contact & Outreach"]
)
st.sidebar.markdown("---")


# --- 3. MAIN CONTENT RENDERING LOGIC ---

if menu == "🚀 Overview":
    st.title(f"Snowflake at {EVENT_NAME}")
    st.header("Build Better AI with Snowpark and PyTorch")

    st.markdown("""
        The Snowflake Developer Relations team is excited to be at the PyTorch Conference 2025!
        We are showcasing how **Snowpark** and **Snowpark Container Services** provide a 
        secure, scalable, and powerful environment to build, train, and deploy your 
        PyTorch models without ever moving your data.

        **Stop by our booth for live code examples, swag, and 1:1 sessions with our architects!**
        
        ---
    """)

    # Event highlight callout
    st.info(f"""
        **Find Our Booth!** We are located at **{BOOTH_LOCATION}**. 
        We'll be here **{BOOTH_HOURS}** to discuss your PyTorch and ML challenges.
    """)
    

elif menu == "🗓️ Schedule & Sessions":
    st.title("🗓️ Conference Schedule & Key Sessions")
    
    st.markdown(f"**Booth Hours:** {BOOTH_HOURS} | **Location:** {BOOTH_LOCATION}")
    st.markdown("---")
    
    st.header("Featured Sessions")
    st.markdown("Join our team for these technical deep-dives on Snowpark + PyTorch integration.")

    for session in SESSIONS:
        st.subheader(f"Session: {session['title']}")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            # Use st.metric for a clear, high-impact display of time/location
            st.markdown(f"**{session['time']}**")
            st.markdown(f"**Room:** {session['location']}")
            st.caption(f"Speaker: {session['speaker']}")
        with col2:
            st.markdown(f"*{session['summary']}*")
        st.markdown("---")
        
    st.markdown("## Live Demo Schedule at the Booth")
    st.markdown("Ask any of our team members for a live demonstration of these projects!")


elif menu == "📦 Projects & Demos":
    st.title(":package: Featured Projects & Code Demos")
    st.markdown("All demos showcase PyTorch integration running directly within the Snowflake Data Cloud.")

    for i, project in enumerate(PROJECTS):
        # Use a container for a nicer visual separation
        with st.container(border=True):
            st.subheader(f"{project['icon']} {project['title']}")

            # Summary and Tech stack in a single line
            st.caption(f"**Summary:** {project['summary']}")
            
            # Use an expander for details
            with st.expander("Show Details"):
                st.markdown(f"**Project Goal:** {project['details']}")
                st.markdown(f"**Core Stack:** `{'` | `'.join(project['tech'])}`")
                
                if st.button(f"Request Live Demo of {project['title'].split(':')[0]}", key=f"demo_btn_{i}"):
                    st.balloons()
                    st.success(f"A team member will be notified about your interest in the {project['title'].split(':')[0]} demo!")

        st.markdown("\n") # Add a small break

elif menu == "👥 Our Team":
    st.title(":busts_in_silhouette: Meet the Snowflake DevRel Team")
    st.markdown("These are the experts available at the booth. Feel free to connect with them and ask about Snowpark for ML!")

    # Use columns to create a neat, responsive grid layout
    cols = st.columns(len(TEAM_MEMBERS))

    for i, member in enumerate(TEAM_MEMBERS):
        with cols[i]:
            st.image(
                f"https://placehold.co/150x150/2c97e8/ffffff?text={member['name'].split(' ')[0]}", # Snowflake blue accent
                caption=member["name"],
                use_column_width="always"
            )
            st.markdown(f"**{member['role']}**")
            st.markdown(f"[:link: Connect on LinkedIn](https://linkedin.com/in/{member['linkedin']})")
            st.markdown("---")

elif menu == "📝 Contact & Outreach":
    st.title("📝 Contact & Outreach")
    st.markdown("The Snowflake Developer Relations team is eager to connect with you. Use the form below to initiate a follow-up or subscribe to our event updates.")

    # General Contact Info
    st.subheader("Booth & General Contact")
    st.markdown(f"""
        - **Booth:** {BOOTH_LOCATION}
        - **Email:** devrel@snowflake.com
    """)
    
    st.markdown("---")

    # Specialized Contact Form with Opt-in
    st.subheader("Connect with DevRel")
    
    with st.form("contact_form"):
        st.markdown("Please provide your details below.")
        
        name = st.text_input("Your Name *", key="contact_name")
        email = st.text_input("Your Email *", key="contact_email")
        
        st.markdown("---")
        
        # New required options
        contact_request = st.checkbox(
            "✅ I would like a Snowflake DevRel team member to follow up with me directly regarding my PyTorch project.", 
            value=False
        )
        opt_in = st.checkbox(
            "🚀 Opt-in: Receive occasional emails about future developer events and new PyTorch/Snowflake integrations.", 
            value=True
        )
        
        question = st.text_area("Your Question or Project Idea (Optional)", height=100)
        
        submitted = st.form_submit_button("Submit & Connect")

        if submitted:
            if not name or not email:
                 st.error("Please provide your Name and Email (required fields) to submit.")
            else:
                # In a real app, this data would be sent to a CRM/database.
                st.success(f"Thank you, {name}! Your connection request has been sent to the DevRel team.")
                st.info(f"Follow-up requested: {'Yes' if contact_request else 'No'}. Opt-in for updates: {'Yes' if opt_in else 'No'}.")
                st.balloons()
                
                # Print to console for demonstration purposes
                print(f"--- New Contact Request ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---")
                print(f"Name: {name}, Email: {email}")
                print(f"Follow-up: {contact_request}, Opt-in: {opt_in}")
                print(f"Question: {question or 'N/A'}")
                print("-------------------------------------------------------")


# --- 4. FOOTER ---
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: gray;'>Powered by Streamlit | {TEAM_NAME} @ {EVENT_NAME}</p>", unsafe_allow_html=True)
