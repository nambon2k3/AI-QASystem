from setuptools import setup, find_packages

setup(
    name='GenAI-QASys',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "llama-index",
        "google-generativeai",
        "llama-index-llms-gemini",
        "pypdf",
        "python-dotenv",
        "IPython",
        "llama-index-embeddings-gemini",
        "streamlit",
        "pinecone",
        "llama-index-vector-stores-pinecone",
        "llama-index-readers-file",
        "arxiv",
        "pinecone[grpc]"
    ],
)
