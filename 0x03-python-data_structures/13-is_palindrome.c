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
	listint_t *h = *head;
	int *tmp;
	size_t size, i;

	if (*head == NULL)
		return (1);
	for (size = 0; h->next; h = h->next, size++)
		continue;
	tmp = malloc(sizeof(int) * (size + 1));
	if (tmp == NULL)
		return (0);
	h = *head;
	for (i = 0; h; h = h->next, i++)
		tmp[i] = h->n;
	for (i = 0; i <= size; i++)
	{
		if (tmp[i] != tmp[size - i])
		{
			free(tmp);
			return (0);
		}
	}
	free(tmp);
	return (1);
}
