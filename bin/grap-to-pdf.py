#!/usr/bin/env python3
import pygraphviz as pgv
import re
import uuid
from pathlib import Path
import os

fldr = Path('/home/dvs/scripts/mind_maps/')


def add_node(lbl,  G):
    nid = str(uuid.uuid4())
    G.add_node(nid)
    n = G.get_node(nid)
    n.attr['label'] = lbl.replace('\\','\\\\')
    return nid


def process_file(fl):
    with open(fl, 'r') as f:
        data = f.read().strip().splitlines()

    G = pgv.AGraph(directed=True, rankdir='LR')

    root_nid = add_node(data[0],  G)
    stack = [root_nid]*10

    for ln in data[1:]:
        c_idx = len(re.findall(r'^\s*', ln)[0])//4
        lbl = ln.strip()
        p_idx = c_idx - 1
        c_nid = add_node(lbl,  G)
        stack[c_idx] = c_nid
        G.add_edge(stack[p_idx], c_nid)

    tgt_pth = '/mnt/c/Users/Dell/Desktop/google_drive_bkp/' + \
        str(fl.parents[0]).replace('/home/dvs/scripts/', '') + '/'
    if not os.path.exists(tgt_pth):
        os.makedirs(tgt_pth)

    G.layout(prog='dot')
    G.draw(tgt_pth + fl.name.replace('.txt', '.pdf'))


for fl in fldr.rglob('*.txt'):
    process_file(fl)
