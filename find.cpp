#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s function_name\n", argv[0]);
        exit(1);
    }

    char cmd[256];
    snprintf(cmd, sizeof(cmd), "cat /proc/kallsyms | grep ' %s$'", argv[1]);

    FILE *fp = popen(cmd, "r");
    if (fp == NULL) {
        perror("popen");
        exit(1);
    }

    char line[256];
    while (fgets(line, sizeof(line), fp) != NULL) {
        printf("%s", line);
    }

    pclose(fp);
    return 0;
}
