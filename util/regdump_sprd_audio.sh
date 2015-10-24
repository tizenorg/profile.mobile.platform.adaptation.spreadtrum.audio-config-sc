#!/bin/sh
#--------------------------------------
#  sprd_audio regdump
#--------------------------------------

filename=/root/dump_audio_reg.txt
if [ "$1" ]
then
sprd_debug=$1/sprd_audio
mkdir -p ${sprd_debug}
filename=${sprd_debug}/dump_audio_reg.txt
fi

#echo "save to " $filename
#echo -e "#sprd-codec bias_level" > $filename
#cat /sys/kernel/debug/asoc/sprdphone/sprd-codec.32/dapm/bias_level >> $filename
#echo -e "\n\n" >> $filename

echo -e "#sprd-codec dapm widget status" > $filename
#searchdir=/sys/kernel/debug/asoc/sprdphone/sprd-codec.32/dapm
searchdir=`find /sys/kernel/debug/asoc/sprdphone -name sprd-codec.*`
searchdir=$searchdir/dapm
for entry in $searchdir/*
do
	echo -e "[""$entry""]" >> $filename
	cat "$entry" >> $filename
done
echo -e "\n\n" >> $filename

echo -e "#sprd-codec register" >> $filename
cat /proc/asound/sprdphone/sprd-codec >> $filename
echo -e "\n\n" >> $filename
echo -e "#vbc register" >> $filename
cat /proc/asound/sprdphone/vbc >> $filename
