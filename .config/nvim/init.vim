set number
set relativenumber
set autoindent
set tabstop=4
set shiftwidth=4
set smarttab
set softtabstop=4
set pastetoggle=<F3>

call plug#begin()
Plug 'rrethy/vim-hexokinase', { 'do': 'make hexokinase' }
Plug 'navarasu/onedark.nvim'
Plug 'preservim/nerdtree'
Plug 'lambdalisue/suda.vim'
Plug 'gleich/monovibrant'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'sainnhe/gruvbox-material'
" Plug 'zchee/deoplete-jedi'
" Plug 'python-mode/python-mode'
call plug#end()

let g:Hexokinase_highlighters = [ 'backgroundfull' ]

set tgc
let g:gruvbox_material_background = 'hard'
let g:gruvbox_material_disable_italic_comment = '1'
let g:gruvbox_material_transparent_background = '0'
colorscheme gruvbox-material
" Open the existing NERDTree on each new tab.
autocmd BufWinEnter * if getcmdwintype() == '' | silent NERDTreeMirror | endif
let mapleader = " "
nnoremap <leader>n :NERDTreeToggle<CR>
nnoremap <Space> <NOP>

nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

nnoremap <A-=> 3<C-w><
nnoremap <A--> 3<C-w>>
nnoremap <A-.> 3<C-w>+
nnoremap <A-,> 3<C-w>-

tnoremap <Esc> <C-\><C-n>

nnoremap d "_d

" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

" set statusline+=%#warningmsg#
" set statusline+=%{SyntasticStatuslineFlag()}
" set statusline+=%*
" 
" let g:syntastic_always_populate_loc_list = 1
" let g:syntastic_auto_loc_list = 1
" let g:syntastic_check_on_open = 1
" let g:syntastic_check_on_wq = 0

" let g:pymode_lint = 1
" let g:pymode_lint_on_write = 1
" let g:pymode_lint_message = 1
" let g:pymode_lint_checkers = ['pyflakes', 'pep8']
" let g:pymode_lint_cwindow = 1
" let g:pymode_lint_signs = 1
" let g:pymode_syntax_all = 0
