import asyncio
from unittest.mock import AsyncMock, patch
from tasks import AsyncHttpClient, AsyncWebScraper, AsyncRateLimitedClient


async def test_async_http_client():
    with patch('aiohttp.ClientSession') as mock_session:
        mock_response = AsyncMock()
        mock_response.json.return_value = {"status": "ok"}
        mock_response.status = 200
        mock_session.return_value.__aenter__.return_value.get.return_value = mock_response
        
        async with AsyncHttpClient() as client:
            result = await client.get("https://api.example.com/test")
            assert result["status"] == "ok"


async def test_async_web_scraper():
    urls = ["https://example.com", "https://test.com"]
    
    with patch('aiohttp.ClientSession') as mock_session:
        mock_response = AsyncMock()
        mock_response.text.return_value = "<html>Test content</html>"
        mock_response.status = 200
        mock_session.return_value.__aenter__.return_value.get.return_value = mock_response
        
        scraper = AsyncWebScraper(max_concurrent=2)
        results = await scraper.scrape_urls(urls)
        
        assert len(results) == 2
        assert all("content" in result for result in results)


async def test_async_rate_limited_client():
    with patch('aiohttp.ClientSession') as mock_session:
        mock_response = AsyncMock()
        mock_response.json.return_value = {"data": "test"}
        mock_response.status = 200
        mock_session.return_value.__aenter__.return_value.get.return_value = mock_response
        
        async with AsyncRateLimitedClient(rate_limit=2, per_second=1.0) as client:
            result = await client.request("GET", "https://api.example.com")
            assert result["data"] == "test"


