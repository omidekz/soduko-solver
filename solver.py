from math import inf
import copy


class _Solver:
    def __get_empty_houses(self):
        pass

    def __get_domains(self):
        pass

    def __solve(self, path):
        pass

    def __mkdomain(self):
        pass


def _checker(f):

    def call(self, table):
        if table is None:
            raise Exception("table is None Exception")
        if type(table) is not list:
            raise Exception("table is not list")
        for index, line in enumerate(table):
            if type(line) is not list:
                raise Exception(table[index], "is not list")
            if len(line) is not len(table):
                raise Exception("i can solve n * n sudoku. len(table[%d]) != len(table)" % index)
        return f(self, table)

    return call


class Solver(_Solver):
    @_checker
    def __init__(self, table):
        self.table = copy.deepcopy(table)
        self.table_size = len(table)

    def __get_empty_houses(self):
        return [(row, col)
                for row in range(self.table_size)
                for col in range(self.table_size)
                if self.table[row][col] == 0]

    def __get_domains(self):
        table_size = self.table_size
        empty_houses = self.__get_empty_houses()
        empty_domains = list()
        for tup_row_index, tup_col_index in empty_houses:

            domain = self.__mkdomain()

            # walk on row and reduce the domain
            for col in self.table[tup_row_index]:
                if col is not 0 and domain.__contains__(col):
                    domain.remove(col)

            # walk on col and reduce the domain
            for row_index in range(table_size):
                if self.table[row_index][tup_col_index] is not 0 \
                        and domain.__contains__(self.table[row_index][tup_col_index]):
                    domain.remove(self.table[row_index][tup_col_index])

            if table_size == 9:
                # walk on section
                s_row = int(tup_row_index / 3)
                s_col = int(tup_col_index / 3)
                for i in range(3):
                    for j in range(3):
                        rr = s_row * 3 + i
                        cc = s_col * 3 + j
                        if not self.table[rr][cc] == 0 and domain.__contains__(self.table[rr][cc]):
                            domain.remove(self.table[rr][cc])

            empty_domains.append((tup_row_index, tup_col_index, domain))
        return empty_domains

    def __mkdomain(self):
        return list(range(1, self.table_size + 1))

    def __check_for_solve(self):
        table_size = self.table_size

        # rows checker
        for line in self.table:
            domain = self.__mkdomain()
            for atom in line:
                if domain.__contains__(atom):
                    domain.remove(atom)
            if len(domain) is not 0:
                return False

        # cols checker
        for col_index in range(table_size):
            domain = self.__mkdomain()
            for row_index in range(table_size):
                if domain.__contains__(self.table[row_index][col_index]):
                    domain.remove(self.table[row_index][col_index])
            if len(domain) is not 0:
                return False

        return True

    def solve(self):
        return self.__solve(list())[1]

    def __solve(self, path: list):
        if self.__check_for_solve():
            return True, path

        empty_domains = self.__get_domains()
        if len(empty_domains) is 0:
            return False, path

        min_index = [inf, -1]
        for i in enumerate(empty_domains):
            if len(i[1][2]) < min_index[0]:
                min_index = [len(i[1][2]), i[0]]

        min_index = min_index[1]
        row = empty_domains[min_index][0]
        col = empty_domains[min_index][1]
        domain = empty_domains[min_index][2]
        for i in domain:
            self.table[row][col] = i

            path.append(copy.deepcopy(self.table))
            result = self.__solve(path)
            if result[0]:
                return result
            path.pop()

        self.table[row][col] = 0
        return False, path
