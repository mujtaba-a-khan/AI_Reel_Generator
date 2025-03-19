# AI_Reel_Generator

# 1. Introduction
This project aims to explore the capabilities of AI in automated video generation by developing an AI-powered Reel Generator. The system takes a news article URL as input, scrapes the content, generates a structured video script, creates AI-generated images, generates realistic voice narration, adds subtitles, and compiles everything into a fully edited short-form video.

The goal is to demonstrate the power of AI in automated multimedia production, evaluating how well different deep learning models can be combined to create engaging short-form content.
 
# 2. Use Case & Relevance
Why is this use case interesting?

1) Growing Demand for Short-Form Video Content: Platforms like YouTube Shorts, TikTok, and Instagram Reels have dominated digital media consumption, creating a high demand for quick, engaging content.
2) Automating Video Creation: Traditional video production is time-consuming. This AI-powered solution automates the entire process, reducing human effort.
3) Accessibility & Scalability: Anyone can use the tool to generate videos without prior editing skills.
4) Potential Business Applications: The system can be extended for marketing, education, and news content generation, allowing journalists, influencers, and educators to quickly create engaging videos.

# 3. How the System Works
1.	Web Scraping: Uses Crawl4AI to extract content from a news article.
2.	Script Generation: GPT-4o-mini analyzes the article and creates a structured video script with scene-wise narration.
3.	AI Image Generation: DALL·E 3 generates scene-specific images based on the script.
4.	Text-to-Speech (TTS) Conversion: Deepgram converts text narration into realistic AI voice.
5.	Subtitles Processing: The system syncs subtitles with the generated audio using Pysrt.
6.	Final Video Compilation: Uses FFmpeg to merge images, audio, and subtitles into a final Reel video.

# 4. Reproducibility: How to Use the System
To reproduce this project, follow these steps:

# 4.1 Prerequisites

●	Python 3.8+ installed

●	FFmpeg installed

●	API keys for OpenAI, Deepgram


Required Python libraries:

```bash
pip install crawl4ai pydantic-ai requests ffmpeg-python pysrt
```

# 4.2 Steps to Run
Clone the repository from GitHub:

1.	Set up API keys in .env file:

```bash
OPENAI_API_KEY=your_openai_key
```

```bash
DEEPGRAM_API_KEY=your_deepgram_key
```

2.	Run the script with any news article URL:

```bash
python ai_reel_generator.py
```

3.	The script will generate a video

# 5. References
1.	GPT-4o-mini Model - OpenAI: https://platform.openai.com/
2.	DALL·E 3 for Image Generation - OpenAI: https://openai.com/dall-e
3.	Deepgram Text-to-Speech API - https://deepgram.com
4.	Pysrt Library for Subtitles - https://pypi.org/project/pysrt/
5.	FFmpeg for Video Processing - https://ffmpeg.org/


