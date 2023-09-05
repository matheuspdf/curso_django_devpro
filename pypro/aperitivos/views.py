from django.shortcuts import render


def video(request, slug):
    videos = {
        'oo': {'titulo': 'Vídeo Aperitivo: OO em Python sem sotaque', 'vimeo_id': 856570782},
        'iot': {'titulo': 'IOT com Luciano Ramalho', 'vimeo_id': 861071461}

    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
