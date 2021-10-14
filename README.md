### **Purpose**

This repo is prepared for audio file conversation from ***.mp3 , .mp4 , etc*** to **.wav** format. It is prepared for win machine, if you use in linux need to take care of folder/file separator ('\\', '/' )

### **How is work**

The user can use class for conversation, the only need is giving file format (that also related folder name of source audio files) and the class does the rest (creates a new folder and convert all audio file automatically to wav and save in the new folder)

```python
from audio_converter2wav import AudioConverter2Wav

audio_converter = AudioConverter2Wav(read_f='.mp3')
result = audio_converter.convert_files() #if result == True , the process is succesfully complated 
```
It is reading the main folder/source folder (in source code I share '.mp3' as an example) and convert all audio files to the requested one separately. 

### **Depandencies**

This repo prepared pretty fast and only use **moviepy** module. In a normal case, **pydub** is a more advanced one for audio file processing but pydub requests some extra installment like ff**, etc. So this sample code is a company-laptop friendly solution :)

### **How can I test class/scrip is everything all right**

Also, is prepared **test_xx** scrip for unit testing. The user can test for its purpose. 
