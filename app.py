import streamlit as st
import time
from logic import YoutubeSumVid

st.set_page_config(
    layout="wide"
)
youtube = YoutubeSumVid()
def main():
    

    # Set the title and background color
    st.title("YouTube video Resumen 🎥")
    st.markdown('<style>h1{color: orange; text-align: center;}</style>', unsafe_allow_html=True)

    # Expander for app details
    with st.expander("Acerca de la app"):
        st.write("Crea resumen de videos de youtube con LLMs.")
        st.write("Ingresa la url de un video abajo y da click en 'Cargar' para empezar.")

    # Input box for YouTube URL
    youtube_url = st.text_input("Enter YouTube URL")

    # Submit button
    if st.button("Cargar") and youtube_url:
        start_time = time.time()  # Start the timer
        # Download video
        file_path = youtube.download_video(youtube_url)
        # Initialize model
        model_node = youtube.load_model()

        # Transcribe audio
        output = youtube.transcribe_aud(file_path, model_node)

        end_time = time.time()  # End the timer
        elapsed_time = end_time - start_time

        # Display layout with 2 columns
        col1, col2 = st.columns([1,1])

        # Column 1: Video view
        with col1:
            st.video(youtube_url)

        # Column 2: Summary View
        with col2:
            st.header("Resumen del Video")
            st.write(output)
            st.success(output["results"][0].split("\n\n[INST]")[0])
            st.write(f"Tiempo estimado : {elapsed_time:.2f} segundos")

if __name__ == "__main__":
    main()