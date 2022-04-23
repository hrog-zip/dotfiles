set number
set relativenumber
set autoindent
set tabstop=4
set shiftwidth=4
set smarttab
set softtabstop=4
set pastetoggle=<F3>

set clipboard+=unnamedplus

call plug#begin()
Plug 'rrethy/vim-hexokinase', { 'do': 'make hexokinase' }
Plug 'navarasu/onedark.nvim'
Plug 'preservim/nerdtree'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'sainnhe/gruvbox-material'
Plug 'vimwiki/vimwiki'
Plug 'christoomey/vim-tmux-navigator'
Plug 'simrat39/symbols-outline.nvim'
Plug 'neovim/nvim-lspconfig'
Plug 'williamboman/nvim-lsp-installer'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'nvim-treesitter/nvim-treesitter'
Plug 'm-demare/hlargs.nvim'
Plug 'glacambre/firenvim'
Plug 'junegunn/goyo.vim'
Plug 'machakann/vim-sandwich'
Plug 'glepnir/dashboard-nvim'
call plug#end()

let g:Hexokinase_highlighters = [ 'backgroundfull' ]

set tgc
"let g:gruvbox_material_background = 'hard'
"let g:gruvbox_material_disable_italic_comment = '1'
"let g:gruvbox_material_transparent_background = '0'
"colorscheme gruvbox-material
colorscheme onedark

let mapleader = " "
nnoremap <leader>n :NERDTreeToggle<CR>
nnoremap <Space> <NOP>

let g:surround_prefix = 's'

nnoremap <A-=> 3<C-w><
nnoremap <A--> 3<C-w>>
nnoremap <A-.> 3<C-w>+
nnoremap <A-,> 3<C-w>-

tnoremap <Esc> <C-\><C-n>

nnoremap d "_d
" nnoremap x "_x
nnoremap c "_c

nnoremap gh 0
nnoremap gl $
vnoremap gh 0
vnoremap gl $

inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O

nnoremap <C-c> :Centerpad<CR>
nnoremap gs :nohlsearch<CR>
nnoremap <Leader>w :w<CR>
nnoremap <Leader>t <C-w>T

autocmd InsertEnter * norm zz
" remove trailing space on write
autocmd BufWritePre * :%s/\s\+$//e

" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

function Suedit()
  let fname=tempname()
  exec 'w' fname
  let writetarget=shellescape(expand("%:p"))
  let owner=shellescape(system('stat --printf=%U:%G ' . writetarget))
  let modes=system('stat --printf=c%a ' . writetarget)
  exec '!sudo cp' shellescape(fname) writetarget
  exec '!sudo chmod' modes writetarget
  exec '!sudo chown' owner writetarget
endfunction

lua <<EOF
local lsp_installer = require("nvim-lsp-installer")

-- Register a handler that will be called for each installed server when it's ready (i.e. when installation is finished
-- or if the server is already installed).
lsp_installer.on_server_ready(function(server)
    local opts = {}

    -- (optional) Customize the options passed to the server
    -- if server.name == "tsserver" then
    --     opts.root_dir = function() ... end
	-- end

    -- This setup() function will take the provided server configuration and decorate it with the necessary properties
    -- before passing it onwards to lspconfig.
    -- Refer to https://github.com/neovim/nvim-lspconfig/blob/master/doc/server_configurations.md
	-- opts.autostart = false
    server:setup(opts)
end)

vim.g.symbols_outline = {
	highlight_hovered_item = true,
    show_guides = true,
    auto_preview = true}

vim.diagnostic.disable()

local hlargs = require('hlargs')
hlargs.enable()
EOF
