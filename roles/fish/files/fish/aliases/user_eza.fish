if type -q eza
  alias ls "eza --color=auto --icons=never --group-directories-first"
  alias ll "ls -lghm --octal-permissions --smart-group"
  alias la "ll -a"
  alias lt "la -T"
  alias l "la"
end
