""" GPT Chosen Word """

from openai import OpenAI


def gpt_word(lingua, dificuldade, tamanho):
    client = OpenAI(api_key="chave")

    prompt = [{"role": "user", "content": f"Chat, seu trabalho é gerar uma palavra na língua {lingua} que seja de {dificuldade} dificuldade e tenha {tamanho} letras. o resultado gerado precisa ser apenas a palavra, sem nenhum comentário antes ou depois e a palavra precisa ter seus acentos removidos."}]

    response = client.chat.completions.create(
        messages=prompt,
        model="gpt-3.5-turbo-0125",
        max_tokens=200,
        temperature=1
    )

    resposta = response.choices[0].message.content
    return resposta.lower()