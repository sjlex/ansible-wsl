# Fzf
set -U FZF_DISABLE_KEYBINDINGS 1

set -l c0 '--color=bg:-1,bg+:#e8e8e8,spinner:#24A8B4,hl:#DF5273'
set -l c1 '--color=bg:-1,bg+:#e8e8e8,spinner:#24A8B4,hl:#DF5273'
set -l c2 '--color=fg:#9DA0A2,header:#DF5273,info:#FFB987,pointer:#000000'
set -l c3 '--color=marker:#24A8B4,fg+:#000000,prompt:#EFB993,hl+:#DF5273'
set -l c4 '--color=fg+:regular,hl:bold,hl+:bold,pointer:bold,marker:bold'

set -U FZF_DEFAULT_OPTS $c0 $c1 $c2 $c3 $c4
