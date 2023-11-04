<h1 align="center">
  <img src="coffe_img.png" alt="coffe" width="70">
<br>
Federal University of Rio Grande - FURG 

Coffee Team - Sistema de Arquivos ☕ 
</h1>

<p> This project is to implement an i-node based file system. Your 256MB hard drive uses 4KB blocks. Each i-node stores file/directory details and access permissions. The system supports file and directory operations like creation, removal, content addition, reading, copying, renaming, and linking.
  
The objective of this work is to implement a file system based on i-nodes. To do this, consider the following information:

Your hard drive has a capacity of 256 MB
Data storage blocks are 4 KB
That each i-node has the following structure:
File/directory name
The creator
Owner
Size
Creation date
Date modification
Access permissions (owner and other users – read, write, execute)
Block pointers
Pointer to any other i-node
Remember that part of the hard disk space is used to store management information, that is, controlling which blocks/i-nodes are free or occupied and also the i-nodes themselves.

The file system must support the following operations:

File operations:

    - Create file (touch file)
    - Remove file (rm file)
    - Create a file adding content (echo "legal content" > file)
    - Add content to an existing file or create it if it doesn't exist (echo "cool content" >> file)
    - Read file (cat file)
    - Copy file (cp file1 file2)
    - Rename/move file (mv file1 file2)
    - Create links between files (ln -s fileOriginal link)

Directory Operations:

    - Create directory (mkdir directory)
    - Remove directory (rmdir directory) - only works if the directory is empty
    - List the contents of a directory (ls directory)
    - Change directory (cd directory)
        * Don't forget special files. That's it ..
    - Rename/move directory (mv directory1 directory2)

    - Create links between directories (ln -s fileOriginal link) </p>

<h2 align="center" >
Instruções de execução do Gerenciador de Processos
</h2>

<h4>
  
  
    Passo 1: Abra o seu terminal (cmd) e digite o seguinte comando para executar o programa:
    python main.py    
    Passo 2: Informe o nome do arquivo que deseja usar, juntamente de sua extensão.
  
    -> Para testar o algoritmo de alternância circular digite "alternancia.txt".
    -> Para testar o algoritmo de prioridades digite "prioridades.txt".
    -> Para testar o algoritmo de loteria digite "loteria.txt".
    -> Para testar o algoritmo de CFS digite "cfs.txt".

    Passo 3: Com o seu programa em execução é possível inserir um novo processo. Para isso, digite um processo seguindo o seguinte formato: 
    nomeProcesso|PID|tempoDeExecução|prioridade (ou bilhetes)|UID|qtdeMemoria

    Exemplo de novo processo para ser inserido: processo-1111|1111|56|99|1|5120
</h4>



