#include <iostream>
#include <string>
#include <cctype>

using namespace std;

string normalizeKey(string key)
{
    string result = "";
    bool used[26] = { false };

    for (char ch : key)
    {
        if (!isalpha(ch))
            continue;

        ch = toupper(ch);

        if (ch == 'J')
            ch = 'I';

        int index = ch - 'A';

        if (!used[index])
        {
            used[index] = true;
            result += ch;
        }
    }

    return result;
}

void createMatrix(string normalizedKey, char matrix[5][5])
{
    string alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    string matrixString = normalizedKey;

    for (char ch : alphabet)
    {
        if (matrixString.find(ch) == string::npos)
        {
            matrixString += ch;
        }
    }

    int index = 0;

    for (int row = 0; row < 5; row++)
    {
        for (int col = 0; col < 5; col++)
        {
            matrix[row][col] = matrixString[index];
            index++;
        }
    }
}

void displayMatrix(char matrix[5][5])
{
    cout << "\nPlayfair Matrix:" << endl;

    for (int row = 0; row < 5; row++)
    {
        for (int col = 0; col < 5; col++)
        {
            cout << matrix[row][col] << " ";
        }

        cout << endl;
    }
}

string preparePlaintext(string text)
{
    string cleanText = "";

    for (char ch : text)
    {
        if (!isalpha(ch))
            continue;

        ch = toupper(ch);

        if (ch == 'J')
            ch = 'I';

        cleanText += ch;
    }

    string result = "";

    int i = 0;

    while (i < cleanText.length())
    {
        char first = cleanText[i];

        if (i + 1 >= cleanText.length())
        {
            result += first;

            if (first == 'X')
                result += 'Q';
            else
                result += 'X';

            i++;
        }
        else
        {
            char second = cleanText[i + 1];

            if (first == second)
            {
                result += first;

                if (first == 'X')
                    result += 'Q';
                else
                    result += 'X';

                i++;
            }
            else
            {
                result += first;
                result += second;
                i += 2;
            }
        }
    }

    return result;
}

void findPosition(char matrix[5][5], char ch, int& row, int& col)
{
    row = -1;
    col = -1;

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (matrix[i][j] == ch)
            {
                row = i;
                col = j;
                return;
            }
        }
    }
}

string encryptPlayfair(string plaintext, char matrix[5][5])
{
    string ciphertext = "";

    for (int i = 0; i < plaintext.length(); i += 2)
    {
        char first = plaintext[i];
        char second = plaintext[i + 1];

        int row1, col1;
        int row2, col2;

        findPosition(matrix, first, row1, col1);
        findPosition(matrix, second, row2, col2);

        if (row1 == row2)
        {
            ciphertext += matrix[row1][(col1 + 1) % 5];
            ciphertext += matrix[row2][(col2 + 1) % 5];
        }

        else if (col1 == col2)
        {
            ciphertext += matrix[(row1 + 1) % 5][col1];
            ciphertext += matrix[(row2 + 1) % 5][col2];
        }

        else
        {
            ciphertext += matrix[row1][col2];
            ciphertext += matrix[row2][col1];
        }
    }

    return ciphertext;
}

string prepareCiphertext(string text)
{
    string result = "";

    for (char ch : text)
    {
        if (!isalpha(ch))
            continue;

        ch = toupper(ch);

        if (ch == 'J')
            ch = 'I';

        result += ch;
    }

    return result;
}

string decryptPlayfair(string ciphertext, char matrix[5][5])
{
    string plaintext = "";

    for (int i = 0; i < ciphertext.length(); i += 2)
    {
        char first = ciphertext[i];
        char second = ciphertext[i + 1];

        int row1, col1;
        int row2, col2;

        findPosition(matrix, first, row1, col1);
        findPosition(matrix, second, row2, col2);

        if (row1 == row2)
        {
            plaintext += matrix[row1][(col1 + 4) % 5];
            plaintext += matrix[row2][(col2 + 4) % 5];
        }

        else if (col1 == col2)
        {
            plaintext += matrix[(row1 + 4) % 5][col1];
            plaintext += matrix[(row2 + 4) % 5][col2];
        }

        else
        {
            plaintext += matrix[row1][col2];
            plaintext += matrix[row2][col1];
        }
    }

    return plaintext;
}

int main()
{
    int choice;
    string key;
    string text;
    string normalizedKey;
    char matrix[5][5];

    while (true)
    {
        cout << "\nPLAYFAIR CIPHER" << endl;
        cout << "1. Encrypt" << endl;
        cout << "2. Decrypt" << endl;
        cout << "0. Exit" << endl;
        cout << "Choose: ";

        cin >> choice;
        cin.ignore();

        if (choice == 1)
        {
            cout << "Enter key: ";
            getline(cin, key);

            normalizedKey = normalizeKey(key);

            cout << "Normalized key: " << normalizedKey << endl;

            createMatrix(normalizedKey, matrix);
            displayMatrix(matrix);

            cout << "Enter plaintext: ";
            getline(cin, text);

            string preparedText = preparePlaintext(text);
            string ciphertext = encryptPlayfair(preparedText, matrix);

            cout << "\nKey: " << key << endl;
            cout << "Plaintext: " << text << endl;
            cout << "Prepared plaintext: " << preparedText << endl;
            cout << "Ciphertext: " << ciphertext << endl;
        }

        else if (choice == 2)
        {
            cout << "Enter key: ";
            getline(cin, key);

            normalizedKey = normalizeKey(key);

            cout << "Normalized key: " << normalizedKey << endl;

            createMatrix(normalizedKey, matrix);
            displayMatrix(matrix);

            cout << "Enter ciphertext: ";
            getline(cin, text);

            string preparedCiphertext = prepareCiphertext(text);

            if (preparedCiphertext.length() % 2 != 0)
            {
                cout << "Error: Ciphertext length must be even!" << endl;
                continue;
            }

            string decryptedText =
                decryptPlayfair(preparedCiphertext, matrix);

            cout << "\nKey: " << key << endl;
            cout << "Ciphertext: " << text << endl;
            cout << "Prepared ciphertext: "
                 << preparedCiphertext << endl;
            cout << "Decrypted text: "
                 << decryptedText << endl;
        }

        else if (choice == 0)
        {
            cout << "Exit program." << endl;
            break;
        }

        else
        {
            cout << "Invalid choice!" << endl;
        }
    }

    return 0;
}