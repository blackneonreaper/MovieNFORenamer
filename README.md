# MovieNFORenamer
Python3 script to rename movie files based on NFO data

## Commands
- python3 readNFO.py -d `<directory>`
- python3 readNFO.py -h

Created for Jellyfin NFO files only support dut and eng srt files  
I needed to add the quality and codec to the movie file name to to have Radarr read it properly  
This will skip iso files since these can't be read by any media server  
Movies must be placed in a separated folder

## Before:
2fast2furious/
- 2 Fast and Furious.dut.srt
- english.srt
- 2 Fast 2 Furious-poster.jpg
- 2 Fast 2 Furious.mp4
- 2 Fast 2 Furious.nfo
- poster.jpg
- fanart.jpg

## After:
2 Fast 2 Furious (2003)/
- 2.Fast.2.Furious.2003.H264.1080p.dut.srt
- 2.Fast.2.Furious.2003.H264.1080p.eng.srt
- 2.Fast.2.Furious.2003.H264.1080p-poster.jpg
- 2.Fast.2.Furious.2003.H264.1080p.mp4
- 2.Fast.2.Furious.2003.H264.1080p.nfo
- poster.jpg
- fanart.jpg

## Extra command to find and clean up your directory:
#find files larger then Xsize and group by containing dir
- find . -maxdepth 1 -type d | while read -r dir; do printf "%s:\t" "$dir"; find "$dir" -type f -size +100M | wc -l; done  
#find empty diretories
- find . -type d -empty -print  
#find and delete empty directories
- find . -type d -empty -delete
#find and group by extention  
-find . -type f | perl -ne 'print $1 if m/\.([^.\/]+)$/' | sort -u
#find files and group by extension per directory  
- find . -type f -iname '*.nfo' -printf '%h\n'|sort|uniq -c | awk '$1 > 1'
