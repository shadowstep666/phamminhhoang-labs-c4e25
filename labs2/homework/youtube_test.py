from youtube_dl import YoutubeDL

#1. download single youtube video
dl=YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=qKU9fST7-_E'])#put video want to download

#2. download mutilple youtube video 
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=IBAVuzZAdmE','https://www.youtube.com/watch?v=P_xFh7XFC_w','https://www.youtube.com/watch?v=EehyUebz2J4','https://www.youtube.com/watch?v=bZX8jmfwbnE'])


#3. download audio
option = {
    'format' : 'bestaudio/audio' #download  the best quality of audio
}
dl=YoutubeDL(option)
dl.download(['https://www.youtube.com/watch?v=WHyzxVlOI98'])

#4.search and download first video
option={
    'default_search' : 'ytsearch' ,
    'max_downloads' : 1 ,
}
dl=YoutubeDL(option)
dl.download('shayne ward until you')


#5.search and download first video
option={
    'default_search' : 'ytsearch' ,
    'max_downloads' : 1 ,
    'format':'bestaudio/audio'
}
dl=YoutubeDL(option)
dl.download('betrayal')