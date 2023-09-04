import os
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv('HuggingFaceHub')
llm = HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct", model_kwargs={"temperature": 0.5})

conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory()
)

def response_from_model(text):
	return conversation.predict(input=text)
