from pydub import AudioSegment

token = '5106366099:AAGNu5aUYOLrhxastPowyUcom-cuZ4Q_b7o'

def send_files(chat_id):
    files = os.listdir(new_path)
    for i in files:
        if i != '.DS_Store':
            f = open(new_path + '/' + i, 'rb')
            msg = bot.send_voice(chat_id, f)
            file_id = msg.voice.file_id
            print(file_id)
def add_music(i):
    song = AudioSegment.from_mp3(from_path + i)
    needed = song[30 * 1000:45 * 1000 + 1]
    needed.export(new_path + i, format="mp3")

def open_files():
    files = os.listdir(from_path)
    for i in files:
        if i != '.DS_Store':
            add_music('/' + i)
open_files()