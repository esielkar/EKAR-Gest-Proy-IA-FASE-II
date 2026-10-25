import requests
import sys

def verificar_modelo_ollama():
    url = "http://ollama:11434/api/tags"
    print("[INFO] Conectando con el motor de IA en el NAS...")
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("[EXITO] ¡Conexión exitosa con Ollama!")
            print("Modelos disponibles:", response.json().get("models", []))
        else:
            print(f"[ADVERTENCIA] Respuesta inesperada: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] No se pudo conectar a Ollama: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verificar_modelo_ollama()