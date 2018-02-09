#include <bits/stdc++.h>
using namespace std;
 
#define MAX 4
 
#define MAX_THREAD 4
 
int matA[MAX][MAX];
int matB[MAX][MAX];
int matC[MAX][MAX];
int step_i = 0;
 
void* multi(void* arg)
{
    int core = step_i++;
 
    for (int i = core * MAX / 4; i < (core + 1) * MAX / 4; i++) 
        for (int j = 0; j < MAX; j++) 
            for (int k = 0; k < MAX; k++) 
                matC[i][j] += matA[i][k] * matB[k][j];
}
 
int main()
{
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            matA[i][j] = rand() % 10;
            matB[i][j] = rand() % 10;
        }
    }
 
    cout << endl
         << "Matrix A" << endl;
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) 
            cout << matA[i][j] << " ";
        cout << endl;
    }
 
    cout << endl
         << "Matrix B" << endl;
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) 
            cout << matB[i][j] << " ";        
        cout << endl;
    }
 
    pthread_t threads[MAX_THREAD];
    for (int i = 0; i < MAX_THREAD; i++) {
        int* p;
        pthread_create(&threads[i], NULL, multi, (void*)(p));
    }
 
    for (int i = 0; i < MAX_THREAD; i++) 
        pthread_join(threads[i], NULL);    
 
    cout << endl
         << "Multiplication of A and B" << endl;
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) 
            cout << matC[i][j] << " ";        
        cout << endl;
    }
    return 0;
}