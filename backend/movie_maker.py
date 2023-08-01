import openai
import moviepy.editor as mp

def movie_maker(topic):
    
    with open('key.txt', 'r') as f:
        openai.api_key = f.read().strip()

    script = script_maker(topic)
    parsed_script = parse_script(script)
    character_images = {
        'PHOENIX': 'assets/placeholder_def.png',
        'MILES': 'assets/placeholder_pro.png',
        'JUDGE': 'assets/placeholder_judge.png',
        'OBJECTION!': 'assets/objection.png',
        'OBJECTION': 'assets/objection.png',
        'TAKE THAT!': 'assets/takethat.png',
        'TAKE THAT': 'assets/takethat.png',
        'HOLD IT!': 'assets/takethat.png',
        'HOLD IT': 'assets/takethat.png'

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
            scene.duration = 6
            clips.append(scene)
        else:
            character = line
            image = mp.ImageClip(character_images[character])
            scene = mp.CompositeVideoClip([image.set_position(('center'))], size=mp.ImageClip(character_images["PHOENIX"]).size)
            scene.duration = 2
            clips.append(scene)

    #combine clips
    video = mp.concatenate_videoclips(clips)
    #output. need to figure out how to get this working with server
    video.write_videofile("output.mp4", fps=1)
    

def parse_script(script):
    lines = script.split('\n')
    parsed_script = []

    for line in lines:
        line = line.strip()
        if line.startswith('['):
            end_bracket = line.find(']')
            character = line[1:end_bracket]
            text = line[end_bracket+2:]
            parsed_script.append((character.upper(), text))
        elif line != '':
            parsed_script.append(line.upper())

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
    video = movie_maker("woodwinds suck")
    print("created video output.mp4")

