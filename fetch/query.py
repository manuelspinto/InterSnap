import mechanize, gzip, os

class addQuery:

    @staticmethod
    def run_query(day, month, year, ipver):

        if ipver == 'ipv4':
            root_dir = "http://data.caida.org/datasets/routing/routeviews-prefix2as"
        else:
            root_dir = "http://data.caida.org/datasets/routing/routeviews6-prefix2as"

        br = mechanize.Browser()
        dir = "{}/{}/{}/".format(root_dir,year,month)
        date = "{}{}{}".format(year,month,day)

        try:
            br.open(dir)
        except (mechanize.HTTPError,mechanize.URLError):
            return -1

        if ipver == 'ipv4':
            mask_count = [0] * 32
        else:
            mask_count = [0] * 128

        tot = 0
        dis = 0

        for link in br.links():
            zipfname = link.text
            if date in zipfname:
                br.retrieve(dir + zipfname, zipfname)
                dec_stream = gzip.open(zipfname)

                if ipver == 'ipv4':
                    maskmin = 8-1
                    maskmax = 24-1
                else:
                    maskmin = 16-1
                    maskmax = 48-1

                for line in dec_stream:
                    entry = line.split("\t")
                    mask = int(entry[1])
                    if maskmin <= (mask-1) <= maskmax:
                        mask_count[mask-1] += 1
                        tot += 1
                    else:
                        dis += 1

                dec_stream.close()
                os.remove(zipfname)

                return QueryRes(tot,dis,zipfname,mask_count, dir + zipfname)

class QueryRes:

    def __init__(self, tot,dis,zipfname,mask_count,fullfile):
        self.tot = tot
        self.dis = dis
        self.zipfname = zipfname
        self.mask_count = mask_count
        self.fullfile = fullfile
