// Define tree data structure and functions
class TreeNode {
    constructor(key) {
        this.left = null;
        this.right = null;
        this.key = key;
    }
}

function insert(root, key) {
    if (root === null) {
        return new TreeNode(key);
    } else {
        if (root.key < key) {
            root.right = insert(root.right, key);
        } else {
            root.left = insert(root.left, key);
        }
    }
    return root;
}

function treeData(root) {
    if (root === null) {
        return null;
    }
    return {
        name: root.key.toString(),
        children: [treeData(root.left), treeData(root.right)].filter(Boolean)
    };
}

// Initial tree
let root = new TreeNode(50);
let keys = [30, 70, 20, 40, 60, 80];
keys.forEach(key => insert(root, key));

// Create SVG and group elements
const svg = d3.select("svg");
const width = +svg.attr("width");
const height = +svg.attr("height");

const g = svg.append("g")
    .attr("transform", "translate(40,0)");

const tree = d3.tree().size([height, width - 160]);
const stratify = d3.stratify().parentId(d => d.id);

function update(root) {
    const nodes = d3.hierarchy(treeData(root));
    const links = tree(nodes).links();

    // Nodes
    const node = g.selectAll(".node")
        .data(nodes.descendants(), d => d.data.name);

    const nodeEnter = node.enter().append("g")
        .attr("class", "node")
        .attr("transform", d => `translate(${d.y},${d.x})`);

    nodeEnter.append("circle")
        .attr("r", 10);

    nodeEnter.append("text")
        .attr("dy", 3)
        .attr("x", d => d.children ? -12 : 12)
        .style("text-anchor", d => d.children ? "end" : "start")
        .text(d => d.data.name);

    node.exit().remove();

    // Links
    const link = g.selectAll(".link")
        .data(links, d => d.target.data.name);

    link.enter().insert("path", "g")
        .attr("class", "link")
        .attr("d", d3.linkHorizontal()
            .x(d => d.y)
            .y(d => d.x));

    link.exit().remove();
}

// Initial render
update(root);

// Add new nodes periodically
setInterval(() => {
    const newKey = Math.floor(Math.random() * 90) + 10;
    insert(root, newKey);
    update(root);
}, 1000);
