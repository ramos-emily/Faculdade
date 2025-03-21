#include <stdio.h>
#include <string.h>

int main() {
    int age;

    printf("Digite a sua idade: ");
    scanf("%d", &age);



    if (age >= 18) {
        printf("Habilitado!!!");
    } else {
        printf("nao pode veii!, nao ta Habilitado!!!");
    }
    return 0;

}

// TIP See CLion help at <a
// href="https://www.jetbrains.com/help/clion/">jetbrains.com/help/clion/</a>.
//  Also, you can try interactive lessons for CLion by selecting
//  'Help | Learn IDE Features' from the main menu.