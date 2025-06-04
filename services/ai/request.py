from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

from config import cnf


def request(text):
    giga = GigaChat(
        credentials=cnf.app.AI_API_KEY,
        verify_ssl_certs=False,
    )
    contacts = (open('services/ai/data/datasets/contacts.txt', 'r', encoding='utf-8')).read()
    faq = (open('services/ai/data/datasets/faq.txt', 'r', encoding='utf-8')).read()
    messages = [
        SystemMessage(
            content=f"Ты бот-ассистент для студентов, можешь отвечать на различные вопросы и знаешь все об институте и сотрудниках потому что знаешь {faq} и {contacts}"
        )
    ]
    
    messages.append(HumanMessage(content=text))
    res = giga.invoke(messages)
    messages.append(res)
    print(res.content)
    
print(request('кто такой гребенюк'))