HISTFILE=~/.zsh_history
HISTSIZE=100000
SAVEHIST=100000
setopt appendhistory

export ZSH_AUTOSUGGEST_STRATEGY=(history completion)
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Check for virtualenvwrapper
if type workon >/dev/null 2>&1; then
  VENV_WRAPPER=true
else
  VENV_WRAPPER=false
fi

function _virtualenv_auto_activate() {
    if [ -e ".venv" ]; then
        # Check for symlink pointing to virtualenv
        if [ -L ".venv" ]; then
          _VENV_PATH=$(readlink .venv)
          _VENV_WRAPPER_ACTIVATE=false
        # Check for directory containing virtualenv
        elif [ -d ".venv" ]; then
          _VENV_PATH=$(pwd -P)/.venv
          _VENV_WRAPPER_ACTIVATE=false
        # Check for file containing name of virtualenv
        elif [ -f ".venv" -a $VENV_WRAPPER = "true" ]; then
          _VENV_PATH=$WORKON_HOME/$(cat .venv)
          _VENV_WRAPPER_ACTIVATE=true
        else
          return
        fi

        # Check to see if already activated to avoid redundant activating
        if [ "$VIRTUAL_ENV" != $_VENV_PATH ]; then
            if $_VENV_WRAPPER_ACTIVATE; then
              _VENV_NAME=$(basename $_VENV_PATH)
              workon $_VENV_NAME
            else
              _VENV_NAME=$(basename `pwd`)
              VIRTUAL_ENV_DISABLE_PROMPT=1
              source .venv/bin/activate
              _OLD_VIRTUAL_PS1="$PS1"
              PS1="($_VENV_NAME)$PS1"
              export PS1
            fi
            echo Activated virtualenv \"$_VENV_NAME\".
        fi
    fi
}

export PROMPT_COMMAND=_virtualenv_auto_activate
if [ -n "$ZSH_VERSION" ]; then
  function chpwd() {
    _virtualenv_auto_activate
  }
fi

source ~/.config/lf/lfcd

bindkey -s '^o' '^llfcd\r'

update_prompt() {
    local CMD_EXIT_CODE=$?
    PROMPT=$'%F{#313b40}[%F{yellow}%n%F{#313b40}@%F{#c94f55}%m%f%F{#313b40}]%f %F{red}%B%~%b%f \n$ '
    
    if [ $CMD_EXIT_CODE != "0" ]; then
        RPROMPT="%F{#313b40}[%F{#c94f55}$CMD_EXIT_CODE%f%F{#313b40}]"
    else
        RPROMPT=""
    fi

    echo
}

precmd() { update_prompt }

alias restartx='sudo systemctl restart display-manager'
alias s="/bin/ls"
alias ls='ls -Al --color=auto'
alias aura='sudo aura'
alias pacman='sudo pacman'
alias dotfilescfg="/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME"
alias rr="ranger"
alias ss="sudo !!"
alias n="nvim"
alias cfgq="nvim ~/.config/qtile/config.py"
alias cfgzsh="nvim ~/.zshrc"
alias cfgx="nvim ~/.xprofile"
alias cfgn="nvim ~/.config/nvim/init.vim"
alias cfgsxhkd="nvim .config/sxhkd/sxhkdrc"
alias cfglf="nvim ~/.config/lf/lfrc"
alias cfgp="nvim ~/.config/picom/picom.conf"
alias cfgt="nvim ~/.config/tmux/tmux.conf"

# cat ~/.cache/wal/sequences

# figlet ARZT ARSCH | lolcat -S 60
function stierlitz { shuf -n 1 .stierlitz | lolcat -F 0.05; }
pfetch

# stierlitz
# neofetch

export PATH="$HOME/.poetry/bin:$PATH"
