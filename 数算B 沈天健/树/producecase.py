import random
from samplecode import parse_tree, preorder_traversal, inorder_traversal

# 生成树的字符串表示形式
def generate_tree_string():
    # 随机生成树的结构
    def generate_tree():
        if random.random() < 0.6:  # 60% 的概率生成子树
            left_subtree = generate_tree()
            right_subtree = generate_tree()
            return f"(X{left_subtree},{right_subtree})"
        else:  # 40% 的概率生成叶子节点
            return random.choice("ABCDEFGHIJ*")

    # 生成树的字符串
    tree_string = generate_tree()
    return tree_string


# 生成输入和输出文件
for i in range(20):
    input_filename = f"data/{i}.in"
    output_filename = f"data/{i}.out"

    # 生成树的字符串
    tree_string = generate_tree_string()

    # 将树的字符串写入输入文件
    with open(input_filename, "w") as input_file:
        input_file.write(tree_string)

    # 解析树，并计算先序遍历和中序遍历
    tree = parse_tree(tree_string)
    preorder = preorder_traversal(tree)
    inorder = inorder_traversal(tree)

    # 将先序遍历和中序遍历写入输出文件
    with open(output_filename, "w") as output_file:
        output_file.write(preorder + "\n")
        output_file.write(inorder + "\n")