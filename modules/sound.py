from pygame import mixer, time

LOADED = {}
PLAYING = {}

mixer.init(11025)

def _randid():
    if not PLAYING: return 0
    return max(PLAYING.keys()) + 1

def load_effect(name):
    """
    load_effect(name) -- Preload the named sound effect to reduce initial
        playback latency.
    """
    LOADED[name] = mixer.Sound(name)

def play_effect(name, volume=0.5, pitch=1):
    if name in LOADED:
        sound = LOADED[name]
    else:
        sound = mixer.Sound(name)
    sound.play()
    id = _randid()
    PLAYING[id] = sound
    return id

def stop_effect(effect_id):
    PLAYING[effect_id].stop()
    del PLAYING[effect_id]
