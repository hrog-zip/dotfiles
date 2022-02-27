#!/bin/sh
# picom --experimental-backends -b
pgrep -x sxhkd > /dev/null || sxhkd &
