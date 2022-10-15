from analysis import analysis

from fastapi import FastAPI

app = FastAPI()


class User:
    username: str
    password: str
    email: str


@app.post("/register/")
async def register(user: User):
    # TODO create doc in MongoDB
    # TODO send confirmation email
    return {"message": "Confirmation email sent!"}


@app.post("/refresh")
async def refresh():
    users = []  # TODO from MongoDB

    for user in users:
        user.song = analysis  # TODO update doc in MongoDB

    # TODO send email/text notification

    return {"message": "Songs of the Day generated!"}
