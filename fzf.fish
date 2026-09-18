set -l color00 '#F4F6F8'
set -l color01 '#B86B73'
set -l color02 '#668C77'
set -l color03 '#A98955'
set -l color04 '#466E92'
set -l color05 '#897A98'
set -l color06 '#638E99'
set -l color07 '#486174'
set -l color08 '#5F717D'

set -l non_color_opts
for arg in (string split ' ' -- $FZF_DEFAULT_OPTS)
    if not string match -q -- '--color*' $arg
        set -a non_color_opts $arg
    end
end

set -Ux FZF_DEFAULT_OPTS "$non_color_opts --color=bg+:$color00,bg:$color00,spinner:$color06,hl:$color04 --color=fg:$color07,header:$color04,info:$color02,pointer:$color06 --color=marker:$color06,fg+:$color07,prompt:$color02,hl+:$color04"
