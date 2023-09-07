import os
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv(f"{HuggingFaceHub}")
llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature": 0.5})

prompt = PromptTemplate(
	input_variables=['input'],
	template= """
	human: {input}
	ai assistant: 
	 """
	)

chain = LLMChain(prompt = prompt, llm = llm)
def response_from_model(text):
	res = chain.predict(input=text)
	print(res)
	return res
