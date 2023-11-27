#include "lists.h"

/**
 * check_cycle - function to checks if a linked list contains a cycle
 * @list: linked list to be checked
 *
 * Return: 0 if No cycle in the linked list, 1 if it has a cycle.
 */
int check_cycle(listint_t *list)
{
        listint_t *once_ptr = list;
        listint_t *twice_ptr = list;

        if (list == NULL)
                return (0);

        while (once_ptr &&  twice_ptr && twice_ptr->next)
        {
                once_ptr = once_ptr->next;
                twice_ptr = twice_ptr->next->next;
                if (once_ptr == twice_ptr)
                        return (1);
        }

        return (0);
}
