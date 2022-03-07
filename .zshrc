HISTFILE=~/.zsh_history
HISTSIZE=100000
SAVEHIST=100000
setopt appendhistory

export ZSH_AUTOSUGGEST_STRATEGY=(history completion)
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh

export EDITOR=vim
export TERM=alacritty
# export BROWSER=firefox

source /home/arzt/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

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

export PF_INFO="ascii title os host kernel uptime pkgs shell wm de memory palette" 

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

export PATH="$HOME/bin:$PATH"

# figlet ARZT ARSCH | lolcat -S 60
function stierlitz { shuf -n 1 .stierlitz | lolcat -F 0.05; }
pfetch

stierlitz
# neofetch
