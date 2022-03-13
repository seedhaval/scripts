#!/usr/bin/env python3
import pygraphviz as pgv
import re
import uuid
from pathlib import Path

fldr = Path('/home/dvs/scripts/mind_maps/')


def add_node(lbl, clr, G):
    nid = str(uuid.uuid4())
    G.add_node(nid)
    n = G.get_node(nid)
    n.attr['style'] = 'filled'
    n.attr['fillcolor'] = clr
    n.attr['label'] = lbl
    return nid


def process_file(fl):
    with open(fl, 'r') as f:
        data = f.read().strip().splitlines()

    G = pgv.AGraph(directed=True, rankdir='LR')
    clr = ['#d7191c', '#fdae61', '#ffffbf', '#abd9e9', '#2c7bb6']
    root_nid = add_node(data[0], clr[0], G)
    stack = [root_nid]*5

    for ln in data[1:]:
        c_idx = len(re.findall(r'^\s*', ln)[0])//3
        lbl = ln.strip()
        p_idx = c_idx - 1
        c_nid = add_node(lbl, clr[c_idx], G)
        stack[c_idx] = c_nid
        G.add_edge(stack[p_idx], c_nid)

    G.layout(prog='sfdp')
    G.draw(str(fl).replace('.txt', '.svg'))


for fl in fldr.rglob('*.txt'):
    process_file(fl)
