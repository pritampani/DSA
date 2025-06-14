#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node *left;
    struct node *right;
};

struct node *newNode(int value) {
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->value = value;
    temp->left = temp->right = NULL;
    return temp;
}

struct node *insertNode(struct node *node, int value) {
    if (node == NULL) {
        return newNode(value);
    }
    if (value < node->value) {
        node->left = insertNode(node->left, value);
    } else if (value > node->value) {
        node->right = insertNode(node->right, value);
    }
    return node;
}

//inorder(left->root->right)
void inorder(struct node *root)
{
    if (root!=NULL){
        inorder(root->left);
        printf("%d ->",root->value);
        inorder(root->right);
    }
}




void printTree(struct node *root) {
    if (root!= NULL) {
        printTree(root->left);
        printf("%d-> ", root->value);
        printTree(root->right);
    }
}

int main() {
    struct node *root = NULL;

    root = insertNode(root, 50);
    root = insertNode(root, 30);
    root = insertNode(root, 20);
    root = insertNode(root, 40);
    //inorder(root);
    printTree(root);

    return 0;
}
