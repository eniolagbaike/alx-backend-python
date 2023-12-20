#!/usr/bin/env python3
"""Task 0 module"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay number """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay