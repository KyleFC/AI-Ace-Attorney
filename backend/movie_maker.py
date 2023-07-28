import openai
openai.api_key_path = "key.txt"
system_prompt = "prompt.txt"

def movie_maker(topic):
    script = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"syste", "content":system_prompt}, {"role": "user", "content": topic}])
    return script

if __name__ == "__main__":
    pass

