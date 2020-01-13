import random
import datetime

start_phrases = [
    "Hallo Sjef!",
    "God dag til deg!",
    "Hva skjer a?",
    "Denne samtalen kan bli tatt opp.",
    "Hvordan har du det?",
    "Hallo mitt navn er Grenseveien.",
    "Jeg er Superman.",
    "Du vet hvem dette er?.",
    "Doktor.",
    "Hallo solstråle!",
    "Hallo partner!",
    "Jeg kommer i fred!"
]

end_phrases = [
    "Jeg er her, fortell meg hvis du trenger noe mere.",
    "Hade bra for nå!",
    "Snakkes",
    "Jeg gleder meg til å høre fra deg igjen, hade så lenge",
    "Gode venner sier aldri hade, men på gjensyn!",
    "Elvis, har forlatt bygningen!",
    "Din personlige assistent, har foraltt bygningen!",
    "Du kommer tilbake. Jeg vet at du vil...",
    "hade bra for denne gang...",
    "Kom snart tilbake.",
    "Til vi ses igjen...",
    "Jeg er her, hvis du ikke kobler meg i fra da........"
]

def handleLaunchText():
    prompt = random.choice(start_phrases) +" Hvordan kan jeg hjelpe deg?"

    return prompt
    
def handleCancelText():
    prompt = random.choice(end_phrases)

    return prompt