import openai

cliente = openai.OpenAI(api_key = "sua chave")
        
mensagem_definicao_de_chat = [{"role": "system", "content": "Você é um assistente prestativo."}]


# Entrada das mensagens no chat
resposta = cliente.chat.completions.create(
messages=mensagem_definicao_de_chat + [{"role": "user", "content": "conteúdo desejado para perguntar ao chat" }],
model="gpt-3.5-turbo")

resposta_do_chat = resposta.choices[0].message.content
mensagem_definicao_de_chat.append({"role": "assistant", "content": resposta_do_chat}) 

print("Resposta:", resposta_do_chat, end="")