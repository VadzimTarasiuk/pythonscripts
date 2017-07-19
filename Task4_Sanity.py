import psutil
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
    writeparser.set('Common', 'interval', '1')
    with open(somepath, 'w') as configfile:
        writeparser.write(configfile)
    writeparser.clear()


def defaults():
    output = "log"
    interval = 0.5
    result = [output, interval]
    return result

def sanityCheck(interval, linenumber):
    SNAP = "SNAPSHOT%d\t" % linenumber
    DT = str(datetime.now().date()) + " " + str(datetime.now().strftime('%H:%M:%S')) + " : "
    CPU = str(psutil.cpu_percent(interval=interval, percpu=True)) + "\t"
    MEM =  str(psutil.swap_memory().used) + "\t"
    VMEM = str(psutil.virtual_memory().used) + "\t"
    IOinf = str(psutil.disk_io_counters()) + "\t"
    NET = str(psutil.net_if_stats()) + "\n"
    line = SNAP + DT + CPU + MEM + VMEM + IOinf + NET
    return line

def executesanityCheck():
    if pathtoconfig.is_file():
        configuration = readConfig(path)
        outputpath = Path("sanity.%s" % configuration[0])
    else:
        configuration = defaults()
        outputpath = Path("sanity.%s" % configuration[0])

    if outputpath.is_file():
        outputfile = open(outputpath, mode="r+")
        counter = len(outputfile.readlines()) + 1
    else:
        outputfile = open(outputpath, mode="w")
        counter = 1
    outputfile.write(sanityCheck(configuration[1], counter))
    outputfile.flush()
    outputfile.close()

#writeConfigSample(pathtoconfig)
executesanityCheck()
