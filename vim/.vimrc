set nocompatible
syntax enable
filetype plugin indent on
set background=dark

" indentation
set tabstop=4 shiftwidth=4 expandtab

" display
set number relativenumber
set scrolloff=5
set wildmenu

" search: case-insensitive unless a capital is typed, highlight as you go
set ignorecase smartcase
set incsearch hlsearch

" editing
set backspace=indent,eol,start
set mouse=a
set clipboard=unnamed
set hidden

" persistent undo
call mkdir(expand('~/.vim/undo'), 'p')
set undofile undodir=~/.vim/undo//

" double Esc clears search highlight
nnoremap <Esc><Esc> :nohlsearch<CR>
