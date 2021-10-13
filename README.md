### **Purpose**

This repo is prepared for audio file conversation from ***.mp3 , .mp4 , etc*** to **.wav** format. It is prepared for win machine, if you use in linux need to take care of folder/file separator ('\\', '/' )

### **How is work**

The user can use class for conversation, the only need is give file format (that also related folder name of source audio files) and the class does the rest (creates new fodler and convert all audio file autoimatically to wav and save in the new folder)

```python
from audio_converter2wav import AudioConverter2Wav

audio_converter = AudioConverter2Wav(read_f='.mp3')
result = audio_converter.convert_files() #if result == True , the process is succesfully complated 
```
It is reading main folder / source folder (in source code I share '.mp3' as an example) and convert all audio file to requested one separately. 

### **Depandencies**

This repo prepared pretty fast and only use **moviepy** module. In normal case, **pydub** is more advance one for audio file precessing but pydub request some extra installment like ff** etc. So this sample code is company-laptop friendly solution :)

### **How can I test class/scrip is everythongs all right**

Also, is prepared **test_xx** scrip for unit testing. The user can test for its own purpose. 


