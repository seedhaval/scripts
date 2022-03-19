"Highlight matches on search
set hlsearch

"Allow to move between files even with unsaved changes
set hidden

"normal mode mappings
nnoremap <f2> :w<cr>
nnoremap <f3> :ls<cr>:b
nnoremap <f4> :qa!<cr>

"insert mode mappings
"expand file name
inoremap <f3> <c-x><c-f>

"do not allow equals sign in file name. Useful with var=fl type scenarios
set isfname-==

"case insensitive all
set ignorecase
set fileignorecase

"allow serching without pressing enter
set incsearch

"show options when entering filenames in command mode
set wildmode=list:longest

"wrap text
set wrap

"allow undo after restart
"one time activity. Create undo dir
"mkdir -p ~/.vim/undo
set undofile
set undodir=~/.vim/undo
set undolevels=1000
set undoreload=10000

"allow using mouse
set mouse=a

"change tab to space for insert mode
inoremap <tab> <space><space><space><space>

"show line numbers
set number

"shift tab to minus 4 spaces
inoremap <S-tab> <c-o>3h
