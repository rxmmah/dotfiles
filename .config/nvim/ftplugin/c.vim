nnoremap <buffer> <LocalLeader>c :w<CR>:!clang % -o %<.out<CR>

nnoremap <buffer> <LocalLeader>r :w<CR>:split \| execute 'terminal ./%:r.out'<CR>



