import mechanize
import gzip


class fetch:

    @staticmethod
    def disp_links(db):
        br = mechanize.Browser()
        br6 = mechanize.Browser()
        base_year = 2007
        base_month = "08"
        base_day = "01"
        base_link = "http://data.caida.org/datasets/routing/routeviews-prefix2as"
        base_link6 = "http://data.caida.org/datasets/routing/routeviews6-prefix2as"


        for iyear in range(base_year,3000,1):
            index = "{}/{}/{}/".format(base_link,iyear,base_month)
            index6 = "{}/{}/{}/".format(base_link6,iyear,base_month)
            date = "{}{}{}".format(iyear,base_month,base_day)
            try:
                br.open(index)
                br6.open(index6)
            except (mechanize.HTTPError,mechanize.URLError):
                return

            mask_count = [0] * 32
            zipfname = ""
            tot = 0
            tot_type = 0
            dis = 0

            mask_count6 = [0] * 128
            zipfname6 = ""
            tot6 = 0
            tot_type6 = 0
            dis6 = 0

            #ipv4
            for link in br.links():
                zipfname = link.text
                if date in zipfname:
                    print zipfname
                    br.retrieve(index + zipfname, zipfname)
                    dec_stream = gzip.open(zipfname)

                    maskmin = 8-1
                    maskmax = 24-1

                    t = pxtree.Tree()

                    for line in dec_stream:
                        entry = line.split("\t")
                        px = entry[0]
                        mask = int(entry[1])
                        asn_guess = entry[2]

                        if maskmin <= (mask-1) <= maskmax:
                            mask_count[mask-1] += 1
                            tot += 1
                            if ("_" not in asn_guess) and ("," not in asn_guess) and ("." not in asn_guess):
                                tot_type += 1
                                asn = int(asn_guess)
                                t.insert_px(px,mask,asn)
                        else:
                            dis += 1

                    stat_tmp = t.get_stat()

                    stat_v4 = pxtree.Stat()
                    stat_v4.dea = stat_tmp.dea
                    stat_v4.dele = stat_tmp.dele
                    stat_v4.lon = stat_tmp.lon
                    stat_v4.top = stat_tmp.top

                    dec_stream.close()
                    os.remove(zipfname)
                    break


            #ipv6
            for link in br6.links():
                zipfname6 = link.text
                if date in zipfname6:
                    print zipfname6
                    br.retrieve(index6 + zipfname6, zipfname6)
                    dec_stream = gzip.open(zipfname6)

                    maskmin = 16-1
                    maskmax = 48-1

                    t6 = pxtree.Tree()

                    for line in dec_stream:
                        entry = line.split("\t")
                        px = entry[0]
                        mask = int(entry[1])
                        asn_guess = entry[2]

                        if maskmin <= (mask-1) <= maskmax:
                            mask_count6[mask-1] += 1
                            tot6 += 1
                            if ("_" not in asn_guess) and ("," not in asn_guess) and ("." not in asn_guess):
                                tot_type6 += 1
                                asn = int(asn_guess)
                                t6.insert_px_v6(px,mask,asn)
                        else:
                            dis6 += 1





                    stat_tmp = t6.get_stat()

                    stat_v6 = pxtree.Stat()
                    stat_v6.dea = stat_tmp.dea
                    stat_v6.dele = stat_tmp.dele
                    stat_v6.lon = stat_tmp.lon
                    stat_v6.top = stat_tmp.top


                    dec_stream.close()
                    os.remove(zipfname6)
                    break



            db.session.add(main.AddStruct(int(date),iyear,8,1,tot, dis, index, zipfname,mask_count,tot6,dis6, index6, zipfname6,mask_count6, stat_v4.dea, stat_v4.top, stat_v4.lon, stat_v4.dele, stat_v6.dea, stat_v6.top, stat_v6.lon, stat_v6.dele, tot_type, tot_type6))
            db.session.commit()
