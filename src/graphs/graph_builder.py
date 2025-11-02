from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import GroqLLM
# from src.states.blogstate import BlogState
# from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self,llm):
        self.llm=llm