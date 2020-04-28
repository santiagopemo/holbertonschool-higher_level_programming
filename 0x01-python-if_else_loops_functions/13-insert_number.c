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
	listint_t *h, *new;

	if (head == NULL)
		return (NULL);
	if (*head == NULL || (*head)->n >= number)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	h = *head;
	while (h && h->next)
	{
		if (h->next->n >= number)
			break;
		h = h->next;
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = h->next;
	h->next = new;
	return (new);
}
