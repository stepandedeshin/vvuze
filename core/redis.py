from fastapi import FastAPI, Request
from redis.asyncio import Redis, from_url
import json
from functools import wraps

from config import cnf


async def get_redis() -> Redis:
    redis = await from_url(f"redis://{cnf.redis.HOST}:{cnf.redis.PORT}/{cnf.redis.DB}", encoding="utf-8", decode_responses=True)
    return redis


def cache(key_pattern: str, ttl: int = 60):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = kwargs.get('request')
            redis = await get_redis()
            
            cache_key = key_pattern.format(**kwargs)
            cached = await redis.get(cache_key)
            if cached:
                return json.loads(cached)

            result = await func(*args, **kwargs)
            
            await redis.setex(cache_key, ttl, json.dumps(result))
            
            return result
        return wrapper
    return decorator