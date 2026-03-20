function fish_user_key_bindings
  # ls
  bind \el 'user_list_current_token'

  # ctrl+shift+f
  bind \e\[70\;6u 'br --cmd "//&cr//i"'

  # ctrl+g
  bind \cg '__fzf_find_file'

  # ctrl+shift+g
  bind \e\[71\;6u '__fzf_cd --hidden'

  # ctrl+r
  bind \cr '__fzf_reverse_isearch'

  # ctrl+shift+r
  bind \e\[82\;6u 'user_fzf_select_z'

  # ctrl+delete
  bind \e\[3\;5~ kill-word
  # ctrl+backspace
  bind \b backward-kill-word

  # ctrl+e
  bind \ce 'br .'

  # ctrl+h
  bind \ch 'cd ~; commandline -f repaint'

end
