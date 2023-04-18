import datetime
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends, Form, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from agents.control import AgentsController
from auth.control import AuthController, ACCESS_TOKEN_EXPIRE_MINUTES
from persons.control import PersonController
from persons.model import Person

app = FastAPI()


@app.get("/agents/{agent_id}")
def get_individual_agent(agent_id: int):
    agent = AgentsController(agent_id)
    response = agent.get_one_agent()
    return response


@app.get("/agents")
def get_all_agents(current_user: Person = Depends(AuthController.get_current_user)):
    agents = AgentsController()
    response = agents.get_all_agents()
    return response


@app.post("/register")
def register_user(name: Annotated[str, Form()], email: Annotated[str, Form()], password: Annotated[str, Form()],
                  elo: Annotated[str, Form()], favorite_agent_id: Annotated[str, Form()],
                  is_private: Annotated[bool, Form()]):
    user = PersonController(name=name, email=email, password=password, elo=elo, favorite_agent_id=favorite_agent_id,
                            is_private=is_private)
    response = user.create_new_person()
    return response


@app.post("/login")
def login(email: Annotated[str, Form()], password: Annotated[str, Form()]):
    auth = AuthController(email, password)
    user = auth.authenticate_user()
    if user:
        access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = AuthController.create_access_token(
            data={"sub": user.email},
            expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        return HTTPException(status_code=400, detail="Incorrect email or password")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
