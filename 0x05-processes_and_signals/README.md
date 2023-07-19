# 0x05. Processes and signals
## Tasks

0. Write a Bash script that displays its own PID.
1. Write a Bash script that displays a list of currently running processes.
Requirements:
- Must show all processes, for all users, including those which might not have a TTY
- Display in a user-oriented format
- Show process hierarchy

2. Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.

Requirements:

- You cannot use `pgrep`
- The third line of your script must be `# shellcheck disable=SC2009`

3. Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`. Requirements:
You cannot use `ps`

4. Write a Bash script that displays `To infinity and beyond` indefinitely.
Requirements:

- In between each iteration of the loop, add a `sleep 2`

**More Info**

**The second line of all your Bash scripts should be a comment explaining what is the script doing**
