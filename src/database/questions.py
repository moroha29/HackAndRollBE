from ..models.questions import QuestionModel
from .connection import db
from bson.objectid import ObjectId
from typing import Optional


questions = db.get_collection("questions")


async def add_question(question: QuestionModel) -> str:
    result = await questions.insert_one(question.model_dump(by_alias=True))
    question_id = str(result.inserted_id)
    return question_id


async def fetch_random(user_id: str) -> Optional[dict]:
    cursor = questions.aggregate(
        [
            {"$match": {"answers": {"$not": {"$elemMatch": {"user_id": user_id}}}}},
            {"$sample": {"size": 1}},
        ]
    )
    question = None
    async for q in cursor:
        question = q
        break
    await cursor.close()
    return question


async def fetch_all() -> list[dict]:
    cursor = questions.find()
    result = []
    async for q in cursor:
        q["_id"] = str(q["_id"])
        result.append(q)
    await cursor.close()
    return result


async def answer_question(question_id: str, answer: dict) -> bool:
    result = await questions.update_one({"_id": ObjectId(question_id)}, {"$push": {"answers": answer}})
    question_id = str(result.upserted_id)
    return result.modified_count > 0
