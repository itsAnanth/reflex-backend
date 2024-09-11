
import os
from groq import Groq

class LLM:
    
    def __init__(self):
        self.API_KEY = "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"
        self.MODEL = "mixtral-8x7b-32768"
        self.contexts = {}
        self.client = Groq(api_key=self.API_KEY)
        
    def initPrompt(self, userId):
        self.contexts[userId] = []
        self.addSystemMessage(userId, "You are a helpful assistant, your name is Reflex AI. you were built by DUK students for primarily object detection, indentify the objects in it and answer queries regarding the objects")
        
        
    def addUserMessage(self, userId, content):
        
        if (not self.contexts.get(userId)):
            self.initPrompt(userId)
        self.contexts[userId].append({
            "role": "user",
            "content": content
        })
        
    def addAssistantMessage(self, userId, content):
        self.contexts[userId].append({
            "role": "assistant",
            "content": content
        })
        
    def addSystemMessage(self, userId, content):
        self.contexts[userId].append({
            "role": "system",
            "content": content
        })
        
    def generate(self, userId, content):
        
        self.addUserMessage(userId, content)
        
        # print(self.contexts)
        chat = self.client.chat.completions.create(messages=self.contexts[userId], model=self.MODEL)
        chat = chat.choices[0].message.content
        self.addAssistantMessage(userId, chat)
        return chat
        
        # self.add
        # pass




# messages = [
#         {
#             "role": "system",
#             "content": "you are a helpful assistant."
#         }
# ]


# while True:
#     inp = str(input("> "))
    
#     if inp == 'exit': break
    
#     messages.append({
#         "role": "user",
#         "content": inp
#     })
    
#     chat = client.chat.completions.create(messages=messages, model=MODEL)
    
#     print(f"> {chat.choices[0].message.content}")
    
#     messages.append({
#         "role": "assistant",
#         "content": str(chat.choices[0].message.content)
#     })
    
    
    

# print(chat_completion.choices[0].message.content)