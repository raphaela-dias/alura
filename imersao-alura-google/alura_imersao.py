import google.generativeai as genai
genai.configure(api_key = google_api_key)

#Lista os modelos generativos disponíveis
# for i in genai.list_models():
#     if 'generateContent' in i.supported_generation_methods:
#         print(i.name)

#Configurações do modelo
generation_config = {
    #Números de respostas dadas
    'candidate_count': 1,
    'temperature': 0.5
}

#Configurações de segurança
safety_settings = {
    'HARASSMENT': 'BLOCK_NONE',
    'HATE': 'BLOCK_NONE',
    'SEXUAL': 'BLOCK_NONE',
    'DANGEROUS': 'BLOCK_NONE'
}

#Inicializando o modelo
model = genai.GenerativeModel(
    model_name = 'gemini-1.0-pro',
    generation_config = generation_config,
    safety_settings = safety_settings
)

# Pegando resposta do modelo
# response = model.generate_content('Me dê 3 itens de higiene pessoal')
# print(response.text)

#Criando histórico do chat
chat = model.start_chat(
    history = []
)

#Conversa com o chat
prompt = input('Insira uma pergunta ou comando: ').lower()

while prompt != 'fim':
    response = chat.send_message(prompt)
    print('Resposta: ' + response.text + '\n')
    prompt = input('Insira uma pergunta ou comando: ').lower()