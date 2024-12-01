import streamlit as st
from agents import AgentManager
from utils import logger


def main():
    st.set_page_config(page_title="Multi-Agent AI System", layout="wide")
    st.title("Multi-Agent AI System With Collaboration and Validation")


    st.sidebar.title(body="Select Task")

    tasks = [
        "Summarize Medical Text",
        "Write and Refine Reseach Article",
        "Sanitize Medical Data (PHI)"
    ]

    task = st.sidebar.selectbox(label="Choose a task", options=tasks)

    agent_manager = AgentManager(max_retries=2, verbose=True)


    if task == "Summarize Medical Text":
        summarize_section(agent_manager)
    elif task == "Write and Refine Reseach Article":
        write_and_refine_article_section(agent_manager)
    elif task == "Sanitize Medical Data (PHI)":
        pass


def summarize_section(agent_manager):
    st.header("Summarize Medical Text")
    text = st.text_area("Enter Medical Text to Summarize", height=200)
    if st.button("Summarize"):
        if text:
            main_agent = agent_manager.get_agent("summarize")
            validator_agent = agent_manager.get_agent("summarize_validator")
            with st.spinner("Summarizing..."):
                try:
                    summary = main_agent.execute(text)
                    st.subheader("Summary:")
                    st.write(summary)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"SummarizeAgent Error: {e}")
                    return
            with st.spinner("Validating summary..."):
                try:
                    validation_summary = validator_agent.execute(original_text=text, summary=summary)
                    st.subheader("Validation:")
                    st.write(validation_summary)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"ValidateAgent Error: {e}")
                    return
        else:
            st.write("Please enter some text to summarize.")
def write_and_refine_article_section(agent_manager):
    st.header("Write and Refine Research Article")
    topic = st.text_input(label="Enter the topic for research article")
    outline = st.text_area(label="Enter a outline (optional):", height=150)
    if st.button(label="Submit"):
        if topic:
            writer_agent = agent_manager.get_agent("write_article")
            refiner_agent = agent_manager.get_agent("refiner")
            validator_agent = agent_manager.get_agent("write_article_validator")
            with st.spinner("Writing a article.."):
                try:
                    draft = writer_agent.execute(topic, outline)
                    st.subheader("Draft Article:")
                    st.write(draft)
                except Exception as e:
                    st.error("Error: {e}")
                    logger.error("Writing Article Agent Error")
                    return
            with st.spinner(text="Refining a article.."):
                try:
                    refined_article = refiner_agent.execute(draft)
                    st.subheader("Refined Article:")
                    st.write(refined_article)
                except Exception as e:
                    st.error("Error: {e}")
                    logger.error("Refiner Artcle Agent Error.")
                    return
            with st.spinner(text="Validating Article.."):
                try:
                    validated_agent = validator_agent.execute(topic, refined_article)
                    st.subheader("Validated Article:")
                    st.write(validated_agent)
                except Exception as e:
                    st.error("Error: {e}")
                    logger.error("Validator Artcle Agent")
                    return
        else:
            st.write("Please provide a topic.")






if __name__ == "__main__":
    main()