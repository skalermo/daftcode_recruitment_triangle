use std::borrow::{Borrow, BorrowMut};
use std::fmt::Debug;
use std::slice::IterMut;

#[derive(Debug)]
pub struct TriangleTree<T> {
    nodes: Vec<Node<T>>,
    pub height: u32,
}

#[derive(Debug)]
#[derive(Copy, Clone)]
pub struct Node<T> {
    pub id: NodeId,
    pub prev: Option<NodeId>,
    pub next_on_path: Option<NodeId>,

    left_child: Option<NodeId>,
    right_child: Option<NodeId>,

    pub height: u32,
    pub data: T,
}

#[derive(Debug)]
#[derive(Copy, Clone, Hash, Eq, PartialOrd, PartialEq)]
pub struct NodeId {
    pub index: usize,
}

#[derive(Debug)]
#[derive(Clone, Copy)]
pub struct ValueSet {
    pub val: u8,
    pub heuristic_val: u32,
    pub cum_val: u32,
}

impl<T> TriangleTree<T> {
    pub fn new() -> Self {
        TriangleTree { nodes: Vec::new(), height: 0 }
    }
    pub fn new_node(&mut self, data: T) -> NodeId {
        // Get the next free index
        let next_index = self.nodes.len();

        // Push the node into the arena
        self.nodes.push(Node {
            id: NodeId { index: next_index },
            prev: None,
            next_on_path: None,
            left_child: None,
            right_child: None,
            height: self.height,
            data,
        });

        // Return the node identifier
        NodeId { index: next_index }
    }

    pub fn link_as_left_child_parent(&mut self, left_child: NodeId, parent: NodeId) {
        self.nodes[parent.index].left_child = Some(left_child);
    }

    pub fn link_as_right_child_parent(&mut self, right_child: NodeId, parent: NodeId) {
        self.nodes[parent.index].right_child = Some(right_child);
    }

    pub fn get_node_by_id(&self, node_id: &NodeId) -> &Node<T> {
        self.nodes[node_id.index].borrow()
    }

    pub fn get_node_by_id_mut(&mut self, node_id: NodeId) -> &mut Node<T> {
        self.nodes[node_id.index].borrow_mut()
    }

    pub fn get_root(&self) -> NodeId {
        NodeId { index: 0 }
    }

    pub fn nodes_iter_mut(&mut self) -> IterMut<Node<T>> {
        self.nodes.iter_mut()
    }
}

impl TriangleTree<ValueSet> {
    pub fn add_leaves(&mut self, leaves: Vec<u8>) -> Vec<NodeId> {
        self.height += 1;
        let mut node_ids: Vec<NodeId> = Vec::new();

        for leaf in leaves.into_iter() {
            node_ids.push(self.new_node(ValueSet {val: leaf, cum_val: 1_000_000, heuristic_val: 0}));
        }
        node_ids
    }

    pub fn get_children_of(&mut self, parent: NodeId) -> Option<(NodeId, NodeId)> {
        let parent_node = self.nodes[parent.index].clone();
        match (parent_node.left_child, parent_node.right_child) {
            (Some(left), Some(right)) => {
                let mut left_node = self.nodes[left.index].borrow_mut();
                if left_node.data.cum_val > left_node.data.val as u32 + parent_node.data.cum_val {
                    left_node.data.cum_val = left_node.data.val as u32 + parent_node.data.cum_val;
                    left_node.prev = Some(parent);
                }
                let mut right_node = self.nodes[right.index].borrow_mut();
                if right_node.data.cum_val > right_node.data.val as u32 + parent_node.data.cum_val {
                    right_node.data.cum_val = right_node.data.val as u32 + parent_node.data.cum_val;
                    right_node.prev = Some(parent);
                }
                Some((left, right))
            },
            _ => None
        }
    }
}

