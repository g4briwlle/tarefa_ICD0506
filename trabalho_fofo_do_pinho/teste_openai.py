from openai import OpenAI

client = OpenAI(api_key=userdata.get("OPENAI_API_KEY"))

prompt = [{"role": "user", "content": "o que é pneumoultramicroscopicosilicovulcanoconiótico"}]

response = client.chat.completions.create(
    messages=prompt,
    model="gpt-3.5-turbo-0125",
    max_tokens=100,
    temperature=0
)

print(response)
