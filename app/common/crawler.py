import asyncio
from pydantic import HttpUrl
from crawl4ai import *

async def crawl_link(link: HttpUrl):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=link)
        return (result.markdown)

# test = asyncio.run(crawl_link("https://docs.mongoengine.org/apireference.html"))

# print(test)