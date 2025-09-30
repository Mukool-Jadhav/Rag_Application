from langchain.agents import create_agent
from langchain.tools import tool
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.messages import MessageLikeRepresentation
from langchain_text_splitters import RecursiveCharacterTextSplitter
from VectoreStore import vector_store
from chatModel import llm

# Load and chunk contents of the PDF file
PDF_FilePath = r"C:\Users\Admin\Downloads\NIPS-2017-attention-is-all-you-need-Paper.pdf"
loader = PyPDFLoader(PDF_FilePath)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

# Index chunks
_ = vector_store.add_documents(documents=all_splits)

# Construct a tool for retrieving context
@tool(response_format="content")
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

tools = [retrieve_context]
# If desired, specify custom instructions
prompt = (
    "You have access to a tool that retrieves context from a PDF File. "
    "Use the tool to help answer user queries."
)
agent = create_agent(llm, tools, prompt=prompt)
#query message
query = "how many layers are in the transformer, give indetailed answer ?"
for step in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()