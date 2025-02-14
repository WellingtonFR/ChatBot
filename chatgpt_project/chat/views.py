from openai import OpenAI
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def chat_view(request):
    if request.method == "POST":
        try:
            user_message = request.POST.get("message", "")

            response = client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}])

            chat_response = response.choices[0].message.content
            return JsonResponse({"response": chat_response})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, "chat/chat.html")
