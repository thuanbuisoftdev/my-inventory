GPT4ALL_API_URL = "http://localhost:4891/v1"

from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage


def main():
    chat = ChatOpenAI(
        base_url=GPT4ALL_API_URL,
        api_key="not-needed",
    )

    message = HumanMessage(content="Say hello world!")

    response = chat.invoke([message])

    print("AI Response:", response.content)


if __name__ == "__main__":
    main()
