from fastapi import APIRouter

router = APIRouter(tags=["healthcheck"])


@router.get("/healthcheck")
def read_root() -> dict[str, str]:
    return {"status": "OK"}
