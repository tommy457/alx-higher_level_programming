#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: start of the linked list to be cheked
 *
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *tmp;
	listint_t *fist_half = *head;
	listint_t *second_half;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	while(slow)
	{
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}
	second_half = prev;
	while (second_half)
	{
		if (fist_half->n != second_half->n)
			return (0);
		fist_half = fist_half->next;
		second_half = second_half->next;
	}
	return (1);
}
