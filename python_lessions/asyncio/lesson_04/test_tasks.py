import asyncio
from tasks import AsyncProducer, AsyncConsumer, AsyncPipeline


async def test_async_producer_consumer():
    queue = asyncio.Queue()
    items = [1, 2, 3, 4, 5]
    
    producer = AsyncProducer(queue, items)
    consumer = AsyncConsumer(queue)
    
    await producer.produce()
    await consumer.consume()
    
    assert consumer.processed_items == items


async def test_async_pipeline():
    pipeline = AsyncPipeline()
    items = ["hello", "world", "async"]
    
    producer = AsyncProducer(pipeline.queue, items)
    consumer = AsyncConsumer(pipeline.queue)
    
    pipeline.add_producer(producer)
    pipeline.add_consumer(consumer)
    
    await pipeline.run()
    
    assert consumer.processed_items == items


