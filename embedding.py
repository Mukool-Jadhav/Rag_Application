# from sentence_transformers import SentenceTransformer

# # Load the model
# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# # Encode text(s)
# sentences = ["This is a sentence.", "This is another sentence."]
# embeddings = model.encode(sentences)

# print(embeddings.shape)  # (2, 384) -> 384-dimensional embeddings
# print(embeddings[0][:10])  # first 10 numbers of first embedding

import getpass
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")