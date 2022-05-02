from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next  
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def get(self, index):
        pass

    def set(self, index, elem):
        pass

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("teu cu é meu")
        if pointer:
            return pointer.data
        else: 
            raise IndexError("TEU CU É MEU")

    def __setitem__(self, index, elem):
        ointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("teu cu é meu")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("TEU CU É MEU")


lista = LinkedList()

