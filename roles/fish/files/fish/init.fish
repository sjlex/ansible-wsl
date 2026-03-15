# Load system-wide profile
for profile in /etc/profile.d/*.fish
  source $profile
end

# Load environment variables
source $__fish_config_dir/env.fish

# Load aliases
for alias in $__fish_config_dir/aliases/**/*
  source $alias
end
