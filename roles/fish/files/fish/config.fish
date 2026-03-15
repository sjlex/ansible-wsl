# Load initial config
source $__fish_config_dir/init.fish

set -x PATH "$HOME/.local/bin" $PATH

if status is-interactive
  # Commands to run in interactive sessions can go here
end
