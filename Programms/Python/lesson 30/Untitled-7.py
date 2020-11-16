import wave
import struct


def pitch_and_toss():
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")
 
    dest.setparams(source.getparams())
 
    frames_count = source.getnframes()
    cnt_in_one = frames_count // 4
 
    data = struct.unpack("<" + str(frames_count) + "h",
                         source.readframes(frames_count))
    data = list(data)

    first = data[:cnt_in_one]
    second = data[cnt_in_one:cnt_in_one * 2]
    thirt = data[cnt_in_one * 2:cnt_in_one * 3]
    fourth = data[cnt_in_one * 3:]

    newdata = tuple(thirt + fourth + first + second)

    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata) 

    dest.writeframes(newframes) 
    source.close()
    dest.close()
