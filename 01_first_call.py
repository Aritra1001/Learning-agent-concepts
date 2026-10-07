# Step 1: Your first model call
# File: 01_first_call.py

# Load .env with load_dotenv().
# Create a model with init_chat_model("groq:<model-name>").
# Call model.invoke("...") with a simple question.
# Print the whole response object, not just .content, and look at:
# .content: the text
# .response_metadata: model name and finish reason
# .usage_metadata: input and output token counts
# In LangSmith: open the trace and match each field to what you printed.
# 🎯 Exercise: change temperature (0 vs 1) and max_tokens, run the same prompt 3 times each, and compare how much the answers vary.



import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from groq import Groq
import truststore

truststore.inject_into_ssl()

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")

# for m in Groq().models.list().data:
#     print(m.id)

model = init_chat_model(model="openai/gpt-oss-20b", model_provider="groq", temperature=1)

response = model.invoke("Explain what an AI agent is?")

print("CONTENT:\n", response.content)
print("\nUSAGE:", response.usage_metadata)
print("\nRESPONSE METADATA:", response.response_metadata)
print("\nADDITIONAL KWARGS:", response.additional_kwargs)
print("\nRUN ID:", response.id)
