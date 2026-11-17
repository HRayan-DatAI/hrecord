"""Premier appel à l'API Mistral : envoyer un SMS fictif et lire la réponse."""
import os
import time

from mistralai.client import Mistral

SMS = "Bonjour, est-ce que je peux avoir un acompte de 200 € ce mois-ci ? Merci, Sarah"


def main() -> None:
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise SystemExit("MISTRAL_API_KEY manquante : vérifie ton fichier .env")

    with Mistral(api_key=api_key) as client:
        start = time.perf_counter()
        response = client.chat.complete(
            model="mistral-small-latest",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "Tu analyses des SMS envoyés par des salariés à leur gérante. "
                    "Indique en une phrase le type de demande et les informations clés.",
                },
                {"role": "user", "content": SMS},
            ],
        )
        elapsed = time.perf_counter() - start

    print("Réponse :", response.choices[0].message.content)
    print(f"Tokens  : {response.usage.prompt_tokens} en entrée, {response.usage.completion_tokens} en sortie")
    print(f"Latence : {elapsed:.2f} s")


if __name__ == "__main__":
    main()