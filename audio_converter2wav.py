import os
from moviepy.editor import *


class AudioConverter2Wav():
    
    def __init__(self,read_f:str , target_f:str='.wav', codec:str="pcm_s16le", channel:int=2, fr:int=16000):
        self.sample_rate = fr
        self.channel = channel
        self.codec = codec
        self.read_format = read_f
        self.target_format = target_f
        self.read_path = read_f.split('.')[-1]
        self.target_path = target_f.split('.')[-1]
    
    def get_audio_files(self, aformat)->(dict):
        '''use audio files folder and creates audio_file dict={filename:lang} for use'''
        mypath = aformat.split('.')[-1]
        onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
        specific_files = [f for f in onlyfiles if aformat in f]
        audio_files = {( mypath + '\\' + f):(f.split('__')[0]) for f in specific_files}
        #print('*'*10 , f'| {aformat} |', audio_files, '*'*10)
        return audio_files
    
    def compare_folder(self):
        '''using mypath, read_f and target_f compare every file is created or not'''
        readfiles, targetfiles = self.get_audio_files(self.read_format), self.get_audio_files(self.target_format)

        for key,val in readfiles.items():
            searchK = self.target_path + '\\'+ key.split('\\')[-1].split('.')[0] + self.target_format
            if searchK not in targetfiles:
               return False 
        return True
    
    def create_folder_if_nec(self, folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
    def convert_files(self):
        ''' read all au file and convert them'''
        for filename, lang in self.get_audio_files(self.read_format).items(): #read files
            # convert wav to mp3
            try:                                                            
                audioclip = AudioFileClip(filename)
                filename = filename.split('\\')[-1]
                newfolder, name = self.target_path , filename.split('.')[0]
                new_filename = newfolder + '\\'+ name +self.target_format
                self.create_folder_if_nec(newfolder) #create if nec
                #print('#'*10 , f'| {new_filename} | {newfolder} | {name} |', '#'*10)
                audioclip.write_audiofile(new_filename, fps=self.sample_rate, nbytes=self.channel, buffersize=2000,bitrate=None, codec=self.codec)
            except Exception as e:
                print(f'Error: <{e}>')
                return False
                
        '''check if all files created'''
        return True if self.compare_folder() else False

#activate if necessary
'''
if __name__ == "__main__":
    audio = AudioConverter2Wav(read_f='.mp3', target_f='.wav')
    result = audio.convert_files()
    print(f'***** file translation: {result} *****') 
'''