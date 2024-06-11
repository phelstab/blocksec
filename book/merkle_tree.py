import hashlib
from IPython.display import display, HTML
from merkly import MerkleTree

class MerkleTreeVisualizer:
    def __init__(self, data_list):
        self.data_list = data_list
        self.tree = MerkleTree(hash_function=hashlib.sha256)
        for data in data_list:
            self.tree.add_leaf(data.encode())
        self.tree.make_tree()

    def visualize(self):
        def hash_short(hash_value):
            return hash_value.hex()[:8] + '...'

        def node_html(node, level=0):
            if node is None:
                return ''
            left_html = node_html(node.left, level + 1)
            right_html = node_html(node.right, level + 1)
            node_data = f'<p>Hash: {hash_short(node.value)}</p>'
            node_html = f'<div style="display: inline-block; border: 1px solid black; padding: 10px; margin: 5px;">{node_data}</div>'
            if left_html or right_html:
                node_html += f'<div style="display: flex; justify-content: space-around;">{left_html}{right_html}</div>'
            return node_html

        root = self.tree.get_root()
        html = '<div style="font-family: monospace;">'
        html += node_html(root)
        html += '</div>'
        display(HTML(html))

