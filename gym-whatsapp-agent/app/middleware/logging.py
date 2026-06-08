from fastapi import Request

async def log_request(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")
    return await call_next(request)
