#include "lists.h"

/**
 * check_cycle - function in that checks if a singly linked list has a cycle
 * @list: pointer to listint_t linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	for (; list && tmp; list = list->next, tmp = tmp->next)
	{
		tmp = tmp->next;
		if (tmp == list)
			return (1);
	}
	return (0);

}
