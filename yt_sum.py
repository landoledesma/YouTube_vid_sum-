from pytube import YouTube
from haystack.nodes import PromptModel, PromptNode
from haystack.nodes.audio import WhisperTranscriber
from haystack.pipelines import Pipeline
from dotenv import load_dotenv
import os

load_dotenv("token.env")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class YoutubeSum():

    def load_model():
        summary_prompt = "deepset/summarization"
        model_node = PromptNode(
            "gpt-3.5-turbo",
            api_key=OPENAI_API_KEY,
            max_length=256,
            stop_words=["Observation:"],
            model_kwargs={"temperature": 0.5},
            default_prompt=summary_prompt,
            use_gpu=False
        )
        return model_node

    def download_video(url):
        yt = YouTube(url)
        video = yt.streams.filter(abr='160kbps').last()
        return video.download()


    def transcribe_aud(file_path,prompt_node):
        whisper = WhisperTranscriber()
        pipeline = Pipeline()
        pipeline.add_node(component=whisper, name="whisper",inputs=["File"])
        pipeline.add_node(component=prompt_node, name="promt",inputs=["whisper"])
        output = pipeline.run(file_path=[file_path])
        return output
