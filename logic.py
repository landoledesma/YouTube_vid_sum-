from pytube import YouTube
from haystack.nodes import  PromptNode
from haystack.nodes.audio import WhisperTranscriber
from haystack.pipelines import Pipeline
import os
from dotenv import load_dotenv

load_dotenv('token.env')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


class YoutubeSumVid:

    def load_model(self):
        prompt_node = PromptNode("text-davinci-003", max_length=1000,default_prompt_template="deepset/summarization",
                         api_key=OPENAI_API_KEY,)
        return prompt_node

    def download_video(self,url:str):
        yt = YouTube(url)
        video = yt.streams.filter(abr='160kbps').last()
        return video.download()


    def transcribe_aud(self,file_path,prompt_node):
        whisper = WhisperTranscriber()
        pipeline = Pipeline()
        pipeline.add_node(component=whisper, name="whisper",inputs=["File"])
        pipeline.add_node(component=prompt_node, name="promt",inputs=["whisper"])
        
        output = pipeline.run(file_paths=[file_path])
       
        return (output["results"])
