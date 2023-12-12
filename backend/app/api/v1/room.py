from typing import Any, List

from fastapi import APIRouter
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.deps.request_params import ItemRequestParams
from app.repo.room_repo import RoomRepo
from app.schemas.room import RoomRead, RoomUpdate

router = APIRouter(prefix="/rooms")

@router.get("/", response_model=List[RoomRead])
async def get_floor_rooms(
        response: Response,
        session: CurrentAsyncSession,
        request_params: ItemRequestParams,
        floor_id: int| None = None,
        room_id: int|None = None,
) -> Any:
    room_repo: RoomRepo = RoomRepo(session)
    room = room_repo.get_room(floor_id=floor_id,room_id=room_id)

    if not room:
        return []
    return rooms

@router.post("", response_model=RoomRead, status_code=201)
async def create_room(
        room_in: RoomRead,
        session: CurrentAsyncSession,
) -> Any:
    room_repo: RoomRepo = RoomRepo(session)
    room = RoomRead(**room_in.dict())
    result = await room_repo.create_room(room)
    return result

@router.put("/{room_id}", response_model=RoomRead)
async def update_room(
        room_id: int,
        room_in: RoomUpdate,
        session: CurrentAsyncSession,
) -> Any:
    room_repo: RoomRepo = RoomRepo(session)
    result = await room_repo.update_room(room_id, room_in)
    return result

@router.delete("/{room_id}")
async def delete_room(
        room_id: int,
        session: CurrentAsyncSession,
) -> Any:
    room_repo: RoomRepo = RoomRepo(session)
    result = await room_repo.delete_room(room_id)
    return result