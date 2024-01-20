from fastapi import APIRouter
from .questions import router as questions_router
from .users import router as users_router
from .gpt_generated import router as gpt_generated_router


router = APIRouter()
router.include_router(questions_router, prefix="/questions", tags=["questions"])
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(gpt_generated_router, prefix="/gpt", tags=["gpt"])
