from pypro.aperitivos.models import Video
from django.shortcuts import render

videos = [
    Video(slug='oo', titulo='Vídeo Aperitivo: OO em Python sem sotaque', vimeo_id='856570782'),
    Video(slug='iot', titulo='IOT com Luciano Ramalho', vimeo_id='861071461'),
]


videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
