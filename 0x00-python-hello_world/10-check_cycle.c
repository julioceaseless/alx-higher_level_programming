#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle loop
 * uses the tortoise-hare algorithm
 *
 * @list: head node
 *
 * Return: 0 if no cycle and 1 is cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	if (list == NULL || list->next == NULL)
		return (0);
	hare = tortoise = list;

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;

		if (hare == tortoise)
			return (1);
	}
	return (0);
}
