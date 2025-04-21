from django.shortcuts import render, redirect
from googletrans import Translator

def indexView(request):
    if request.method == 'POST':
        translator = Translator()
        lang1 = request.POST.get('from')
        lang2 = request.POST.get('to')
        text = request.POST.get('text')
        translated = translator.translate(text, src=lang1, dest=lang2)
        return render(request, 'shablon/index.html', {'text': translated.text})

    return render(request, 'shablon/index.html')
