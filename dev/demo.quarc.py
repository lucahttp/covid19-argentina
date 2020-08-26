import asyncio
import random
import aioredis
import redis
from quart import Quart, request, url_for, jsonify

app = Quart(__name__)


