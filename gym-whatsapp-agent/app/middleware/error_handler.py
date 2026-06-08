from fastapi import Request
from fastapi.responses import JSONResponse

async def catch_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        return JSONResponse({"error": str(exc)}, status_code=500)
