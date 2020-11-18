#!/usr/bin/python
import xml.etree.ElementTree as ET
import os
import sys, getopt

def clearName(name, isDir):
    name = name.replace('/', '-').replace(':', '').replace(',', '').replace('...', '').strip()
    if isDir != True:
        name = name.replace(' ', '.')
    return name

def getdirname(nfofile, add3D):
    tree = ET.parse(nfofile)
    root = tree.getroot()
    titleelement = root.find('title')
    yearelement = root.find('year')
    if add3D == True:
        return clearName(titleelement.text, True) + ' 3D (' + yearelement.text + ')'
    else:
        return clearName(titleelement.text, True) + ' (' + yearelement.text + ')'

def getfilename(nfofile, add3D):
    tree = ET.parse(nfofile)
    root = tree.getroot()
    titleelement = root.find('title')
    yearelement = root.find('year')
    videoelement = root.find('fileinfo').find('streamdetails').find('video')
    codecelement = videoelement.find('codec')
    widthelement = videoelement.find('width')
    size = 'SD'
    if int(widthelement.text) >= 480:
        size = '480p'
    if int(widthelement.text) >= 720:
        size = '720p'
    if int(widthelement.text) >= 1920:
        size = '1080p'

    if add3D == True:
        return clearName(titleelement.text, False) + '.' + yearelement.text + '.3D.' + codecelement.text.upper() + '.' + size
    else:
        return clearName(titleelement.text, False) + '.' + yearelement.text + '.' + codecelement.text.upper() + '.' + size

def renameMovieDir(newName, currentName, location):
    if newName == currentName:
        return False

    os.rename(location + '/' + currentName,location + '/' + newName)
    return True

def renameMovieFile(newName, file, location):
    filename, fileExtension = os.path.splitext(location + '/' + file)
    if fileExtension == '.jpg':
        if '-poster' in file:
            newName = newName + '-poster'
        elif '-fanart' in file:
            newName = newName + '-fanart'
        else:
           return False

    if fileExtension == '.srt' or fileExtension == '.ssa' or fileExtension == '.txt':
        if '.dut.' in file or '.nl.' in file:
            newName = newName + '.dut'
        else:
            newName = newName + '.eng'

    newName = newName + fileExtension
    if newName == file:
        return False

    os.rename(location + '/' + file, location + '/' + newName)
    return True

def main(argv):
    directory = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["directory="])
    except getopt.GetoptError:
        print('readNFO.py -d <directory>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('readNFO.py -d <directory>')
            sys.exit()
        elif opt in ("-d", "--directory"):
            directory = arg

    if not directory:
        print('readNFO.py -d <directory>')
        sys.exit()

    for dirname in os.listdir(directory):
        shouldRename = True
        is3DMovie = False
        nfoLocation = ''
        renamedFiles = []
        for filename in os.listdir(directory + '/' + dirname):
            if filename.endswith(".nfo"):
                nfoLocation = directory + '/' + dirname + '/' + filename
                continue
            if filename.endswith(".iso"):
                shouldRename = False
                continue

        if shouldRename == True:
            newFilename = getfilename(nfoLocation, '3D' in nfoLocation)
            nfoLocation = directory + '/' + dirname + '/' + newFilename + '.nfo'
            for filename in os.listdir(directory + '/' + dirname):
                if renameMovieFile(newFilename, filename, directory + '/' + dirname) == True:
                   renamedFiles.append(directory + '/' + dirname + '/' + filename)

        newDirname = getdirname(nfoLocation,'3D' in nfoLocation)
        if renameMovieDir(newDirname, dirname, directory) == True:
            print(newDirname)
        for renamedFile in renamedFiles:
            print(renamedFile)

main(sys.argv[1:])
