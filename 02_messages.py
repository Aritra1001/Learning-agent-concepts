import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.chat_models import init_chat_model
import truststore

truststore.inject_into_ssl()

load_dotenv()

model=init_chat_model(
    model="openai/gpt-oss-20b",
    model_provider="groq"
)

# messages = [
#     # instructions for the model
#     SystemMessage(
#         content="You are a pirate. Answer in one sentence."
#     ),
#     # user's message
#     HumanMessage(
#         content="What is Python?"
#     )
# ]

# messages_1=[
#     SystemMessage(
#         content="You are a helpful Python tutor. Answer in one line"
#     ),
#     HumanMessage(
#         content="What is a list?"
#     ),
#     # Previous model response
#     # This AI message was not previously generated. I am explicitly telling the model this is something you have said earlier
#     AIMessage(
#         content="A list is an ordered collection of items in Python."
#     ),
#     HumanMessage(
#         content="Can you give me an example?"
#     )
# ]

# messages_2=[
#      SystemMessage(
#         content="You are a helpful assistant."
#     ),
#     HumanMessage(
#         content="My name is Aritra."
#     ),
#     AIMessage(
#         content="Nice to meet you, Aritra!"
#     ),
#     HumanMessage(
#         content="What is my name?"
#     )
# ]

# Prove that the model is stateless. It won't memorize the earlier message contexts until explicitly passed to it
# messages = [
#     HumanMessage(content="My favorite programming language is Python.")
# ]

# messages_1=[
#     # On asking this directly, the model wont have the answer for this
#     HumanMessage(content="What is my favorite programming language?")
# ]

# Now the model has the context as a Human Message, now it can answer the fav programming language
# messagesWithHistory = [
#     HumanMessage(
#         content="My favorite programming language is Python."
#     ),

#     AIMessage(
#         content="That's a popular choice!"
#     ),

#     HumanMessage(
#         content="What is my favorite programming language?"
#     )
# ]


# Building the chat loop
messages = [
    SystemMessage(
        content="You are a helpful Python tutor."
    )
]

while True:
    user_input = input("You:")
    if user_input.lower() in ["exit", "quit"]:
        break

    # add user's message to history
    messages.append(
        HumanMessage(
            content=user_input
        )
    )

    # send entire conversation history
    response=model.invoke(messages)

    # add AI response to history
    messages.append(
        AIMessage(
            content=response.content
        )
    )

    print("AI:", response.content)



# not used for chat loop
# response = model.invoke(messagesWithHistory)

# print(response.content)