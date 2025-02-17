from openai import OpenAI
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required

client = OpenAI(api_key=settings.OPENAI_API_KEY)


# @login_required
def chat_view(request):
    if request.method == "POST":
        try:
            user_message = request.POST.get("message", "").strip()

            if not user_message:
                return JsonResponse({"error": "A mensagem não pode estar vazia."}, status=400)

            chat_history = request.session.get("chat_history", [])

            chat_history.append({"role": "user", "content": user_message})

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=chat_history
            )

            response_json = json.loads(response.model_dump_json())

            if "choices" not in response_json or not response_json["choices"]:
                return JsonResponse({"error": "Resposta inválida da OpenAI."}, status=500)

            chat_response = response_json["choices"][0]["message"]["content"]

            chat_history.append(
                {"role": "assistant", "content": chat_response})

            request.session["chat_history"] = chat_history[-10:]

            return JsonResponse({"response": chat_response})

        except json.JSONDecodeError:
            return JsonResponse({"error": "A resposta da OpenAI não é um JSON válido."}, status=500)

        except Exception as e:
            return JsonResponse({"error": f"Erro inesperado: {str(e)}"}, status=500)

    return render(request, "chat/chat.html")
