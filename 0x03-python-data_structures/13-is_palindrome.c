#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int arr[20], count = 0, i = 0, j = 0;
	listint_t *tmp = *head;
	listint_t *tmp1 = *head;

	while (tmp != NULL)
	{
		arr[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}

	while (tmp1 != NULL)
	{
		if (arr[j] == tmp1->n)
			count++;

		tmp1 = tmp1->next;
		j++;
	}

	if (count <= 2)
		return 1;
	else
		return 0;
}
