from pytube import YouTube

def download_video(url, output_path='./'):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if video:
            video.download(output_path)
            print(f'Download completo: {video.title}')
        else:
            print('Não foi possível encontrar vídeo disponível para download.')
    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')

# Exemplo de uso
if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=xsWA4IdcKk8'
    download_video(video_url)
