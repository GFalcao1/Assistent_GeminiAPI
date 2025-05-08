import google.generativeai as gemini
from dotenv import load_dotenv
import os
import time
import sounddevice as sound
from scipy.io.wavfile import write
from faster_whisper import WhisperModel




load_dotenv()

gemini.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = WhisperModel("base")

def gravador (nome_arquivo="gravacao_10s.wav", duracao=10, fs=16000):
    print("***GRAVANDO***")
    audio = sound.rec(int(duracao * fs), samplerate=fs, channels=1)
    sound.wait()
    write(nome_arquivo, fs, audio)
    print("áudio salvo.")
    return nome_arquivo

def transcrever(caminho):
    segments, _ = model.transcribe(caminho)
    texto = " ".join([seg.text for seg in segments])
    return texto

def respostas(pergunta):
    chat = gemini.GenerativeModel("gemini-2.0-flash").start_chat(history=[])
    resposta = chat.send_message(
        f"Aja como um assistente de um professor de inglês em aula ao vivo com seu aluno. Ajude o professor a desenvolver a aula com perguntas para os alunos, com base no diálogo que ele tiver com seu aluno.: \"{pergunta}\"")
    return resposta.text

def call_realtime():
    while True:
        caminho_audio = gravador()
        texto = transcrever(caminho_audio)
        print(f"\nTranscrição: {texto}\n")
        if texto.strip():
            resposta = respostas(texto)
            print(f"Resposta geradas: {resposta}\n")

        time.sleep(1)


if __name__ == "__main__":
    print("Ativando assistente...")
    call_realtime()