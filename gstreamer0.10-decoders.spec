Summary:	Default GStreamer 0.10 decoders
Name:		gstreamer0.10-decoders
Version:	1
Release:	13
License:	GPLv2+ # spec file
Group:		Video
BuildArch:	noarch

# Please provide URL to sample which does not work without the
# package and works correctly with it, if adding new packages here.

# We want audio as well:
Requires:	%{name}-audio

# AC-3 decoder (popular multichannel audio codec), used usually
# only in videos:
# http://samples.mplayerhq.hu/A-codecs/AC3/liba52_altivec.avi
Suggests:	gstreamer0.10-a52dec

# MPEG-1/2 video decoder:
# http://samples.mplayerhq.hu/MPEG1/zelda%20first%20commercial.mpeg
Suggests:	gstreamer0.10-mpeg

# DTS multichannel audio decoder, used usually only in videos:
# http://samples.mplayerhq.hu/A-codecs/DTS/dtsac3audiosample.avi
Suggests:	gstreamer0.10-dts

# DV file support:
# http://samples.mplayerhq.hu/DV-raw/voxnews.dv
Suggests:	gstreamer0.10-dv

%description
Virtual package which installs the GStreamer 0.10 input plugins that
cover most of the usage cases.

This package can be suggested or required by software that uses
GStreamer to open media files, such as video players.

%package audio
Summary:	Default GStreamer 0.10 audio decoders
Group:		Sound

# Core plugins required for operation:
Requires:	gstreamer0.10-plugins-base

# HTTP protocol support:
# http://samples.mplayerhq.hu/A-codecs/GSM/countdown.wmv
Suggests:	gstreamer0.10-neon

# MMS protocol support:
# Used for live broadcasts, for example freely-viewable NASA TV.
# mms://63.250.197.124/bcenc202056?StreamID=51410198&pl_auth=2e83b652202abf941f7793
# bda887d1f5&ht=30&pl_b=00D90C088654FA550A41CFEAA7477AC791&CG_ID=1369080&Segment=149773
Suggests:	gstreamer0.10-mms

# GSM audio decoder:
# http://samples.mplayerhq.hu/A-codecs/GSM/countdown.wmv
Suggests:	gstreamer0.10-gsm

# AAC audio decoder (most commonly used in .mp4 files):
# http://samples.mplayerhq.hu/A-codecs/AAC/ct_nero-heaac.mp4
Suggests:	gstreamer0.10-faad

# Contains important plugins such as AVI demuxer:
Suggests:	gstreamer0.10-plugins-good

# Contains, for example, an MP3 decoder:
# http://samples.mplayerhq.hu/FLV/flash8/mrandmrssmith_320x176_200.flv
Suggests:	gstreamer0.10-plugins-ugly

# Contains, for example, NUV demuxer, used in MythTV recordings:
# http://samples.mplayerhq.hu/nuv/mythtvexample.nuv
# CD Audio
Suggests:	gstreamer0.10-plugins-bad

# Lots of decoders, for example for Flash video and MPEG-2 TS (eg. DVB):
# http://samples.mplayerhq.hu/FLV/flash8/mrandmrssmith_320x176_200.flv
# http://samples.mplayerhq.hu/MPEG-VOB/transport/dishtest.ts
Suggests:	gstreamer0.10-ffmpeg

# FLAC audio decoder (popular lossless codec):
# Note that the below sample plays without working seeking even
# without this package.
# http://samples.mplayerhq.hu/flac/dilvie_-_the_dragonfly.flac
Suggests:	gstreamer0.10-flac

# Musepack audio decoder:
# http://samples.mplayerhq.hu/A-codecs/musepack/06%20-%20Kalifornia.mpc
Suggests:	gstreamer0.10-musepack


%description audio
Virtual package which installs the GStreamer 0.10 input plugins that
cover most of the audio-only usage cases. For playing videos see
%{name}.

This package can be suggested or required by software that uses
GStreamer to open audio files.

%files
%files audio

