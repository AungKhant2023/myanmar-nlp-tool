import streamlit as st
import os
import utilities_testing
from docx import Document
from io import BytesIO

# Load stopwords
with open("sw.txt", encoding="utf-8") as f:
    stopwords = set(line.strip() for line in f if line.strip())

def remove_stopwords(text, stopwords):
    words = text.split()
    filtered = [w for w in words if w not in stopwords]
    return " ".join(filtered)

# Streamlit UI
st.sidebar.image("images/peacock-3.png", width=200)
st.sidebar.markdown("<h3 style='text-align: center;'>NLP Tool</h3>", unsafe_allow_html=True)

select = ['syllable-tokenization']
option = st.sidebar.selectbox('Choose an option', select)

if option == "syllable-tokenization":

    uploaded_file = st.file_uploader("📂 Choose a .docx file", type=["docx"])

    if uploaded_file is not None:
        try:
            # Read DOCX content
            doc = Document(BytesIO(uploaded_file.read()))
            input_text = "\n".join([para.text for para in doc.paragraphs])

            # Tokenize
            tokenized = utilities_testing.syllable_tokenization(input_text)

            # Remove stopwords
            cleaned = remove_stopwords(tokenized, stopwords)

            st.subheader("✏️ Edit Output (You can modify here)")
            edited_text = st.text_area(
                "Edit your tokenized result:",
                value=cleaned,
                height=300
            )

            # Create output directory
            os.makedirs("output", exist_ok=True)

            # Save edited output
            output_path = os.path.join("output", "syllable_tokenized_output.txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(edited_text)

            # Download button
            st.download_button(
                label="📄 Download Final Tokenized File",
                data=edited_text,
                file_name="syllable_tokenized_output.txt",
                mime="text/plain"
            )

            # Preview
            st.subheader("📝 Final Output Preview:")
            st.text(edited_text)

        except Exception as e:
            st.error(f"❌ Error processing file: {e}")



# import streamlit as st
# import os
# import utilities_testing

# # Streamlit UI
# st.sidebar.image("images/peacock-3.png", width=200)
# st.sidebar.markdown("<h3 style='text-align: center;'>NLP Tool</h3>", unsafe_allow_html=True)

# # List of options
# select = ['syllable-tokenization']
# option = st.sidebar.selectbox('Choose an option', select)

# if option == "syllable-tokenization":

#     # File uploader
#     uploaded_file = st.file_uploader("📂 Choose a .txt file", type=["txt"])

#     if uploaded_file is not None:
#         try:
#             # Read and decode input text
#             input_text = uploaded_file.read().decode("utf-8")
            
#             # Tokenize using dictionary-based tokenization
#             result = utilities_testing.syllable_tokenization(input_text)

#             # Create output directory if it doesn't exist
#             os.makedirs("output", exist_ok=True)

#             # Save tokenized output to file
#             output_path = os.path.join("output", "syllable_tokenized_output.txt")
#             with open(output_path, "w", encoding="utf-8") as f:
#                 f.write(result)

#             # Download button
#             st.download_button(
#                 label="📄 Download Tokenized File",
#                 data=result,
#                 file_name="syllable_tokenized_output.txt",
#                 mime="text/plain"
#             )

#             # Show tokenized output preview
#             st.subheader("📝 Tokenized Output Preview:")
#             st.text(result)

#         except Exception as e:
#             st.error(f"❌ Error processing file: {e}")


# import streamlit as st
# import os
# import utilities_testing

# # Streamlit UI
# st.sidebar.image("images/peacock-3.png", width=200)
# st.sidebar.markdown("<h3 style='text-align: center;'>NLP Tool</h3>", unsafe_allow_html=True)

# # Load dictionary file once
# with open("dict-words.txt", encoding="utf-8") as f:
#     dictionary = set(line.strip() for line in f if line.strip())

# # Options
# select = ['syllable-tokenization']
# option = st.sidebar.selectbox('Choose an option', select)

# if option == "syllable-tokenization":

#     # File uploader
#     uploaded_file = st.file_uploader("📂 Choose a .txt file", type=["txt"])

#     if uploaded_file is not None:
#         try:
#             # Read and decode input text
#             input_text = uploaded_file.read().decode("utf-8")

#             # Tokenize using dictionary-based tokenization
#             result = utilities_testing.syllable_tokenization(input_text, dictionary)

#             # Save and download
#             os.makedirs("output", exist_ok=True)
#             output_path = os.path.join("output", "syllable_tokenized_output.txt")
#             with open(output_path, "w", encoding="utf-8") as f:
#                 f.write(result)

#             st.download_button("📄 Download Tokenized File", data=result,
#                                file_name="syllable_tokenized_output.txt", mime="text/plain")

#             st.subheader("📝 Tokenized Output Preview:")
#             st.text(result)

#         except Exception as e:
#             st.error(f"❌ Error processing file: {e}")
