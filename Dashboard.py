import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="AlgoU Dashboard", layout="wide")

# CSS Styling
st.markdown("""
<style>
h1 {
    text-align: center;
    font-size: 3rem;
    margin-top: 30px;
    color: white;
}
.navbar {
    display: flex;
    justify-content: space-evenly;
    margin-top: 40px;
    margin-bottom: 30px;
    font-size: 1.2rem;
    font-weight: 600;
}
.nav-link:link,
.nav-link:visited,
.nav-link:active {
    color: white;
    text-decoration: none;
    border-bottom: 2px solid transparent;
    padding-bottom: 5px;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 8px 18px;
}
.nav-link:hover {
    color: #dddddd;
    text-decoration: none;
}
.nav-active:link,
.nav-active:visited {
    color: #1E90FF;
    border-bottom: 3px solid #1E90FF;
    text-decoration: none;
}
.responsive-table {
    overflow-x: auto;
    margin-top: 20px;
}
.responsive-table table {
    width: 100%;
    border-collapse: collapse;
}
.responsive-table th, .responsive-table td {
    padding: 12px 16px;
    text-align: left;
    border-bottom: 1px solid #444;
    color: white;
}
.responsive-table th {
    background-color: #333;
}
.responsive-table tr:nth-child(even) {
    background-color: #2a2a2a;
}
.responsive-table thead th {
    position: sticky;
    top: 0;
    background-color: #222;
    z-index: 2;
}
.css-1kyxreq > div {
    gap: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>AlgoU Interview Prep</h1>", unsafe_allow_html=True)

# Session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "questions"

# Navigation logic
nav_items = {
    "questions": "📋 Questions",
    "insights": "📊 Insights",
    "contact": "📮 Contact Us"
}
query_params = st.query_params
if "nav" in query_params:
    st.session_state.page = query_params["nav"]

# Navigation bar
nav_html = '<div class="navbar">'
for key, label in nav_items.items():
    class_name = "nav-link"
    nav_url = f"/?nav={key}"
    if st.session_state.page == key:
        class_name += " nav-active"
    nav_html += f'<a href="{nav_url}" class="{class_name}">{label}</a>'
nav_html += '</div>'
st.markdown(nav_html, unsafe_allow_html=True)

# Load Data
sheet_url = "https://docs.google.com/spreadsheets/d/1n7uom7PM_54I5QmaZ0AEhjOBBzo742pTt2dJRae6ypM/export?format=csv"
df = pd.read_csv(sheet_url)

# Normalize Round Type
def normalize_round_type(val):
    val = str(val).lower()
    if "technical" in val:
        return "Technical Interview"
    elif "online" in val or "oa" in val:
        return "Online Assessment"
    elif "system design" in val:
        return "System Design Interview"
    elif "lld" in val or "machine-coding" in val:
        return "LLD Interview"
    elif "screening" in val:
        return "Screening Interview"
    elif "phone screen" in val:
        return "Phone Screen"
    elif "hr" in val:
        return "HR Interview"
    elif "written" in val:
        return "Written Test"
    elif "face-to-face" in val or "f2f" in val:
        return "Face To Face"
    else:
        return val.title()

df["Round Type"] = df["Round Type"].apply(normalize_round_type)

# Normalize Topics for filtering
def normalize_topic(topic):
    topic = str(topic).lower()
    if "array" in topic:
        return "Arrays"
    elif "string" in topic:
        return "Strings"
    elif "linked list" in topic:
        return "Linked Lists"
    elif "binary tree" in topic:
        return "Binary Trees"
    elif "tree" in topic:
        return "Trees"
    elif "graph" in topic:
        return "Graphs"
    elif "dp" in topic or "dynamic" in topic:
        return "Dynamic Programming"
    elif "greedy" in topic:
        return "Greedy"
    elif "backtracking" in topic:
        return "Backtracking"
    elif "heap" in topic or "priority" in topic:
        return "Heap / Priority Queue"
    elif "stack" in topic:
        return "Stacks"
    elif "queue" in topic:
        return "Queues"
    elif "math" in topic:
        return "Math / Number Theory"
    elif "recursion" in topic:
        return "Recursion"
    elif "sliding window" in topic:
        return "Sliding Window"
    elif "two pointer" in topic:
        return "Two Pointers"
    elif "binary search" in topic:
        return "Binary Search"
    elif "sorting" in topic:
        return "Sorting"
    elif "prefix" in topic or "suffix" in topic:
        return "Prefix/Suffix Sum"
    elif "simulation" in topic:
        return "Simulation"
    elif "design" in topic:
        return "System / LLD Design"
    elif "hash" in topic:
        return "Hashing"
    elif "bit" in topic:
        return "Bit Manipulation"
    elif "interval" in topic:
        return "Intervals"
    elif "matrix" in topic:
        return "Matrix"
    else:
        return topic.title()

df["Normalized Topic"] = df["Topic"].apply(normalize_topic)

# Clean Hyperlinks
df["Question Link"] = df["Question Link"].apply(lambda url: f'<a href="{url}" target="_blank">🔗 Question</a>')
df["Blog Link"] = df["Blog Link"].apply(lambda url: f'<a href="{url}" target="_blank">📖 Blog</a>')

# Predefined insights data
insights_data = {
    "Company": ["Google", "Uber", "Salesforce", "Microsoft", "Intuit"],
    "Insights": [
        (
            "**🧠 What They Ask:**\n"
            "- Focuses heavily on **DSA** (Graphs, Trees, DP, Binary Search, Recursion).\n"
            "- High-level problem solving expected with strong optimization.\n"
            "- Interviews emphasize **system design** for SDE-1+ (sharding, consistency, scalability).\n"
            "- Coding rounds are time-bound with clear expectations for clean and tested code.\n"
            "- Googleyness and leadership traits assessed during behavioral rounds.\n"
            "\n**🚀 Pro Tips:**\n"
            "* Practice **LeetCode hard-tagged questions**.\n"
            "* Strong understanding of **time-space tradeoffs** and system design patterns. ⏱\n" # Kept time emoji as it was explicitly mentioned to be kept in previous iterations, but now removing others.
            "* Study Google's open-source design docs (Spanner, BigTable, etc.) to understand scale."
        ),
        (
            "**🧠 What They Ask:**\n"
            "- Known for **graph-based problems**, BFS/DFS, and DP.\n"
            "- Real-world simulation problems like ride assignment or surge pricing logic are common.\n"
            "- SDE-1/2 expected to handle **LLD** like cab booking or delivery systems.\n"
            "- Emphasizes scalability and fault-tolerance in system design.\n"
            "\n**🚀 Pro Tips:**\n"
            "* Brush up on **Graphs** (shortest path, cycles, topological sort).\n"
            "* Be fluent with maps/sets in your language of choice (Python/Java).\n"
            "* Prepare for concurrency and real-time system questions."
        ),
        (
            "**🧠 What They Ask:**\n"
            "- Asks standard **DSA** in OAs: Arrays, Strings, Trees, Binary Search.\n"
            "- **System Design** expected for SDE-1+ (e.g., ticketing system, URL shortener).\n"
            "- **LLD** often includes class designs like Parking Lot, Library.\n"
            "- OA contains MCQs around DB, OS, OOP.\n"
            "\n**🚀 Pro Tips:**\n"
            "* Focus on **clean code** and debugging ability.\n"
            "* Be ready to discuss trade-offs in your design decisions.\n"
            "* Behavioral interviews test culture fit and project ownership."
        ),
        (
            "**🧠 What They Ask:**\n"
            "- **DSA is king**: Graphs (toposort, BFS), DP, Trees, Sliding Window, Tries.\n"
            "- Typically 3+ rounds: 1 OA, 2–3 Technical, 1 Design (SDE-1/2), 1 HR.\n"
            "- **System Design** and **LLD** expected for SDE-1/2. Questions are deep and open-ended.\n"
            "- Emphasis on clarity of thought, testing code, and debugging.\n"
            "\n**🚀 Pro Tips:**\n"
            "* **LeetCode medium-to-hard** tagged “Microsoft” are often reused.\n"
            "* Prepare **Binary Search** on answer-type problems.\n"
            "* Practice **object-oriented design** like Snake Game, BookMyShow."
        ),
        (
            "**🧠 What They Ask:**\n"
            "- Focus on real-world coding challenges (simulation, backtracking, grid problems).\n"
            "- Strong preference for **clean, testable, readable code**.\n"
            "- **LLD** expected even for intern roles; design a payment engine or booking module.\n"
            "- Behavioral interviews check for product thinking and team alignment.\n"
            "\n**🚀 Pro Tips:**\n"
            "* Prepare to walk through your code in-depth.\n"
            "* Be ready to discuss feature design from a product perspective.\n"
            "* Learn Intuit’s principles (Design for Delight, customer obsession)."
        )
    ]
}
# ===========================
# 📋 QUESTIONS PAGE
# ===========================
if st.session_state.page == "questions":
    st.subheader("📋 Filter Interview Questions")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        company = st.multiselect("Select Company", options=sorted(df["Company"].dropna().unique()))
    with col2:
        round_type = st.multiselect("Select Round Type", options=sorted(df["Round Type"].dropna().unique()))
    with col3:
        topic = st.multiselect("Select Topic", options=sorted(df["Normalized Topic"].dropna().unique()))
    with col4:
        difficulty = st.multiselect("Select Difficulty", options=sorted(df["Difficulty"].dropna().unique()))
    with col5:
        recency = st.multiselect("Select Recency", options=sorted(df["Recency"].dropna().unique()))
    with col6:
        frequency = st.multiselect("Select Frequency", options=sorted(df["Frequency"].dropna().unique()))

    filtered_df = df.copy()
    if company:
        filtered_df = filtered_df[filtered_df["Company"].isin(company)]
    if round_type:
        filtered_df = filtered_df[filtered_df["Round Type"].isin(round_type)]
    if topic:
        filtered_df = filtered_df[filtered_df["Normalized Topic"].isin(topic)]
    if difficulty:
        filtered_df = filtered_df[filtered_df["Difficulty"].isin(difficulty)]
    if recency:
        filtered_df = filtered_df[filtered_df["Recency"].isin(recency)]
    if frequency:
        filtered_df = filtered_df[filtered_df["Frequency"].isin(frequency)]

    st.markdown("### 🧾 Filtered Questions")
    st.markdown(f'<div class="responsive-table">{filtered_df.to_html(escape=False, index=False)}</div>', unsafe_allow_html=True)
    st.markdown("### 📈 Summary")
    st.write(f"Total Questions: {len(filtered_df)}")

# ===========================
# 📊 INSIGHTS PAGE (Modified to include company insights)
# ===========================
elif st.session_state.page == "insights":
    st.subheader("📊 Company-wise Insights")
    selected_company = st.selectbox("Choose Company", insights_data["Company"])

    # Show insights for selected company
    if selected_company in insights_data["Company"]:
        index = insights_data["Company"].index(selected_company)
        insights = insights_data["Insights"][index]
        st.markdown(f"## 💡 Insights for {selected_company}") # This line seems correct for the main title
        # THIS IS THE CRUCIAL LINE TO CHECK:
        st.markdown(insights) # <--- ENSURE THIS IS st.markdown() AND NOT st.text()
        # If it's st.text(insights), change it to st.markdown(insights)
        # You might also want to add unsafe_allow_html=True here if you plan
        # to embed more complex HTML later, but for basic markdown, it's not strictly necessary.

    company_df = df[df["Company"] == selected_company]
    st.write(f"Total Questions: {len(company_df)}")

    # Difficulty Distribution
    st.markdown("#### 🎯 Difficulty Distribution")
    fig1, ax1 = plt.subplots()
    ax1.pie(company_df["Difficulty"].value_counts(), labels=company_df["Difficulty"].value_counts().index, autopct='%1.1f%%')
    ax1.axis("equal")
    st.pyplot(fig1)

    # Topics Asked
    st.markdown("#### 🧠 Topics Asked")
    fig2, ax2 = plt.subplots()
    company_df["Normalized Topic"].value_counts().plot(kind="bar", ax=ax2, color='skyblue')
    ax2.set_ylabel("Questions")
    st.pyplot(fig2)

    # Round Types
    st.markdown("#### 🧪 Round Types")
    fig3, ax3 = plt.subplots()
    company_df["Round Type"].value_counts().plot(kind="bar", ax=ax3, color='orange')
    ax3.set_ylabel("Count")
    st.pyplot(fig3)

    # Additional Insights
    st.markdown("#### 📈 Additional Insights")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Most Frequent Topic", company_df["Normalized Topic"].mode()[0] if not company_df["Normalized Topic"].mode().empty else "N/A")
        st.metric("Most Common Round", company_df["Round Type"].mode()[0] if not company_df["Round Type"].mode().empty else "N/A")
    with col2:
        st.metric("Most Common Difficulty", company_df["Difficulty"].mode()[0] if not company_df["Difficulty"].mode().empty else "N/A")
        st.metric("Most Recent Tag", company_df["Recency"].mode()[0] if not company_df["Recency"].mode().empty else "N/A")

# ===========================
# 📮 CONTACT PAGE
# ===========================
elif st.session_state.page == "contact":
    st.subheader("📮 Contact Us")
    st.markdown("""
        If you have suggestions, feedback, or want to contribute:
        - 📧 Email: [harshporwal033@gmail.com](mailto:harshporwal033@gmai.com)
        - 🐙 GitHub: https://github.com/harshporwal033
        - 📣 LinkedIn: https://www.linkedin.com/in/harsh-porwal-576815255
        - 🌐 Website: https://portfolio/harshporwal033

        We'd love to hear from you! 💬
    """)