#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void generateMatrix(int n, char *startDirection, char *spiralDirection, int ***matrix);
void printMatrix(int n, int ***matrix);
void saveMatrix(int n, char *startDirection, char *spiralDirection, int ***matrix);
void loadMatrix(int n, char *startDirection, char *spiralDirection, int ***matrix);

int main(int argc, char const *argv[])
{
    int mn;

    printf("-------------------------------------------");
    printf("Spiral Matrix");
    printf("-------------------------------------------\n\n");

    int **matrix = NULL;

    int n;
    char startDirection[10];
    char spiralDirection[10];

    while (mn != 5)
    {
        printf("0 - User guide\n");
        printf("1 - Generate a matrix\n");
        printf("2 - Save a matrix\n");
        printf("3 - Load a matrix\n");
        printf("4 - Print actual matrix\n");
        printf("5 - Exit\n");

        scanf("%d", &mn);

        switch (mn)
        {
        case 0:
            printf("    0 - Felhasznaloi kezikonyv, kiirja minden menupont mukodeset\n    1 - General egy n*n meretu matrixot megadott kezdoirannyal es spiral irannyal\n    2 - Elmenti az aktualis matrixot\n    3 - Betolti az adott matrixot faljbol, ha letezik olyan\n    4 - Kirajzolja az aktualis matrixot\n    5 - Kilep\n");
            break;
        case 1:
            printf("n (matrxi merete): ");
            scanf("%d", &n);
            printf("Kezdo irany: (jobbra, balra, fel, le): ");
            scanf("%s", &startDirection);
            printf("Spiral irany: (cw, ccw): ");
            scanf("%s", &spiralDirection);
            if ((strcmp(startDirection, "jobbra") == 0 || strcmp(startDirection, "balra") == 0 || strcmp(startDirection, "fel") == 0 || strcmp(startDirection, "le") == 0) && (strcmp(spiralDirection, "cw") == 0 || strcmp(spiralDirection, "ccw") == 0))
            {
                generateMatrix(n, startDirection, spiralDirection, &matrix);
            }
            break;
        case 2:
            if (matrix != NULL)
                saveMatrix(n, startDirection, spiralDirection, &matrix);
            break;
        case 3:
            printf("n (matrxi merete): ");
            scanf("%d", &n);
            printf("Kezdo irany: (jobbra, balra, fel, le): ");
            scanf("%s", &startDirection);
            printf("Spiral irany: (cw, ccw): ");
            scanf("%s", &spiralDirection);
            if ((strcmp(startDirection, "jobbra") == 0 || strcmp(startDirection, "balra") == 0 || strcmp(startDirection, "fel") == 0 || strcmp(startDirection, "le") == 0) && (strcmp(spiralDirection, "cw") == 0 || strcmp(spiralDirection, "ccw") == 0))
            {
                loadMatrix(n, startDirection, spiralDirection, &matrix);
            }
            break;
        case 4:
            if (matrix != NULL)
                printMatrix(n, &matrix);
            break;
        default:
            break;
        }
    }

    for (int i = 0; i < n; i++)
    {
        free(matrix[i]);
    }
    free(matrix);
    return 0;
}

void generateMatrix(int n, char *startDirection, char *spiralDirection, int ***matrix)
{

    *matrix = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++)
    {
        (*matrix)[i] = (int *)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++)
        {
            (*matrix)[i][j] = 0;
        }
    }

    int num = 1;
    int row = n / 2;
    int col = n / 2;

    if (n % 2 == 0)
    {
        if (strcmp(startDirection, "jobbra") == 0 && strcmp(spiralDirection, "cw") == 0)
        {
            col -= 1;
            row -= 1;
        }
        if (strcmp(startDirection, "jobbra") == 0 && strcmp(spiralDirection, "ccw") == 0)
        {
            col -= 1;
        }
        if (strcmp(startDirection, "balra") == 0 && strcmp(spiralDirection, "ccw") == 0)
        {
            row -= 1;
        }
        if (strcmp(startDirection, "le") == 0 && strcmp(spiralDirection, "cw") == 0)
        {
            row -= 1;
        }
        if (strcmp(startDirection, "le") == 0 && strcmp(spiralDirection, "ccw") == 0)
        {
            row -= 1;
            col -= 1;
        }
        if (strcmp(startDirection, "fel") == 0 && strcmp(spiralDirection, "cw") == 0)
        {
            col -= 1;
        }
    }

    (*matrix)[row][col] = num++;

    int rowOffset = 0;
    int colOffset = 0;

    if (strcmp(startDirection, "jobbra") == 0)
    {
        colOffset = 1;
    }
    else if (strcmp(startDirection, "balra") == 0)
    {
        colOffset = -1;
    }
    else if (strcmp(startDirection, "fel") == 0)
    {
        rowOffset = -1;
    }
    else if (strcmp(startDirection, "le") == 0)
    {
        rowOffset = 1;
    }
    else
    {
        return;
    }

    while (num <= n * n)
    {
        row += rowOffset;
        col += colOffset;

        (*matrix)[row][col] = num++;

        if (strcmp(spiralDirection, "cw") == 0)
        {
            if ((*matrix)[row + colOffset][col - rowOffset] == 0)
            {
                int temp = rowOffset;
                rowOffset = colOffset;
                colOffset = -temp;
            }
        }
        else if (strcmp(spiralDirection, "ccw") == 0)
        {
            if ((*matrix)[row - colOffset][col + rowOffset] == 0)
            {
                int temp = rowOffset;
                rowOffset = -colOffset;
                colOffset = temp;
            }
        }
        else
        {
            return;
        }
    }
}

void printMatrix(int n, int ***matrix)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%8d ", (*matrix)[i][j]);
        }
        printf("\n");
    }
}

void saveMatrix(int n, char *startDirection, char *spiralDirection, int ***matrix)
{
    char filename[50];
    sprintf(filename, "spiral%d%s%s.txt", n, startDirection, spiralDirection);

    FILE *file = fopen(filename, "w");

    if (file == NULL)
    {
        return;
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            fprintf(file, "%d ", (*matrix)[i][j]);
        }
        fprintf(file, "\n");
    }

    fclose(file);
}

void loadMatrix(int n, char *startDirection, char *spiralDirection, int ***matrix)
{
    char filename[50];
    sprintf(filename, "spiral%d%s%s.txt", n, startDirection, spiralDirection);

    FILE *file = fopen(filename, "r");

    if (file == NULL)
    {
        printf("Nem letezik %s nevu fajl\n", filename);
        return;
    }

    *matrix = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++)
    {
        (*matrix)[i] = (int *)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++)
        {
            fscanf(file, "%d", &(*matrix)[i][j]);
        }
    }

    fclose(file);
}
