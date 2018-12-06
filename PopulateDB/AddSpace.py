import sys

class AddSpace:

    def __init__(self, v, fpath):
        if v == 4:
            AddSpaceIPv4(fpath)
        else:
            AddSpaceIPv6(fpath)


class AddSpaceIPv4:

    def __init__(self, fpath):
        self.fpath = fpath
        self.mask_count = [0] * 32
        self.get_counts()


    def get_counts(self):
        fp = open(self.fpath)
        read_lines = fp.read()

        print read_lines

        #for line in read_lines:
         #   print line
            #entry = line.split("\t")
            #mask = int(entry[1])
            #self.mask_count[mask-1] += 1
        return self.mask_count



    def write_results(self):
        fname = self.fpath.split("/")[1]
        new_fpath = "out/" + fname + ".csv"
        f = open(new_fpath,'w')

        tot = 0
        dis = 0
        for i in range(0,32,1):
            tot += self.mask_count[i]
            if i in range(8,24,1):
                dis += self.mask_count[i]
            f.write("{},{}\n".format(i+1,self.mask_count[i]))
        print "{}: Total pxs = {}".format(fname, tot)
        f.close()


class AddSpaceIPv6:

    def __init__(self, fpath):
        self.fpath = fpath
        self.mask_count = [0] * 128
        self.get_counts()
        self.write_results()


    def get_counts(self):
        with open(self.fpath) as lines:
            for line in lines:
                entry = line.split("\t")
                mask = int(entry[1])
                self.mask_count[mask-1] += 1

    def write_results(self):
        fname = self.fpath.split("/")[1]
        new_fpath = "out/" + fname + ".csv"
        f = open(new_fpath,'w')

        tot = 0
        dis = 0
        for i in range(0,128,1):
            tot += self.mask_count[i]
            if i in range(16,48,1):
                dis += self.mask_count[i]
            f.write("{},{}\n".format(i+1,self.mask_count[i]))
        dis = tot-dis
        print "{}: Total pxs = {}".format(fname, tot)
        f.close()
