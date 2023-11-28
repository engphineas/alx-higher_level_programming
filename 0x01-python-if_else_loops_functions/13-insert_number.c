#include "lists.h"

/**
 * insert_node - Funtion Inserts a number into a sorted singly linked list.
 * @head: pointer the head of the list.
 * @number: The number to be inserted
 *
 * Return: NULL - If function fails.
 * If Success- a pointer to the new node is returned.
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *head, *new_node;

        new_node = malloc(sizeof(listint_t));
        if (new_node == NULL)
                return (NULL);
        new_node->n = number;

        if (node == NULL || node->n >= number)
        {
                new_node->next = node;
                *head = new_node;
                return (new_node);
        }

        while (node && node->next && node->next->n < number)
                node = node->next;

        new_node->next = node->next;
        node->next = new_node;

        return (new_node);
}
