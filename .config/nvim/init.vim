set number
set relativenumber
set autoindent
set tabstop=4
set shiftwidth=4
set smarttab
set softtabstop=4
set pastetoggle=<F3>

call plug#begin()
Plug 'KabbAmine/yowish.vim'
Plug 'sonph/onehalf', { 'rtp': 'vim' }
Plug 'rrethy/vim-hexokinase', { 'do': 'make hexokinase' }
Plug 'navarasu/onedark.nvim'
Plug 'preservim/nerdtree'
Plug 'lambdalisue/suda.vim'
call plug#end()

let g:Hexokinase_highlighters = [ 'backgroundfull' ]

set tgc
colorscheme onedark
" Open the existing NERDTree on each new tab.
autocmd BufWinEnter * if getcmdwintype() == '' | silent NERDTreeMirror | endif
let mapleader = " "
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <Space> <NOP>
