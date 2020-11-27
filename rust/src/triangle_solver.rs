use std::io::{BufRead, BufReader};
use std::fs::File;

use crate::tree::{NodeId, TriangleTree, ValueSet};
use std::borrow::{Borrow, BorrowMut};
use std::collections::HashSet;
use std::u32::MAX;

static MIN_VAL: u32 = 1;

pub fn solve(filename: &str) -> (u32, Vec<u8>) {
    let mut tree = build_tree_from_source(filename);
    calc_heuristic_values(tree.borrow_mut());
    let last_on_path = calc_cum_values(tree.borrow_mut());
    backtrack_and_set_path(tree.borrow_mut(), last_on_path);
    let (cost, path) = get_optimal_path(tree.borrow_mut());
    // println!("{} {:?}", cost, path);
    (cost, path)
}

fn build_tree_from_source(filename: &str) -> TriangleTree<ValueSet> {
    let mut tree = TriangleTree::new();

    let reader = BufReader::new(File::open(filename)
        .expect(format!("Cannot open {}", filename).as_str()));

    let mut old_leaves_ids: Vec<NodeId> = Vec::new();
    let mut new_leaves_ids: Vec<NodeId>;

    for line in reader.lines() {
        let num_row: Vec<u8> = line
            .unwrap()
            .split_whitespace()
            .into_iter()
            .map(|str_num| str_num.parse::<u8>().unwrap())
            .collect();

        new_leaves_ids = tree.add_leaves(num_row);
        if !old_leaves_ids.is_empty() {
            for i in 0..old_leaves_ids.len() {
                tree.link_as_left_child_parent(new_leaves_ids[i], old_leaves_ids[i]);
                tree.link_as_right_child_parent(new_leaves_ids[i+1], old_leaves_ids[i]);
            }
        }

        old_leaves_ids = new_leaves_ids;
    }
    tree
}

fn calc_heuristic_values(tree: &mut TriangleTree<ValueSet>) {
    let tree_height = tree.height;
    for node in tree.nodes_iter_mut() {
        node.data.heuristic_val = (tree_height - node.height) * MIN_VAL;
    }
}

fn calc_cum_values(tree: &mut TriangleTree<ValueSet>) -> NodeId {
    let mut current = tree.get_root();
    let mut root = tree.get_node_by_id_mut(current);
    root.data.cum_val = root.data.val as u32;

    let mut opened_nodes = HashSet::new();
    let mut closed_nodes: HashSet<NodeId> = HashSet::new();
    opened_nodes.insert(current);

    while tree.get_node_by_id(current.borrow()).height < tree.height {
        let tuple = tree.get_children_of(current).unwrap();

        let left = tuple.0;
        let right = tuple.1;

        if !closed_nodes.contains(left.borrow()) {
            opened_nodes.insert(left);
        }
        if !closed_nodes.contains(right.borrow()) {
            opened_nodes.insert(right);
        }
        opened_nodes.remove(current.borrow());

        let mut min_val = MAX;
        for (node_id, node) in opened_nodes
            .iter()
            .map(|id| (id, tree.get_node_by_id(id.borrow()))) {
            if min_val > node.data.cum_val + node.data.heuristic_val {
                min_val = node.data.cum_val + node.data.heuristic_val;
                current = node_id.clone();
            }
        }
        closed_nodes.insert(current);
    }
    current
}

fn backtrack_and_set_path(tree: &mut TriangleTree<ValueSet>, last_node_on_path: NodeId) {
    let mut cur_node = last_node_on_path;
    while let Some(prev_node) = tree.get_node_by_id(cur_node.borrow()).prev {
        tree.get_node_by_id_mut(prev_node).next_on_path = Some(cur_node);
        cur_node = prev_node;
    }
}

fn get_optimal_path(tree: &mut TriangleTree<ValueSet>) -> (u32, Vec<u8>) {
    let mut optimal_path = Vec::new();
    let mut cur = tree.get_root();
    optimal_path.push(tree.get_node_by_id(cur.borrow()).data.val);

    while let Some(next) = tree.get_node_by_id(cur.borrow()).next_on_path {
        optimal_path.push(tree.get_node_by_id(next.borrow()).data.val);
        cur = next;
    }
    // println!("{:?} {:?}", tree.get_node_by_id(cur.borrow()).data.cum_val, optimal_path);
    (tree.get_node_by_id(cur.borrow()).data.cum_val, optimal_path)
}
