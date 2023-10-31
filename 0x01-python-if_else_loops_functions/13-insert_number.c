#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a node in a sorted singly-linked list
 * @head: A pointer to a pointer to the head of the list
 * @number: The value to insert in the list
 *
 * Return: The address of the newly added node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev = NULL;

	if (head == NULL)
		return (NULL);

	/* declare new node */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	/* initialize new node */
	new->n = number;
	new->next = NULL;

	current = *head;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		prev->next = new;
		new->next = current;
	}
	return (new);
}
