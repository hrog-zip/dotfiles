# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

import os
import subprocess

mod = "mod4"
terminal = guess_terminal()
browser = "firefox"

def cmd_increase_margin(self):
   self.margin += 10
   self.group.layout_all()

def cmd_decrease_margin(self):
   new_margin = self.margin - 10
   if new_margin < 0:
        new_margin = 0

   self.margin = new_margin
   self.group.layout_all()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    Key([mod, "control"], "k", lazy.layout.grow()),
    Key([mod, "control"], "j", lazy.layout.shrink()),
    Key([mod], "space", lazy.window.toggle_floating()),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "Return", lazy.spawn(f"qtile run-cmd -f {terminal}"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control", "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "w", lazy.to_screen(1)),
    Key([mod], "e", lazy.to_screen(0)),

    Key([mod], "s", lazy.spawn(browser)),    
    Key([mod, "shift"], "s", lazy.spawn(f"{browser} -private-window")),    
    Key([mod], "d", lazy.spawn("rofi -modi 'drun' -show drun")),    

    Key([mod], "z", lazy.spawn("pavucontrol")),
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([mod], "p", lazy.spawn(f"{terminal} -e" + os.path.expanduser('~/bin/pkginstall'))), 
    Key([mod], "g", lazy.spawn("rofi -modi 'emoji' -show emoji")),
    Key([mod], "t", lazy.spawn("io.github.kotatogram")),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            #Key(
            #    [mod, "shift"],
            #    i.name,
            #    lazy.window.togroup(i.name, switch_group=True),
            #    desc="Switch to & move focused window to group {}".format(i.name),
            #),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name))
        ]
    )

layout_style = {"border_focus": "#ffbd00",
                "border_width": 1,
                "margin": 10,}

floating_layout_style = {"border_focus": "#ff4545",
                         "border_width": 1,}

layouts = [
    #layout.Columns(**layout_style),
    layout.MonadTall(**layout_style),
    layout.Max(),
    #layout.Floating(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

colors = ["#2a3241e5",
          "#7a7a7a",
          "#000000",
          "#ffbd00",
          "#524e39", 
          "#857856",
          "#1D5180",
          "#ff4545",]

def get_widgets():
    return [
                widget.GroupBox(fontsize = 14,
                                margin_y = 3,
                                margin_x = 0,
                                padding_y = 5,
                                padding_x = 5,
                                active = "#ffffff",
                                inactive = colors[1],
                                borderwidth=5,
                                rounded = False, 
                                highlight_color = colors[2], 
                                highlight_method = "block",
                                this_current_screen_border = colors[3],
                                this_screen_border = colors[4],
                                other_current_screen_border = colors[3],
                                other_screen_border = colors[4],
                                foreground = "#ffffff"),

                widget.Sep(margin = 5,
                           padding = 5,
                           ),
                
                widget.CurrentLayout(#foreground = colors[7],
                                     foreground = colors[1],
                                     padding = 7,
                                     fontsize = 14,
                                     ),
                widget.Spacer(),
                widget.WindowName(foreground = "#ffffff",
                                  margin=None, 
                                  width=bar.CALCULATED),
                widget.Spacer(),
                widget.Systray(background = colors[0]),
                widget.Clock(format = "%Y-%m-%d %H:%M:%S",
                             foreground = colors[1],
                             fontsize = 15,),
                # widget.QuickExit(),
            ]

screens = [
    Screen(top=bar.Bar(
               get_widgets(),
               28,
               background=colors[0],
               )
),  Screen(top=bar.Bar(
               get_widgets(),
               28,
               background=colors[0],
               )
),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    **floating_layout_style
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])


