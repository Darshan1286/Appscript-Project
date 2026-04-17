import time

class RateLimiter:
    def __init__(self, limit_per_minute: int = 5):
        self.limit = limit_per_minute
        self.calls = {}

    def is_allowed(self, user: str) -> bool:
        now = time.time()
        window = 60  # 1 minute

        user_calls = self.calls.get(user, [])
        user_calls = [t for t in user_calls if now - t < window]

        if len(user_calls) >= self.limit:
            return False

        user_calls.append(now)
        self.calls[user] = user_calls
        return True

rate_limiter = RateLimiter(limit_per_minute=5)
