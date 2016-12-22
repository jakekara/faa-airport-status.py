import airports, airportstatus, json, time, sys


def get_all():
    ret = {}
    total = len(airports.airports)
    so_far = 0
    errors = 0
    for airport in airports.airports:
        try:
            ret[airport[0]] = airportstatus.get_status(airport[0])
            # ret.append(airportstatus.get_status(airport[0]))
            # print json.dumps(airportstatus.get_status(airport[0]),indent=2)
            # pass
        except:
            errors += 1
            pass

        so_far += 1
        msg = str(so_far) +  " out of " + str(total) +  " airports checked ("\
              + str(errors) + " errors)"
        sys.stdout.write("\r%s" % msg)
        sys.stdout.flush()
        time.sleep(0.1)

        # if so_far > errors:
        #     return ret
        
    return ret


a = get_all()
outfh = open("all.json","w")
outfh.write(json.dumps(a))
outfh.close()
