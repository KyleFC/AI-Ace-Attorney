import openai
import moviepy.editor as mp

def movie_maker(topic):
    
    with open('key.txt', 'r') as f:
        openai.api_key = f.read().strip()

    script = script_maker(topic)
    parsed_script = parse_script(script)
    character_images = {
        'Phoenix': 'assets/placeholder_def.png',
        'Miles': 'assets/placeholder_pro.png',
        'Judge': 'assets/placeholder_judge.png'
    }
    clips = []
    print(len(parsed_script))

    for line in parsed_script:
        if len(line) == 2:
            character, dialogue = line  
            image = mp.ImageClip(character_images[character])
            text = mp.TextClip(dialogue, fontsize=40, bg_color='grey', color='white', method='caption', size=(image.size[0],200))
            text = text.on_color(col_opacity=.4)
            scene = mp.CompositeVideoClip([image, text.set_position(('center', 'bottom'))])
            scene.duration = 5
            clips.append(scene)
        else:
            pass

    #combine clips
    video = mp.concatenate_videoclips(clips)
    #output. need to figure out how to get this working with server
    video.write_videofile("output.mp4", fps=1)
    

def parse_script(script):
    lines = script.split('\n')
    parsed_script = []

    for line in lines:
        if line.startswith('['):
            end_bracket = line.find(']')
            character = line[1:end_bracket]
            text = line[end_bracket+2:]
            parsed_script.append((character, text))
        else:
            parsed_script.append(line)

    return parsed_script

def script_maker(topic):

    with open('prompt.txt', 'r') as f:
        system_prompt = f.read().strip()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": system_prompt},
            {"role": "user", "content": topic}
        ]
    )

    print("Created Script")
    script = response['choices'][0]['message']['content']
    print(f"Script:\n{script}\n\n")
    return script

if __name__ == "__main__":
    print("--------------movie_maker tests------------")
    print("creating video with topic [Best Console]")
    video = movie_maker("best console")
    print("created video output.mp4")

