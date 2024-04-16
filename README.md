# VolumeVeto

## Project Objective
**This project creates a tool for creators to quickly check their final product for any unexpected audio spikes or general level shifts.**

I have been taking classes on Udemy, but have noticed that many teachers seem to have little awareness of their recording levels. This can severely detract from the learnings because it forces the student to sit on the volume slider and push and pull it to keep the teacher audible, or keeps the student staring at the timer to try to cut the intro or outro music that is cut in far louder than everything else.

I also like to have Youtube videos or Twitch steams playing in the background while I work, but every once and a while an alert or sound effect is so egregiously loud that I have to switch creators, playlists or streams.  

This initial project creates a tool for creators to quickly check recordings for these recording anomalies.  I would like to move this into a plugin for live streaming or video consumers, but Python is not the ideal language for high speed audio processing.  (There might be a way to make something like this work on OBS with Python with some additional setup and their scripting features)

## Project Overview
This project scrubs through the audio portion of a file with different windows to detect the aforementioned anomalies.

A timeline will be displayed with a report on what was found.

- Pydub, Soundfile, and Pyloudnorm are used for audio metering throughout this project.  (ACTAULLY MIGHT NOT NEED Pydub BECUASE IM NOT DOING CUTS ANYMORE?)
    - Although I intend to get this app hosted, if you want to run this locally in the short term ffmpeg needs to be added to your path for pydub to work properly.    
