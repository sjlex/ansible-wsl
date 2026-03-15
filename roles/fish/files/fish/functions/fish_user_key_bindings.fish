function fish_user_key_bindings
  # ls
  bind \el 'user_list_current_token'

  # ctrl+shift+f
  bind \e\[70\;5\;6\~ 'echo "Ctrl+Shift+F"'

  # ctrl+g
  bind \cg '__fzf_find_file'
  # ctrl+shift+g
  bind \e\[71\;5\;6\~ '__fzf_cd --hidden'

  # ctrl+r
  bind \cr '__fzf_reverse_isearch'
  # ctrl+shift+r
  bind \e\[72\;5\;6\~ 'user_fzf_select_z'

  # ctrl+delete
  bind \e\[3\;5~ kill-word
  # ctrl+backspace
  bind \b backward-kill-word

  bind \ce 'br .'

  # bind \e\[1\;3B "prevd; commandline -f repaint"
  # bind \e\[1\;3A "nextd; commandline -f repaint"

end
