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

    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),

    Key([mod, "control"], "k", lazy.layout.grow()),
    Key([mod, "control"], "j", lazy.layout.shrink()),
    Key([mod], "space", lazy.window.toggle_floating()),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control", "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "w", lazy.to_screen(1)),
    Key([mod], "e", lazy.to_screen(0)),

    Key([mod], "f", lazy.window.toggle_fullscreen()),
]
# groups = [Group(i) for i in "1234567890"]
groups = [Group("web", layout="max", label=""),
          Group("2mon", label="", matches=[Match(wm_class=["kotatogram-desktop", "discord", "keepassxc"])], layout="max"),
          Group("term", label=""),
          Group("gl", label="", matches=[Match(wm_class=["UltimMC", "Steam"])]),
          # This dsent really work because Minecraft window named something like "Minecraft* 1.18.1"
          # I think its possible to get all windows that contains Minecraft in the name to match group
          # However i dont know how
          Group("game", label="", matches=[Match(wm_class=["Minecraft"])]),
          Group("main", label="", matches=[Match(wm_class=["thunar"])]),
          Group("obs", label="", matches=[Match(wm_class=["obs"])])]

from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

# for i in groups:
#     keys.extend(
#         [
#             # mod1 + letter of group = switch to group
#             Key(
#                 [mod],
#                 groups.index(i),
#                 lazy.group[i.name].toscreen(),
#             ),
#             # mod1 + shift + letter of group = switch to & move focused window to group
#             #Key(
#             #    [mod, "shift"],
#             #    i.name,
#             #    lazy.window.togroup(i.name, switch_group=True),
#             #    desc="Switch to & move focused window to group {}".format(i.name),
#             #),
#             # Or, use below if you prefer not to switch to that group.
#             # # mod1 + shift + letter of group = move focused window to group
#             Key([mod, "shift"], groups.index(i), lazy.window.togroup(i.name),
#                 desc="move focused window to group {}".format(i.name))
#         ]
#     )

layout_style = {"border_focus": "#ffbd00",
                "border_width": 2,
                "margin": 3,}

floating_layout_style = {"border_focus": "#ff4545",
                         "border_width": 1,}

layouts = [
    #layout.Columns(**layout_style),
    # layout.MonadTall(**layout_style),
    #layout.Floating(),
    # layout.Stack(num_stacks=2),
    layout.Bsp(**layout_style),
    layout.Max(),
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
colors = ["#2a3241",
          "#7a7a7a",
          "#000000",
          "#ffbd00",
          "#524e39", 
          "#857856",
          "#1D5180",
          "#f75040",
          "#5cf257",
          "#542b28",
          "#58c9f5",
          "#a678e3"]

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
                
                widget.Net(foreground=colors[10],
                           format="↓ {down} ↑ {up}",
                           use_bits=False),

                widget.Sep(margin = 5,
                           padding = 5,
                           ),

                widget.TextBox(text="", foreground=colors[7], fontsize=17),
                widget.CPUGraph(border_width=0,
                                line_width=3,
                                frequency=0.5,
                                graph_color=colors[7],
                                fill_color=colors[9]),
                
                widget.Sep(margin = 5,
                           padding = 5,
                           ),
                
                widget.TextBox(text="", foreground=colors[3], fontsize=13),
                widget.Memory(foreground=colors[3],
                              format="{MemUsed: .1f}{mm}  /  {MemTotal: .1f}{mm}",
                              measure_mem="G",
                              ),

                widget.Sep(margin = 5,
                           padding = 5,
                           ),

                # widget.CheckUpdates(),
                widget.DF(foreground=colors[8],
                          visible_on_warn=False,
                          update_interval=2,
                          format="  {f}{m} / {s}{m}  [{r:.0f}%]"
                          ),

                widget.Sep(margin = 5,
                           padding = 5,
                           ),

                widget.Clock(format = " %Y %b %a %H:%M:%S",
                             foreground = colors[11],
                             fontsize=14),
                # widget.QuickExit(),
            ]

screens = [
    Screen(top=bar.Bar(
           get_widgets(),
           24,
           background=colors[0],
           )),

    Screen(top=bar.Bar(
           get_widgets(),
           24,
           background=colors[0],
           )),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# dgroups_key_binder = None
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
wmname = "qtile"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])


