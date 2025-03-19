import os
import asyncio
from typing import List
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler
from pydantic_ai import Agent
from dotenv import load_dotenv

from utils.subtitles_generator import generate_audio_and_subtitle
from utils.image_downloader import download_image
from utils.image_generator import generate_image
from utils.video_generator import preprocess_images, create_video_with_audio_and_subtitles

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

if not OPENAI_API_KEY or not DEEPGRAM_API_KEY:
    raise ValueError("Missing API keys in environment variables.")

# Data Models
class Scene(BaseModel):
    scene_number: int
    text: str
    image_prompt: str
    timeframe: int

class YouTubeShortsScript(BaseModel):
    scenes: List[Scene]

# Web Scraper
class WebScraper:
    def __init__(self, url: str):
        self.url = url
        self.client = AsyncWebCrawler()

    async def scrape(self) -> str:
        async with self.client as crawler:
            result = await crawler.arun(url=self.url)
            return result.markdown

# Scene Generator
class SceneGenerator:
    SYSTEM_PROMPT = """You are an advanced language model tasked with analyzing news articles and generating a YouTube Shorts video script..."""

    def __init__(self):
        self.agent = Agent(
            model='openai:gpt-4o-mini',
            system_prompt=self.SYSTEM_PROMPT,
            result_type=YouTubeShortsScript,
        )

    async def generate_scenes(self, article_text: str) -> List[Scene]:
        result = await self.agent.run(article_text)
        return result.data.scenes

# Image Generator
class ImageGenerator:
    def __init__(self):
        self.generated_images = []
    
    def generate_images(self, scenes: List[Scene]):
        for idx, scene in enumerate(scenes):
            print("Generating image for Scene", idx)
            url = generate_image(scene.image_prompt)
            self.generated_images.append((scene.scene_number, url))

    def download_images(self):
        for scene_number, url in self.generated_images:
            print("Downloading image for Scene", scene_number)
            download_image(url, f"image{scene_number}")

# Audio & Subtitle Generator
class AudioGenerator:
    def generate_audio_and_subtitles(self, scenes: List[Scene]):
        generate_audio_and_subtitle([scene.dict() for scene in scenes])

# Video Generator
class VideoGenerator:
    def create_video(self):
        preprocess_images("images", "images_processed")
        create_video_with_audio_and_subtitles("images_processed", "audios", "output_video.mp4")

# AI Reel Generator
class AIReelGenerator:
    def __init__(self, url: str):
        self.url = url
        self.scraper = WebScraper(url)
        self.scene_generator = SceneGenerator()
        self.image_generator = ImageGenerator()
        self.audio_generator = AudioGenerator()
        self.video_generator = VideoGenerator()

    async def run(self):
        print("Scraping article...")
        article_text = await self.scraper.scrape()
        print("Generating scenes...")
        scenes = await self.scene_generator.generate_scenes(article_text)
        print("Generating images...")
        self.image_generator.generate_images(scenes)
        self.image_generator.download_images()
        print("Generating audio & subtitles...")
        self.audio_generator.generate_audio_and_subtitles(scenes)
        print("Creating video...")
        self.video_generator.create_video()
        print("AI Reel generation complete!")

# Run
if __name__ == "__main__":
    url = 'https://www.bbc.com/news/articles/c0mw221z2yyo'
    # url = 'https://www.bbc.com/future/article/20250122-expert-tips-on-how-to-keep-exercising-during-cold-winter-weather'
    generator = AIReelGenerator(url)
    asyncio.run(generator.run())