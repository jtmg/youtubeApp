import pafy
class youtube():
    def __init__(self,url):
    #url = "https://www.youtube.com/watch?v=TyvjLiYPR4c"
        self.video= pafy.new(url)
        audiostreams = self.video.audiostreams
        self.files = dict()
        index = 0
        for a in audiostreams:
            if (a.extension == "m4a"):
                aux = a.bitrate
                bitrate = int (aux[:-1])
                self.files.update({"m4a":[bitrate,index]})
            index += 1
        try:
            
            audiostreams[self.files["m4a"][1]].download(quiet=True,filepath="D:\\Documents\\youtube\\tracks")
        except:
            raise
        #fazer verificação se fichei ja existe

