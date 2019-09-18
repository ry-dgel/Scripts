#!/bin/bash
if ! tmux has-session -t py 2>/dev/null; then
    tmux new-session -s py -d '/home/ry/.miniconda3/envs/default/bin/ipython'
fi
tmux detach-client -s py
tmux attach-session -t py
tmux set-option status
