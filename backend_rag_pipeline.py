from langchain_groq import ChatGroq
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()
llm=ChatGroq(
    model="llama-3.1-8b-instant"
)
def generate_answer(query,retrieved_docs):
    context="\n".join(
        [doc.page_content for doc in retrieved_docs]
    )
    prompt=[
        SystemMessage(
            content=("You are a helpful AI research assistant.\n"
                "Answer ONLY using the provided context.\n"
                "If answer is not present in context,\n"
                "say you do not know."

            )
        ),
        HumanMessage(
            content=(
                f"context : {context}\n Question: {query}"
            )
        )
    ]
    for i, doc in enumerate(retrieved_docs):

        print(f"\nCHUNK {i}\n")

        print(doc.page_content)

        print("\n====================\n")
    response=llm.invoke(prompt)
    return response.content