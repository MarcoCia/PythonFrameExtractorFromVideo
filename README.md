
~~~bash
python extract.py -h
usage: Extract frames from videos [-h] [--video VIDEO | --dir DIR] [--sampling SAMPLING]                                       [--output_root OUTPUT_ROOT] [--workers WORKERS]

optional arguments:
      -h, --help            show this help message and exit
      --video VIDEO         set video filename
      --dir DIR             set videos directory
      --sampling SAMPLING   extract 1 frame every args.sampling seconds                                                 (default: extract all frames)
  --output_root OUTPUT_ROOT
                            set output root directory
  --workers WORKERS         Set number of multiprocessing workers
~~~



### Extract frames from a single video file

~~~
python extract.py --video=demo_videos/talking_dog.mp4
~~~



### Extract frames from a directory of video files

~~~
python extract.py --dir=demo_videos/
#. Extract frames from videos under dir : demo_videos/
#. Store extracted frames under         : extracted_frames
#. Extract all available frames.
#. Scan for video files...
100%|███████████████████████████████████████████████████| 3/3 [00:47<00:00, 15.94s/it]
~~~

Extracted frames are stored under `extracted_frames/`


Option A

SETUP.PY allow to create a exectutable file (.exe):
py setup.py py2exe

the command create a dist directory contains execute.exe

Option B

put file into C:\Users\m.cianciotta\AppData\Local\Programs\Python\Python39\Scripts>
open windows PowerShell
Execute: .\pyinstaller --onefile -w extract.py
