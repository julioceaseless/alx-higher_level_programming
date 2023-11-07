#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverseList - reverses the linked list. Used as a helper function
 * to reverse half of the linked list
 * @head: head pointer or pointer to the starting position
 * Return: returns the new first node
 */
listint_t *reverseList(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *current = NULL;

	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
/**
 * is_palindrome - checks if the content of a linked list is palindrome.
 * @head: node pointer to the begining for the linked list
 * Return: 1 if palindrome and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half = NULL, *first_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* reverse the second half */
	second_half = reverseList(&slow->next);

	/* compare first half with second half */
	first_half = *head;
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}
