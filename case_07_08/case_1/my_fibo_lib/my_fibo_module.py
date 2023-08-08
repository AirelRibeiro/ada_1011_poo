class Fibonacci:
    def gerar_sequencia(self, n):
        sequence = []
        for i in range(n):
            sequence.append(self.recur_fibo(i))
        return sequence

    def recur_fibo(self, n):
        if n <= 1:
            return n
        else:
            return self.recur_fibo(n - 1) + self.recur_fibo(n - 2)
