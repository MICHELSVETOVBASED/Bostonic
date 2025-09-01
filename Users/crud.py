from Users.schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:  ##
    user = user_in.model_dump()
    return {"succcess": True, "user": user}
