import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


import truststore

truststore.inject_into_ssl()

load_dotenv()

model=init_chat_model(
    model="openai/gpt-oss-20b",
    model_provider="groq"
)

# 2 different ways of sending/receiving model requests:
# stream() - one request but receive the answer progressively (piece by piece)
# The model generates the response chunk by chunk. As each chunk is received, the application displays it chunk by chunk

# batch() → multiple independent requests sent together.
# ainvoke() / astream() → asynchronous versions.


# As we have seen in invoke, the application wait for the model to finish and then displays the entire result at once
# response = model.invoke(
#     "Explain what LangChain is in detail."
# )

# print(response.content)

# In real world, chat gpt like applications use streaming
# for chunk in model.stream(
#     "Explain what LangChain is in detail."
# ):
#     # end="" - Dont add a newline
#     # flush=True - Display it immediately
#     print(chunk.content, end="", flush=True)

# print()


# prompts=[
#     "What is Python?",
#     "What is LangChain?",
#     "What is LangGraph?"
# ]

# Using batch we can send multiple prompts at the same time
# And the response will come serially based on the prompts

# responses = model.batch(prompts)

# for response in responses:
#     print(response.content)
#     print('-' * 50)


# ainvoke() - 