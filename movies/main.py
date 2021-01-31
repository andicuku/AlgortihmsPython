import secrets
from time import perf_counter

from fastapi import FastAPI, Request

from .api.categories import router as category_router
from .api.users import router as user_router
from .api.movies import router as movies_router
from .logs import get_logger

app = FastAPI()

log = get_logger(__name__)


@app.middleware("http")
async def log_request_info(request: Request, next):
    req_id = secrets.token_hex(5)

    log.info("REQ-ID=%s :: Path = %r", req_id, request.url.path)

    start_time = perf_counter()
    response = await next(request)
    end_time = perf_counter()

    elapsed_time = "{0:.4f}".format((end_time - start_time))
    log.info("REQ-ID=%s :: Elapsed Time = %s", req_id, elapsed_time)

    return response


@app.get("/")
def index():
    return {"message": "Movies API"}


app.include_router(category_router, prefix="/categories")
app.include_router(user_router, prefix="/users")
app.include_router(movies_router, prefix="/movies")
