from inaSpeechSegmenter import Segmenter, seg2csv
from pydub import AudioSegment

class cnn_segs:
    def __init__(self):
        print("\ncnn_segs init...")
        self.seg = Segmenter()

    def segs(self, path, file):
        print("\nsegs...")

        segmentation = self.seg(path + file)
        print(segmentation)

        segs=[]
        for seg in segmentation:
            if seg[0]== 'male' or seg[0]== 'female':
                segs.append( seg )
        print(segs)

        if not segs: return
        
        audio= AudioSegment.from_wav(path+file )
        audios= audio[ segs[0][1]*1000 : segs[0][2]*1000 ] 

        for seg in segs[1:]:
            audios = audios + audio[ seg[1]*1000 : seg[2]*1000 ]

        audios.export(path + "seg_cnn.wav" , format="wav")
        print("done")

path = 'data/'
file= 'full.wav'

CS= cnn_segs()
CS.segs(path, file)







