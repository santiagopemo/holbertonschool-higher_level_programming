#include "lists.h"
#include <stdlib.h>

/**
 * reverse_listint - function that reverses a listint_t linked list
 * @head: double pointer to a list
 *
 * Return: pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *next;

	prev = NULL;
	for (; *head; *head = next)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to a listint_t linked list head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *h, *r, *rhead;
	int size, i;

	if (*head == NULL)
		return (1);
	for (h = *head, size = 1; h; h = h->next, size++)
		continue;
	if (size == 1)
		return (1);
	for (h = *head, i = 1; i < (size / 2); i++, h = h->next)
		continue;
	h = h->next;
	rhead = reverse_listint(&h);
	r = rhead;
	for (h = *head; r; h = h->next, r = r->next)
	{
		if (h->n != r->n)
			return (0);
	}
	reverse_listint(&rhead);
	return (1);
}
