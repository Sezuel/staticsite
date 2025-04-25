from textnode import *

def split_nodes(old_nodes,delimiter,text_type):
    new_nodes = []
    for node in old_nodes:
        if delimiter in node.text:
            current_index = node.text.index(delimiter)
            new_nodes.append(TextNode(node.text[:current_index],text_type))
            end_index = node.text.find(delimiter,node.text.find(delimiter)+len(delimiter))
            if delimiter == '**':
                new_nodes.append(TextNode(node.text[current_index+1:end_index],TextType.BOLD))
            elif delimiter == '*':
                new_nodes.append(TextNode(node.text[current_index+1:end_index],TextType.ITALIC))
            elif delimiter == '`':
                new_nodes.append(TextNode(node.text[current_index+1:end_index],TextType.CODE))
            new_nodes.append(TextNode(node.text[end_index+1:],text_type))
    return new_nodes