import psutil
import json
import configparser
from pathlib import Path
from datetime import datetime

pathtoconfig = Path("sanityconfig.conf")
path = pathtoconfig.name

def readConfig(somepath):
    readparser = configparser.RawConfigParser()
    readparser.read(somepath)
    output = readparser.get("Common", "output")
    interval = readparser.getfloat("Common", "interval")
    result = [output, interval]
    readparser.clear()
    return result

def writeConfigSample(somepath):
    writeparser = configparser.RawConfigParser()
    writeparser.add_section('Common')
    writeparser.set('Common', 'output', 'json')
    writeparser.set('Common', 'interval', '2')
    with open(somepath, 'w') as configfile:
        writeparser.write(configfile)
    writeparser.clear()


def defaults():
    output = "log"
    interval = 5
    result = [output, interval]
    return result

def sanityCheck(linenumber):
    SNAP = "SNAPSHOT%d\t" % linenumber
    DT = str(datetime.now().date()) + " " + str(datetime.now().strftime('%H:%M:%S')) + " : "
    CPU = str(psutil.cpu_percent(interval=0.5, percpu=True)) + "\t"
    MEM =  str(psutil.swap_memory().used) + "\t"
    VMEM = str(psutil.virtual_memory().used) + "\t"
    IOinf = str(psutil.disk_io_counters()) + "\t"
    NET = str(psutil.net_if_stats()) + "\n"
    strline = SNAP + DT + CPU + MEM + VMEM + IOinf + NET
    jsonline = {'snapshot': SNAP[:-1], 'date': DT[:-3], 'cpu': CPU[:-1], 'memory': MEM[:-1], 'virtmemory': VMEM[:-1], 'ioinf': IOinf[:-1], 'network': NET[:-1]}
    result = [jsonline, strline]
    return result

def executesanityCheck():
    if pathtoconfig.is_file():
        configuration = readConfig(path)

    else:
        configuration = defaults()

    if configuration[0] == "json":
        if Path("sanity.json").is_file():
            with open("sanity.json", mode='r') as rjson:
                data = json.load(rjson)
                counter = len(rjson.readlines()) + 1
                data.update(sanityCheck(counter)[0])
            with open("sanity.json", mode='w') as rjson:
                json.dump(data, rjson)
        else:
            with open("sanity.json", mode='w') as rjson:
                json.dump(sanityCheck(1)[0], rjson)
    else:
        outputpath = Path("sanity.%s" % configuration[0])
        if outputpath.is_file():
            outputfile = open(outputpath, mode="r+")
            counter = len(outputfile.readlines()) + 1
        else:
            outputfile = open(outputpath, mode="w")
            counter = 1
        outputfile.write(sanityCheck(counter)[1])
        outputfile.flush()
        outputfile.close()

#writeConfigSample(pathtoconfig)
executesanityCheck()
