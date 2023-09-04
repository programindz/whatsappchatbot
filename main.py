from fastapi import FastAPI, Form, Request
from utils import send_message
from model import response_from_model

app = FastAPI()

@app.post("/message")
async def reply(Body: str = Form(), From: str=Form()):
	response = response_from_model(Body)
	number = From.replace("whatsapp:","")
	print(response)
	send_message(number, response)
	return ""