#!/bin/bash
raspivid -o - -t 9999999 -w 800 -h 600 --hflip | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:22339}' :demux=h264

