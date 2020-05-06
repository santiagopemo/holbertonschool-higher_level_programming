#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to a listint_t linked list head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *h = *head, *t;
	int size, i, j;

	if (*head == NULL)
		return (1);
	for (size = 0; h->next; h = h->next, size++)
		continue;
	for (t = *head, i = 0; i <= size; i++, t = t->next)
	{
		for (h = *head, j = 0; j < size - i; j++, h = h->next)
			continue;
		if (t->n != h->n)
			return (0);
	}
	return (1);
}
