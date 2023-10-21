import streamlit as st
import time
from yt_sum import YoutubeSum

st.set_page_config(
    layout="wide"
)

def main():
    youtube = YoutubeSum()

    # Set the title and background color
    st.title("YouTube Video Summarizer 🎥")
    st.markdown('<style>h1{color: orange; text-align: center;}</style>', unsafe_allow_html=True)
    st.subheader('Built with the Llama 2 🦙, Haystack, Streamlit and ❤️')
    st.markdown('<style>h3{color: pink;  text-align: center;}</style>', unsafe_allow_html=True)

    # Expander for app details
    with st.expander("About the App"):
        st.write("This app allows you to summarize while watching a YouTube video.")
        st.write("Enter a YouTube URL in the input box below and click 'Submit' to start. This app is built by AI Anytime.")

    # Input box for YouTube URL
    youtube_url = st.text_input("Enter YouTube URL")

    # Submit button
    if st.button("Submit") and youtube_url:
        start_time = time.time()  # Start the timer
        # Download video
        file_path = youtube.download_video(youtube_url)

        # Initialize model
        full_path = "llama-2-7b-32k-instruct.Q4_K_S.gguf"
        model = youtube.load_model_model(full_path)
        prompt_node = prompt_node = youtube.init_prompt_nodeinit_prompt_node(model)
        # Transcribe audio
        output = youtube.transcribe_aud(file_path, prompt_node)

        end_time = time.time()  # End the timer
        elapsed_time = end_time - start_time

        # Display layout with 2 columns
        col1, col2 = st.columns([1,1])

        # Column 1: Video view
        with col1:
            st.video(youtube_url)

        # Column 2: Summary View
        with col2:
            st.header("Summarization of YouTube Video")
            st.write(output)
            st.success(output["results"][0].split("\n\n[INST]")[0])
            st.write(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()