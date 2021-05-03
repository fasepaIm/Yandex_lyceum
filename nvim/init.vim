"Edit
	set nowrap
	set tabstop=4
	set shiftwidth=4
	set noexpandtab
	set hidden
	set breakindent
	set breakindentopt=shift:2
	set nospell
	" let g:polyglot_disabled = ['stylus']
	set noswapfile
"UI
	set updatetime=300
	set shortmess+=c
	set signcolumn=yes

	set scrolloff=5
	set ignorecase
	set mouse=a
	set splitbelow
	set splitright
	set laststatus=2
	set noshowmode
	" set listchars=eol:¬,tab:>-,trail:~,extends:>,precedes:<,space:·
	set listchars+=tab:\│\ 
	" set listchars+=space:·
	set list
	syntax on
	set synmaxcol=196
	set number relativenumber
	:augroup numbertoggle
	: autocmd!
	: autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
	: autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
	:augroup END
filetype plugin indent on

" :augroup numbertoggle
" : autocmd!
" : autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
" : autocmd BufLeave,FocusLost,InsertEnter * set norelativenumber
" :augroup END

"Buttplugs
	call plug#begin('~/.config/nvim/plugged')

"UI
	Plug 'justinmk/vim-sneak'
	Plug 'vim-airline/vim-airline'

"Writing tools
	Plug 'sheerun/vim-polyglot'
	" Plug 'iloginow/vim-stylus'
	Plug 'Yggdroot/indentLine'
	Plug 'tpope/vim-sleuth'
	Plug 'tomtom/tcomment_vim'
	Plug 'kopischke/vim-fetch'
	Plug 'tmsvg/pear-tree'
	Plug 'neoclide/coc.nvim', {'branch': 'release'}
	Plug 'scrooloose/nerdtree'
	Plug 'jistr/vim-nerdtree-tabs'
	Plug 'xuyuanp/nerdtree-git-plugin'
	Plug 'editorconfig/editorconfig-vim'
	Plug 'nathanaelkane/vim-indent-guides'
	Plug 'tpope/vim-fugitive'
	Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --no-bash' }
	Plug 'junegunn/fzf.vim'

"Colorchemes
	Plug 'morhetz/gruvbox'
	Plug 'ayu-theme/ayu-vim' " or other package manager
	Plug 'drewtempelmeyer/palenight.vim'
	Plug 'rakr/vim-one'

call plug#end()

set background=dark
colorscheme palenight
let g:EditorConfig_max_line_indicator = "none"

"ayu theme setting
" set termguicolors     " enable true colors support
" let ayucolor="light"  " for light version of theme
" let ayucolor="mirage" " for mirage version of theme
" let ayucolor="dark"   " for dark version of theme

"PLENIGHT_THEME_SETTING
if (has("nvim"))
  let $NVIM_TUI_ENABLE_TRUE_COLOR=1
endif

if (has("termguicolors"))
  set termguicolors
endif

let g:lightline = { 'colorscheme': 'palenight' }
let g:airline_theme = "palenight"

"ITALIC_COMMENT_STYLE_FOR_THEMES
let g:palenight_terminal_italics=1

"SETTING_SPACE_FOR_SPACE
let g:indentLine_char = '│'
let g:indentLine_faster = 1
let g:indentLine_color_term = 0
" let g:indentLine_color_gui = 0
let g:indentLine_color_tty_light = 0
let g:indentLine_color_dark = 0
let g:indentLine_bufNameExclude = ["term:.*"]

"SCRIPT_FOR_PRETTY
let g:pretty_indent_namespace = nvim_create_namespace('pretty_indent')
function! PrettyIndent()
	let l:view=winsaveview()
	call cursor(1, 1)
	call nvim_buf_clear_namespace(0, g:pretty_indent_namespace, 1, -1)
	while 1
		let l:match = search('^$', 'W')
		if l:match ==# 0
			break
		endif
		let l:indent = cindent(l:match)
		if l:indent > 0
			call nvim_buf_set_virtual_text(
			\   0,
			\   g:pretty_indent_namespace,
			\   l:match - 1,
			\   [[repeat(repeat(' ', &shiftwidth - 1) . '│', l:indent / &shiftwidth - 1), 'IndentGuide']],
			\   {}
			\)
		endif
	endwhile
	call winrestview(l:view)
endfunction

augroup PrettyIndent
 autocmd!
 autocmd TextChanged * call PrettyIndent()
 autocmd BufEnter * call PrettyIndent()
 autocmd InsertLeave * call PrettyIndent()
augroup END

