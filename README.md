# MovieNFORenamer
Python script to rename movie files based on NFO data

## Commands
- readNFO.py -d '<directory>'
- readNFO.py -h

Created for Jellyfin NFO files only support dut and eng srt files  
I needed to add the quality and codec to the movie file name to to have Radarr read it properly  
This will skip iso files since these can't be read by any media server  

## Before:
- 2 Fast and Furious.dut.srt
- english.srt
- 2 Fast 2 Furious-poster.jpg
- 2 Fast 2 Furious.mp4
- 2 Fast 2 Furious.nfo
- poster.jpg
- fanart.jpg

## After:
- 2.Fast.2.Furious.2003.H264.1080p.dut.srt
- 2.Fast.2.Furious.2003.H264.1080p.eng.srt
- 2.Fast.2.Furious.2003.H264.1080p-poster.jpg
- 2.Fast.2.Furious.2003.H264.1080p.mp4
- 2.Fast.2.Furious.2003.H264.1080p.nfo
- poster.jpg
- fanart.jpg
