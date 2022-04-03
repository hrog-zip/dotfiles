# Terminate already running bar instances
killall -q polybar
# If all your bars have ipc enabled, you can also use 
# polybar-msg cmd quit

# Launch Polybar, using default config location ~/.config/polybar/config

# if type "xrandr"; then
#     for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
#         MONITOR=$m polybar --reload example &
#     done
# else
#     polybar --reload example &
# fi

polybar --reload mon0 &
polybar --reload mon1 &

echo "Polybar launched..."
