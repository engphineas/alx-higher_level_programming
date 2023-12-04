#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*add_nodeint - function to add a new node at the beginning of a list
*@head: listint_t head
*@n: integer to add into listint_t list
*Return: address of the new added element, or NULL if failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = n;
	new_node->next = *head;
	*head = new_node;
	return (new_node);
}
/**
*is_palindrome - function to identify if a syngle linked list is palindrome
*@head: listint_t head
*Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *sec_head = *head;
	listint_t *tmp = NULL, *tmp2 = NULL;

	if (*head == NULL || sec_head->next == NULL)
		return (1);
	while (sec_head != NULL)
	{
		add_nodeint(&tmp, sec_head->n);
		sec_head = sec_head->next;
	}
	tmp2 = tmp;
	while (*head != NULL)
	{
		if ((*head)->n != tmp2->n)
		{
			free_listint(tmp);
			return (0);
		}
		*head = (*head)->next;
		tmp2 = tmp2->next;
	}
	free_listint(tmp);
	return (1);
}
