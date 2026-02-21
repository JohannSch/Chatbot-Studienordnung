import os
import chromadb

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from autogen.agentchat.contrib.retrieve_assistant_agent import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

from autogen.retrieve_utils import TEXT_FORMATS


# API configuration
base_url = "https://chat-ai.academiccloud.de/v1"
model = "gpt-oss-120b"


config_list = [{"model": model, "base_url": base_url, "api_key": os.environ['CHAT_AI_API_KEY']}]    # API-Key must be set for this to work


# config_list = autogen.LLMConfig.from_json(path="./OAI_CONFIG_LIST")

llm_config = {"config_list": config_list, "timeout": 600, "cache_seed": 12345678}


assistant = AssistantAgent(
    name = "assistant",
    system_message = "Du bist ein hilfreicher Assistent.",
    llm_config = llm_config,
    description = "Assistent der die Rolle eines normalen Chatbots übernimmt."
)
ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=3,
    retrieve_config={
        "task": "qa",
        "docs_path": [
            "./Pruefungsordnungen/I41b_2023_PO.pdf",
            "./Pruefungsordnungen/I41b_2023_SO.pdf",
            os.path.join(os.path.abspath(""), "..", "website", "docs"),
        ],
        "custom_text_types": ["pdf"],
        "chunk_token_size": 2000,
        "model": config_list[0]["model"],
        "client": chromadb.PersistentClient(path="/tmp/chromadb"),
        "embedding_model": "all-mpnet-base-v2",
        "get_or_create": True,  # set to False if you don't want to reuse an existing collection, but you'll need to remove the collection manually
    },
    code_execution_config=False  # generated code will not be executed
)


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ai-response")
def ai_response(question: str) -> str:
    """
        :param question: A question to the AI.
        :type question: str
        :return: The AI's response to the question.
        :rtype: str
    """
    ragproxyagent.initiate_chat(
        assistant, message=ragproxyagent.message_generator, problem=question#, search_string="Credit"
    )
    last_message = ragproxyagent.last_message(assistant)["content"]
    if(last_message == "UPDATE CONTEXT"):
        raise Exception("Not enough context provided.")
    else:
        print(last_message)
        return last_message