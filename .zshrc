HISTFILE=~/.zsh_history
HISTSIZE=100000
SAVEHIST=100000
setopt appendhistory

export PATH="$HOME/.poetry/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

export ZSH_AUTOSUGGEST_STRATEGY=(history completion)
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

fpath=($HOME/.zsh/zsh-completions $fpath)

source ~/.config/lf/lfcd

function lfcd_bind() { lfcd; zle reset-prompt; zle redisplay}
zle -N lfcd_bind
bindkey '^o' lfcd_bind

update_prompt() {
    local CMD_EXIT_CODE=$?
    # PROMPT=$'%F{#313b40}[%F{yellow}%n%F{#313b40}@%F{#c94f55}%m%f%F{#313b40}]%f %F{red}%B%~%b%f $ '
    PROMPT='%F{#313b40}[%f%F{red}%B%~%b%f%F{#313b40}]%f %F{yellow}$%f '
	[[ -n ${SSH_CONNECTION-}${SSH_CLIENT-}${SSH_TTY-} ]] && PROMPT='%F{green}(ssh)%f %F{#313b40}[%f%F{yellow}%n%F{#313b40}@%F{#c94f55}%m%f %F{red}%B%~%b%f%F{#313b40}]%f %F{yellow}$%f '
    
    if [ $CMD_EXIT_CODE != "0" ]; then
        RPROMPT="%F{#313b40}[%F{#c94f55}$CMD_EXIT_CODE%f%F{#313b40}]"
    else
        RPROMPT=""
    fi

    # echo
}

precmd() { update_prompt }

alias restartx='sudo systemctl restart display-manager'
alias s="/bin/ls"
alias ls='ls -Al --color=auto'
alias aura='sudo aura'
alias pacman='sudo pacman'
alias dotfilescfg="/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME"
alias rr="ranger"
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
# pfetch
# paleofetch | lolcat
# https://github.com/IchMageBaume/clolcat
paleofetch --recache | sed "s,\x1B\[[0-9;]*[a-zA-Z],,g" | clolcat -F 0.05

# stierlitz
# neofetch