" hi EndOfBuffer ctermfg=bg guifg=bg
" 	hi Comment cterm=italic
" 	hi VertSplit ctermbg=bg
"Maps
	let mapleader = " "
	nnoremap <CR> :
	nnoremap <silent> <Esc> :noh<CR>:set nopaste<CR><Esc>

" for fzf plugin
let $FZF_DEFAULT_COMMAND = 'fd --type f --color=never'
" Support russian layout
" set keymap=russian-jcukenwin
set langmap=ФИСВУАПРШОЛДЬТЩЗЙКЫЕГМЦЧНЯ;ABCDEFGHIJKLMNOPQRSTUVWXYZ
set langmap+=фисвуапршолдьтщзйкыегмцчня;abcdefghijklmnopqrstuvwxyz

"Bindings
	let mapleader = " "
	map <leader>f :NERDTreeToggle<CR>
function! NERDTreeRefresh()
	if &filetype == "nerdtree"
		silent exe substitute(mapcheck("R"), "<CR>", "", "")
	endif
endfunction

autocmd BufEnter * call NERDTreeRefresh()

"Complete
	inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
	inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"



" NERDTress File highlighting
function! NERDTreeHighlightFile(extension, fg, bg, guifg, guibg)
 exec 'autocmd filetype nerdtree highlight ' . a:extension .' ctermbg='. a:bg .' ctermfg='. a:fg .' guibg='. a:guibg .' guifg='. a:guifg
 exec 'autocmd filetype nerdtree syn match ' . a:extension .' #^\s\+.*'. a:extension .'$#'
endfunction

" call NERDTreeHighlightFile('jade', 'green', 'none', 'green', '#151515')
" call NERDTreeHighlightFile('ini', 'yellow', 'none', 'yellow', '#151515')
" call NERDTreeHighlightFile('md', 'blue', 'none', '#3366FF', '#151515')
" call NERDTreeHighlightFile('yml', 'yellow', 'none', 'yellow', '#151515')
" call NERDTreeHighlightFile('config', 'yellow', 'none', 'yellow', '#151515')
" call NERDTreeHighlightFile('conf', 'yellow', 'none', 'yellow', '#151515')
" call NERDTreeHighlightFile('json', 'yellow', 'none', 'yellow', '#151515')
" call NERDTreeHighlightFile('html', 'yellow', 'none', 'yellow', '#151515')
" call NERDTreeHighlightFile('styl', 'cyan', 'none', 'cyan', '#151515')
" call NERDTreeHighlightFile('css', 'cyan', 'none', 'cyan', '#151515')
" call NERDTreeHighlightFile('coffee', 'Red', 'none', 'red', '#151515')
" call NERDTreeHighlightFile('js', 'Red', 'none', '#ffa500', '#151515')
" call NERDTreeHighlightFile('php', 'red', 'none', '#ff00ff', '#151515')
" call NERDTreeHighlightFile('py', 'yellow', 'none', 'yellow', '#151515')


"Other
	nnoremap <leader>t :t.<CR>
	nnoremap tt :t.<CR>
	nnoremap <leader>/ :TComment<CR>
	nnoremap <CR> :
	nnoremap K i<CR><Esc>
	nnoremap J kJ<Esc>

	nnoremap <a-w> :close<CR>
	nnoremap <a-d> :vsplit<CR>
	nnoremap <a-D> :split<CR>
	nnoremap <a-h> <c-w>h
	nnoremap <a-j> <c-w>j
	nnoremap <a-k> <c-w>k
	nnoremap <a-l> <c-w>l

	nnoremap <leader>w :close<CR>
	nnoremap <leader>q :bw<CR>
	nnoremap <leader>Q :bw!<CR>
	nnoremap <leader>d :vsplit<CR>
	nnoremap <leader>D :split<CR>
	nnoremap <leader>s :split<CR>
	nnoremap <leader>h <c-w>h
	nnoremap <leader>j <c-w>j
	nnoremap <leader>k <c-w>k
	nnoremap <leader>l <c-w>l
	nnoremap <c-p> :CocList files<CR>
	nnoremap <a-P> :CocList mru<CR>
	nnoremap <a-f> :CocList folders<CR>
	nnoremap <a-E> :CocList extensions<CR>

	vnoremap <a-c> "+y
	vnoremap <a-v> c"+p
	nnoremap <a-v> "+p
	nnoremap <a-V> "+P

	vnoremap <leader>c "+y
	vnoremap <leader>v c"+p
	nnoremap <leader>v "+p
	nnoremap <leader>V "+P

	nmap gL :Rg<CR>

"Prevent exit
	nnoremap <c-z> <esc>

" Jump forward fix
	nnoremap <c-i> <c-i>

	" autocmd vimenter * NERDTreeToggle
