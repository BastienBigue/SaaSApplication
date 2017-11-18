from gtts import gTTS
from projetB11.settings import MEDIA_ROOT
import pathlib

MAPPING_DAY = {1: "lundi", 2: "mardi", 3: "mercredi", 4: "jeudi", 5: "vendredi", 6: "samedi", 7: "dimanche"}
MAPPING_MONTH = {1: "janvier", 2: "fevrier", 3: "mars", 4: "avril", 5: "mai", 6: "juin", 7: "juillet", 8: "aout", 9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre"}


def taskToText(task) :
    text= "Pense à "+ task.title + " à "+task.lieu
    text+=" le " + MAPPING_DAY[task.date.isoweekday()] +" "+ str(task.date.day) +" "+ MAPPING_MONTH[task.date.month] +" "+ str(task.date.year)
    return text

def convertTaskToAudio(task):
    text=taskToText(task)
    tts = gTTS(text=text, lang='fr')
    fileName=("task"+str(task.id)+".mp3")
    OUTPUT_PATH=pathlib.Path(MEDIA_ROOT)
    tts.save(OUTPUT_PATH.joinpath("audio").joinpath(fileName))

