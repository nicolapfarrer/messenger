from api_utils import API, run, NotFound, UnprocessableEntity

api = API()

messages = [
    {"username": "isa", "message": "tschou zäme"},
    {"username": "piotr", "message": "salü isa!"},
]

@api.GET("/api/chat/")
def list_messages():
    return messages

@api.POST("/api/chat/")
def post_message(username:str, message: str):
    messages.append({"username": username, "message": message})

@api.POST("/api/update/")
def post_leave(username:str, action:str):
    messages.append({"username":"Server","message":f'{username} {action} the Chat'})
run(api, port=5000)
