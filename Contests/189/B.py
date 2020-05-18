class Solution:
    def arrangeWords(self, text: str) -> str:

        words = text.split()

        wordlen = list(map(len, words))

        arr = [(w, wl, ind) for w, wl, ind in zip(words, wordlen, range(len(words)))]

        # sorted first based on word length, then on appearnce order/index
        arr = sorted(arr, key = lambda x: (x[1], x[2]))

        arr = ' '.join([i[0].lower() for i in arr])

        print(arr[0].upper() + arr[1:])


class Solution:
    def arrangeWords(self, text: str) -> str:
        return " ".join(sorted(text.split(" "), key=len)).capitalize()


        # Capitalize ensures that the entire string is lower case except the first character
        # sorted ensures that if two strings have same length, the string which appeared first originally is first after sorting.