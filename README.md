1. Info about sort type 'insert sort' - algorythm:
 > https://www.home.umk.pl/~abak/wdimat/s/InsertSort.html
 
W algorytmie sortowania przez wstawianie ciąg danych jest dzielony na dwie części:
- już uporządkowaną (przed uruchomieniem procedury nie zawiera ona żadnych elementów),
- jeszcze nie uporządkowaną (na początku zawiera wszystkie elementy).

Sposób porządkowania można opisać następująco:
- weź pierwszy element z części nieuporządkowanej (jeśli jest pusta to zakończ działanie algorytmu),
- wstaw go w odpowiednie miejsce w części uporządkowanej (po takiej operacji część nieuporządkowana jest jeden element krótsza, a część posortowana zyskuje jeden element).

Pozostaje jeszcze do rozstrzygnięcia, w jaki sposób wyznaczyć prawidłowe położenie nowego elementu w części uporządkowanej. Najprostszy sposób polega na porównaniu tego elementu z kolejnymi elementami części uporządkowanej. Jeżeli element na pozycji i jest większy od wstawianego, to ten nowy element należy wstawić między elementy na pozycjach i-1 i i. Takie podejście jest zastosowane w demonstracji poniżej. Inna strategia wstawiania elementu do uporządkowanego ciągu jest zastosowana w sortowaniu przez wstawianie z binarnym umieszczaniem.

Insertion sort is a simple and efficient algorithm for small input sizes or partially sorted data. It has a time complexity of O(n^2).

2. install all requirements
 > py -m pip install -r requirements.txt

3. run pytest
 > py -m pytest .\test.py -s -vv

