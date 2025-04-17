from langchain_community.llms import Ollama

class LLMService:
    def __init__(self):
        self.llm = Ollama(model="llama3.2")

    def generate_answer(self, question: str, context: str) -> str:
        prompt = f"""Based on the following context, please answer the question.
        
        Context: {context}
        
        Question: {question}
        
        Answer:"""
        
        return self.llm.invoke(prompt) 