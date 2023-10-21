from pytube import YouTube
from haystack.nodes import PromptModel, PromptNode
from haystack.nodes.audio import WhisperTranscriber
from haystack.pipelines import Pipeline
import time
