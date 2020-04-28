#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted linked list
 * @head: double pointer to head of linked list
 * @number: number to insert node
 *
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *h = *head;
	listint_t *new;

	if (*head == NULL || number <= (*head)->n)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	while (h)
	{
		if (number <= h->n)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			tmp = h->next;
			h->next = new;
			new->next = tmp;
			return (new);
		}
		h = h->next;
	}
	return (NULL);
}
