from google.cloud import speech_v1p1beta1

def main():

    client = speech_v1p1beta1.SpeechClient.from_service_account_json('key.json')

    #gcs_uri = "gs://edward-raw/audio/teste_speech_to_texto.mp3"
    gcs_uri = "gs://edward-raw/audio/test.mp3"
    audio = speech_v1p1beta1.RecognitionAudio(uri=gcs_uri)

    config = speech_v1p1beta1.RecognitionConfig(
        encoding=speech_v1p1beta1.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=16000,
        language_code="pt-BR",
    )

    print("Waiting for operation to complete...")
    # Audio Longo
    #operation = client.long_running_recognize(config=config, audio=audio)
    #response = operation.result(timeout=100000)
    # Audio Curto
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(u"Transcript: {}".format(result.alternatives[0].transcript))


if __name__ == '__main__':
    main()


# attention
#https://cloud.google.com/speech-to-text/quotas?hl=pt-br