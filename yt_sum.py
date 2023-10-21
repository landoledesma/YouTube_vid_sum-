from pytube import YouTube
from haystack.nodes import PromptModel, PromptNode
from haystack.nodes.audio import WhisperTranscriber
from haystack.pipelines import Pipeline
import time

def download_video(url):
    yt = YouTube(url)
    video = yt.streams.filter(abr='160kbps').last()
    return video.download()

def init_prompt_node(model):
    summary_prompt = "deepset/summarization"
    return PromptNode(
        model_name_or_path=model,
        default_prompt = summary_prompt,
        use_gpu=False
        )

def transcribe_aud(file_path,prompt_node):
    whisper = WhisperTranscriber()
    pipeline = Pipeline()
    pipeline.add_node(component=whisper, name="whisper",inputs=["File"])
    pipeline.add_node(component=prompt_node, name="promt",inputs=["whisper"])
    output = pipeline.run(file_path=[file_path])
    return output
