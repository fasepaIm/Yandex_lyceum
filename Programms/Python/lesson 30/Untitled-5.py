import wave
import struct


def break_the_silence():
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")
    newdata = []
 
    dest.setparams(source.getparams())

    frames_count = source.getnframes() 
 
    data = struct.unpack("<" + str(frames_count) + "h",
                         source.readframes(frames_count))
                        
    for i in range(frames_count):
        if not -5 <= data[i] <= 5:
            newdata.append(data[i])
    
    newdata = tuple(newdata)
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

    dest.writeframes(newframes) 
    source.close()
    dest.close()