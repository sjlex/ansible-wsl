function fish_user_key_bindings

  bind \ci complete

  # ls
  bind \el 'user_list_current_token'

  # ctrl+shift+f
  bind \e\[70\;5u 'br --cmd "//&cr//i"; commandline -f repaint'

  # ctrl+g
  bind \cg '__fzf_find_file'

  # ctrl+shift+g
  bind \e\[71\;5u '__fzf_cd --hidden'

  # ctrl+r
  bind \cr '__fzf_reverse_isearch'

  # ctrl+shift+r
  bind \e\[82\;5u 'user_fzf_select_z'

  # ctrl+delete
  bind \e\[3\;5~ kill-word
  # ctrl+backspace
  bind \b backward-kill-word

  # ctrl+e
  bind \ce 'br .; commandline -f repaint'

  # ctrl+h
  bind \ch 'cd ~; commandline -f repaint'

  # ctrl+shift+pageup
  bind \e\[5\;6~ 'cd ..; commandline -f repaint'

  # ctrl+shift+pagedown
  bind \e\[6\;6~ 'prevd; commandline -f repaint'

end
