from EVENT_EXCEL import *

Main(20, -64, 256, -64, 511)
dec = gzip.decompress(open("sstates/SLUS_011.15.001", "rb").read())
dat = Br(io.BytesIO(dec))
dat.seek(0xBD9F2)
dat.write(b"\x00\x00\x00\x00")
decNew = gzip.compress(dat.getdata(), compresslevel=9, mtime=None)
out = open("sstates/SLUS_011.15.001", "wb").write(decNew)
