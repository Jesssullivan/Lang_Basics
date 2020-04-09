#!/bin/bash
# recursively convert .heic to png
# by Jess Sullivan
#
# permiss:
# sudo chmod u+x heic_png.sh
#
# installs heif-convert via ppa:
# sudo ./heic_png.sh
#
# run as $USER:
# ./heic_png.sh



command -v heif-convert >/dev/null || {

  echo >&2 -e "heif-convert not intalled! \nattempting to add ppa....";

  if [[ $EUID -ne 0 ]]; then
     echo "sudo is required to install, aborting."
     exit 1
  fi

  add-apt-repository ppa:strukturag/libheif
  apt-get install libheif-examples -y
  apt-get update -y

  exit 0

  }

# default behavior:

for fi in *.heic; do

  echo "converting file: $fi"

  heif-convert $fi $fi.png

  done
