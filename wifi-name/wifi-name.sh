#!/usr/local/bin/bash


SSID=$(networksetup -listallhardwareports | awk '/Wi-Fi/{getline; print $2}' | xargs networksetup -getairportnetwork )
SSID=$(/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I  | awk -F' SSID: '  '/ SSID: / {print $2}' )

## SSID=$(
##     system_profiler SPAirPortDataType | awk -F':' '/Current Network Information:/ {
##     getline
##     sub(/^ */, "")
##     sub(/:$/, "")
##     print
##     }'
## )

echo "SSID is $SSID"
