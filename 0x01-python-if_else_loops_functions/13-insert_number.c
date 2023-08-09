#include "lists.h"

/**
 * insert_node - inserts node in sorted linked list
 * @head: head of linked list
 * @number: value of node to be inserted
 * Return: inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *new;

	curr = *head;
	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!curr || new->n < curr->n)
	{
		new->next = curr;
		return (*head = new);
	}

	while (curr)
	{
		if (!curr->next || new->n < curr->next->n)
		{
			new->next = curr->next;
			curr->next = new;
			return (curr);
		}
		curr = curr->next;
	}
	return (NULL);
}
