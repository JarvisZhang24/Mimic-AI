import modal

app = modal.App("chatterbox-tts-generator")



image = (
    modal.Image.debian_slim(python_version = "3.11")
    .pip_install_from_requirements("textTospeech/requirements.txt")
    .apt_install("ffmpeg")

)


