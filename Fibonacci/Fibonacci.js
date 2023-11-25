function fibonacci_dc(n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci_dc(n - 1) + fibonacci_dc(n - 2);
    }
}

function fibonacci_top_down(n, memo = {}) {
    if (n <= 1) {
        return n;
    } else if (!(n in memo)) {
        memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo);
    }
    return memo[n];
}

function fibonacci_bottom_up(n) {
    if (n <= 1) {
        return n;
    }
    const fib = new Array(n + 1).fill(0);
    fib[1] = 1;
    for (let i = 2; i <= n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib[n];
}

function main() {
    const n = parseInt(prompt("Digite um número inteiro não-negativo:"));

    const result_dc = fibonacci_dc(n);
    console.log(`Algoritmo de Divisão e Conquista: O ${n}-ésimo termo na sequência de Fibonacci é: ${result_dc}`);

    const result_top_down = fibonacci_top_down(n);
    console.log(`Algoritmo de Programação Dinâmica (Top-Down): O ${n}-ésimo termo na sequência de Fibonacci é: ${result_top_down}`);

    const result_bottom_up = fibonacci_bottom_up(n);
    console.log(`Algoritmo de Programação Dinâmica (Bottom-Up): O ${n}-ésimo termo na sequência de Fibonacci é: ${result_bottom_up}`);
}

main();
