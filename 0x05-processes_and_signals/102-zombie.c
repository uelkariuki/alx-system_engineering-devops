#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <sys/wait.h>

int infinite_while(void);
/**
 * main- main function to create 5 zombie processes
 * Return: 0
 */

int main(void)
{
	pid_t child_pid;
	int a;

	for (a = 0; a < 5; a++)
	{
		child_pid = fork();

		if (child_pid == 0) /*child process*/
		{
			exit(0);
		}
		else if (child_pid > 0)
		{
			printf("Zombie process present, PID: %d\n", child_pid);
			wait(NULL);

		}
		else
		{
			perror("Try again, error occured");

		}



	}

	return (0);
}

/**
 * infinite_while- fucntion to enable parent process to not return
 * thus creating zombie processes
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
