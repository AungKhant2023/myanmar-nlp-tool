import streamlit as st
import os

# Load stopwords once
def load_stopwords(path="sw.txt"):
    with open(path, "r", encoding="utf-8") as f:
        stopwords = set(line.strip() for line in f if line.strip())
    return stopwords

# Remove stopwords but preserve lines
def remove_stopwords(text, stopwords):
    lines = text.splitlines()  # split by line
    filtered_lines = []
    for line in lines:
        words = line.split()  # split line by whitespace
        filtered = [w for w in words if w not in stopwords]
        filtered_lines.append(" ".join(filtered))
    return "\n".join(filtered_lines)  # join lines with newline

# Streamlit UI
st.sidebar.image("images/peacock-3.png", width=200)
st.sidebar.markdown("<h3 style='text-align: center;'>NLP Tool</h3>", unsafe_allow_html=True)

# Options
select = ['remove-stopwords']
option = st.sidebar.selectbox('Choose an option', select)

if option == "remove-stopwords":

    uploaded_file = st.file_uploader("📂 Choose a .txt file", type=["txt"])

    if uploaded_file is not None:
        try:
            # Read input text
            input_text = uploaded_file.read().decode("utf-8")

            # Load stopwords
            stopwords = load_stopwords("sw.txt")

            # Remove stopwords
            result = remove_stopwords(input_text, stopwords)

            # Save output
            os.makedirs("output", exist_ok=True)
            output_path = os.path.join("output", "stopwords_removed_output.txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result)

            # Download button
            st.download_button(
                label="📄 Download Processed File",
                data=result,
                file_name="stopwords_removed_output.txt",
                mime="text/plain"
            )

            # Show preview
            st.subheader("📝 Output Preview:")
            st.text(result)

        except Exception as e:
            st.error(f"❌ Error processing file: {e}")