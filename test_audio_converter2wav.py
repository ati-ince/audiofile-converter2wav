import unittest
from audio_converter2wav import AudioConverter2Wav

class TestAudioConverter(unittest.TestCase):
    
    def setUp(self):
        '''Initilizer, set audio file formats for test'''
        pass
    
    def test_convert_files_mp3_wav(self):
        audio_converter = AudioConverter2Wav(read_f='.mp3')#, target_f='.wav')
        self.assertTrue(audio_converter.convert_files())
        
if __name__ == '__main__':
    unittest.main()