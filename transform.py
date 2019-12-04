filev = open("twitter.e", "r")
fileout = open("twitter-kws.e", "w")

for line in filev:
    data = line.split("\t")
    fileout.write(data[0] + "\t" + data[1] + "\t1\n")

fileout.flush()
fileout.close()
