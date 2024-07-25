import vosk

model = vosk.Model("model")  # Remplacez par le chemin correct

# Essayez de charger le modèle
try:
  kaldi_recognizer = vosk.KaldiRecognizer(model, 16000)
  print("Modèle Vosk chargé avec succès !")
except Exception as e:
  print(f"Une erreur est survenue lors du chargement du modèle : {e}")